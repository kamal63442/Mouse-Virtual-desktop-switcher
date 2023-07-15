"""
Virtual Desktop Automation Script
This script allows you to automate virtual desktop operations using mouse and keyboard inputs.

Dependencies:
- pynput library

Usage:
1. Install the pynput library using pip: `pip install pynput`.
2. Adjust the values in the script according to your screen resolution.

Functionality:
- The script detects if the cursor is over a specified start button and the selected area.
- It listens for mouse events, such as movement, scrolling, and clicking.
- When the middle mouse button is clicked while the cursor is over the start button, a new virtual desktop is created.
- When the middle mouse button is clicked while the cursor is over the selected area, the active window is closed.
- When the scroll wheel is scrolled up or down while the cursor is over the start button, the script switches between virtual desktops.

Note: This script is intended for Windows operating system.
"""

from pynput import mouse, keyboard

# Global variables
is_start_button_hovered = False  # Indicates if the cursor is over the start button
is_script_active = False  # Indicates if the script is currently active
selected_area = [(1860, 1036, 1901, 1071)]  # Coordinates of the selected area on the screen

# Create a single instance of the keyboard controller
keyboard_controller = keyboard.Controller()

def on_move(x, y):
    """
    Callback function called when the mouse moves.

    Parameters:
    - x (int): The x-coordinate of the mouse cursor.
    - y (int): The y-coordinate of the mouse cursor.
    """
    global is_start_button_hovered

    # Detect if the cursor is over the start button
    if x < 50 and y > (1080 - 50):  # Adjust the values according to your screen resolution
        is_start_button_hovered = True
    else:
        is_start_button_hovered = False

    # Check if the cursor is over the selected area
    if is_cursor_over_selected_area(x, y):
        print("Cursor is over the selected area")

def on_scroll(x, y, dx, dy):
    """
    Callback function called when the mouse wheel is scrolled.

    Parameters:
    - x (int): The x-coordinate of the mouse cursor.
    - y (int): The y-coordinate of the mouse cursor.
    - dx (int): The horizontal movement of the scroll.
    - dy (int): The vertical movement of the scroll.
    """
    global is_start_button_hovered, is_script_active

    if is_start_button_hovered and not is_script_active:
        is_script_active = True
        # Scroll up or down to switch between virtual desktops
        if dy > 0:
            keyboard_controller.press(keyboard.Key.ctrl_l)
            keyboard_controller.press(keyboard.Key.cmd_l)
            keyboard_controller.press(keyboard.Key.left)
            keyboard_controller.release(keyboard.Key.left)
            keyboard_controller.release(keyboard.Key.ctrl_l)
            keyboard_controller.release(keyboard.Key.cmd_l)
        else:
            keyboard_controller.press(keyboard.Key.ctrl_l)
            keyboard_controller.press(keyboard.Key.cmd_l)
            keyboard_controller.press(keyboard.Key.right)
            keyboard_controller.release(keyboard.Key.right)
            keyboard_controller.release(keyboard.Key.ctrl_l)
            keyboard_controller.release(keyboard.Key.cmd_l)
        
        is_script_active = False

def on_click(x, y, button, pressed):
    """
    Callback function called when the mouse button is clicked.

    Parameters:
    - x (int): The x-coordinate of the mouse cursor.
    - y (int): The y-coordinate of the mouse cursor.
    - button (pynput.mouse.Button): The mouse button that was clicked.
    - pressed (bool): Indicates if the button was pressed or released.
    """
    global is_start_button_hovered, is_script_active

    if button == mouse.Button.middle and is_start_button_hovered and not is_script_active:
        is_script_active = True
        # Create a new virtual desktop
        keyboard_controller.press(keyboard.Key.ctrl_l)
        keyboard_controller.press(keyboard.Key.cmd_l)
        keyboard_controller.press('d')
        keyboard_controller.release('d')
        keyboard_controller.release(keyboard.Key.ctrl_l)
        keyboard_controller.release(keyboard.Key.cmd_l)
        is_start_button_hovered = False  # Reset the start button hover state
        is_script_active = False

    # Check if the middle mouse button is pressed
    if button == mouse.Button.middle and pressed:
        # Check if the cursor is over the selected area
        if is_cursor_over_selected_area(x, y):
            # Close the active window
            close_active_window()

def is_cursor_over_selected_area(x, y):
    """
    Checks if the given cursor coordinates are within the selected area.

    Parameters:
    - x (int): The x-coordinate of the mouse cursor.
    - y (int): The y-coordinate of the mouse cursor.

    Returns:
    - bool: True if the cursor is within the selected area, False otherwise.
    """
    rect_x1, rect_y1, rect_x2, rect_y2 = selected_area[0]
    return rect_x1 <= x <= rect_x2 and rect_y1 <= y <= rect_y2

def close_active_window():
    """
    Closes the active window using keyboard shortcuts.
    """
    keyboard_controller = keyboard.Controller()
    keyboard_controller.press(keyboard.Key.ctrl_l)
    keyboard_controller.press(keyboard.Key.cmd_l)
    keyboard_controller.press(keyboard.KeyCode.from_vk(115))  # F4 key
    keyboard_controller.release(keyboard.KeyCode.from_vk(115))
    keyboard_controller.release(keyboard.Key.cmd_l)
    keyboard_controller.release(keyboard.Key.ctrl_l)

def start_listener():
    """
    Starts the mouse listener to detect mouse events.
    """
    # Start listening for mouse events
    with mouse.Listener(on_move=on_move, on_scroll=on_scroll, on_click=on_click) as listener:
        listener.join()

if __name__ == '__main__':
    start_listener()

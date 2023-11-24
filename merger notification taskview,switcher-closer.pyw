import pyautogui
from pynput.mouse import Listener
from pynput import mouse, keyboard

# Disable PyAutoGUI fail-safe
pyautogui.FAILSAFE = False

# Global variables
is_start_button_hovered = False
is_script_active = False
selected_area = [(1919, 1030, 1919, 1079)]  # [(1860, 1036, 1901, 1071)]

# Create a single instance of the keyboard controller
keyboard_controller = keyboard.Controller()

# Initialize the last stimulation time
last_stimulation_time = pyautogui.time.time()

# Define the cooldown period in seconds
cooldown_period = 0.7

def on_move(x, y):
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
    global is_start_button_hovered, is_script_active, last_stimulation_time

    # Check if the cursor is within the selected area
    if any(left <= x <= right and top <= y <= bottom for left, top, right, bottom in selected_area):
        current_time = pyautogui.time.time()
        # Check if enough time has passed since the last stimulation
        if current_time - last_stimulation_time >= cooldown_period:
            # Simulate Win+Tab key press
            pyautogui.hotkey('win', 'tab')
            # Update the last stimulation time
            last_stimulation_time = current_time

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
    rect_x1, rect_y1, rect_x2, rect_y2 = selected_area[0]
    return rect_x1 <= x <= rect_x2 and rect_y1 <= y <= rect_y2

def close_active_window():
    keyboard_controller = keyboard.Controller()
    keyboard_controller.press(keyboard.Key.ctrl_l)
    keyboard_controller.press(keyboard.Key.cmd_l)
    keyboard_controller.press(keyboard.KeyCode.from_vk(115))  # F4 key
    keyboard_controller.release(keyboard.KeyCode.from_vk(115))
    keyboard_controller.release(keyboard.Key.cmd_l)
    keyboard_controller.release(keyboard.Key.ctrl_l)

def start_listener():
    # Start listening for mouse events
    with mouse.Listener(on_move=on_move, on_scroll=on_scroll, on_click=on_click) as listener:
        listener.join()

# Start the listener
start_listener()

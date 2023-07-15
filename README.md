# Virtual Desktop Automation Script

The Virtual Desktop Automation Script is a Python script that enables automation of virtual desktop operations using mouse and keyboard inputs. It allows users to create new virtual desktops, switch between virtual desktops, and close active windows with simple mouse actions.

## Dependencies

The script relies on the following external library:

- **pynput**: A Python library to monitor and control input devices such as keyboard and mouse.

You can install the required dependencies using the following command:

```bash
pip install pynput
```

## Usage

1. Ensure that the required dependencies are installed.
2. Adjust the values in the script according to your screen resolution.
3. Run the script using the following command:

```bash
python virtual_desktop_automation.py
```

4. The script will start listening for mouse events.

## Functionality

The script provides the following functionality:

- **Detecting Cursor Position**: The script detects the position of the cursor and determines whether it is hovering over the start button or the selected area on the screen.

- **Creating a New Virtual Desktop**: When the middle mouse button is clicked while the cursor is over the start button, a new virtual desktop is created.

- **Switching between Virtual Desktops**: When the scroll wheel is scrolled up or down while the cursor is over the start button, the script switches between virtual desktops.

- **Closing Active Windows**: When the middle mouse button is clicked while the cursor is over the selected area, the script closes the active window.

## Script Components

The script consists of the following components:

- **Global Variables**: These variables store the current state of the script, such as whether the cursor is hovering over the start button, whether the script is active, and the coordinates of the selected area.

- **Mouse Event Callbacks**: These callback functions are triggered when specific mouse events occur, such as movement, scrolling, and clicking. They handle the corresponding actions based on the event.

- **Helper Functions**: These functions provide auxiliary functionality, such as checking if the cursor is over the selected area and closing the active window.

- **Listener Start**: The `start_listener()` function starts the mouse listener, which continuously monitors mouse events and triggers the corresponding callbacks.

## Notes

- This script is intended for Windows operating systems.
- Adjust the values in the script according to your screen resolution to ensure accurate detection of the start button and selected area.

Feel free to customize the script or integrate it into your own projects!

---

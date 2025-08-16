import pyautogui
import time

def press_enter_n_times(n, delay=0.2):
    time.sleep(3)  # Gives you 3 seconds to focus the target application
    for _ in range(n):
        pyautogui.press('enter')
        time.sleep(delay)

# Example: Press Enter 10 times with 0.5 second delay
press_enter_n_times(18)


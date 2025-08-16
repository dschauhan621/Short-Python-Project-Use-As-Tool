import pyautogui
import time

def type_and_press_enter(text, delay=0.9):
    time.sleep(3)  # Gives you 3 seconds to focus the target application
    pyautogui.typewrite(text)
    time.sleep(delay)
    pyautogui.press('enter')

# Example usage:
sentence = input("Enter the sentence to type: ")
type_and_press_enter(sentence)


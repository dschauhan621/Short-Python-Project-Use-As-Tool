# Short-Python-Project-Use-As-Tool

This repository contains short Python projects designed as practical tools for daily use. These scripts aim to simplify routine tasks and improve efficiency in everyday life.

One example is a script that allows you to press a specific key a given number of times with a fixed delay between presses.

**Before executing the code, please update the parameters as needed, such as `n_times=18` and `delay=0.2`.**

Below are some examples:

```python
# Left click
pyautogui.click()

# Right click
pyautogui.click(button='right')

# Press spacebar
pyautogui.press('space')

# Press shift
pyautogui.keyDown('shift')
pyautogui.keyUp('shift')

# Press tab
pyautogui.press('tab')
```

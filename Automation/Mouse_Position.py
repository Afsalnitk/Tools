import pyautogui
import time

time.sleep(3)
# Get mouse position
currentMouseX, currentMouseY = pyautogui.position()
print(f"Current mouse position: X={currentMouseX}, Y={currentMouseY}")

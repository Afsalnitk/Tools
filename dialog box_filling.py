import pyautogui
import time

file_path = r'D:\Other Coading\Automation\Automation_functions\jpgFileName.txt'   #It contain the file path

try:
    with open(file_path, 'r') as file:
        text = file.read().strip()  
        print(f"Read content from the file: {text}")
except FileNotFoundError:
    print("The file does not exist or the file path is incorrect.")
except Exception as e:
    print(f"An error occurred: {e}")

# Wait for the dialog box to appear 
time.sleep(2)

# Writing the text content retrieved from the file
pyautogui.write(text)

pyautogui.press('enter')  # Pressing 'enter' key after writing the text

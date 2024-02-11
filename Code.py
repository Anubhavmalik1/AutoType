import pyautogui
import time


# Set the initial delay before the script starts (in seconds)
initial_delay = 1
time.sleep(initial_delay)

# Set the text you want to type
custom_text = "Hello, I am your custom text!"

# Set the number of times you want to repeat the typing
total_iterations = 100

count = 0
while count < total_iterations:
    pyautogui.typewrite("HOLA, I AM ANUBHAV")
    pyautogui.press("enter")
    count += 1

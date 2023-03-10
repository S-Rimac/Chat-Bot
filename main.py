import pyautogui
import time

time.sleep(5)
f = open("text.txt", "r", encoding="UTF-8")
for word in f:
    striped = word.strip("\n")
    if "." in striped:
        striped = striped.replace(".", ".\n")
    if "$" in striped:
        time.sleep(10)
        continue
    pyautogui.typewrite(striped, interval=0.10)
    pyautogui.press("enter")


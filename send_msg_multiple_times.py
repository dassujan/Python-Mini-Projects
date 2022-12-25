# Firstly we have to install PyAutoGUI libary!!!
# Soo, run it on terminal ---> pip install PyAutoGUI
import pyautogui
import time
n = int(input("How many times you want to run the message : "))
s = int(input("Enter the sleep timer : "))
msg = str(input("Enter your message : "))
time.sleep(s)
count = 0
for i in range(n):      # while count < n:
    # pyautogui.typewrite(msg + ' ' + str(count))
    pyautogui.typewrite(msg)
    pyautogui.press("enter")
    count = count+1
print("Congratulations! Your message successfully printed.")
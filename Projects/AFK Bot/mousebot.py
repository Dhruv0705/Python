import pyautogui
import random
import time 

CurrentCoords = pyautogui.position()
AFKCounter = 0
while True:
    if pyautogui.position() == CurrentCoords:
        AFKCounter +=1
    else:
        AFKCounter = 0
        CurrentCoords = pyautogui.position()
    if AFKCounter > 2:
        x = random.randint(0, 5120)
        y = random.randint(1, 1440)
        pyautogui.moveTo(x, y, 0.5)
        CurrentCoords = pyautogui.position()
    print(f'AFK Counter: {AFKCounter}')
    time.sleep(2)

import cv2
import pyautogui
import numpy as np
import time

Resolution = (1920, 1080)

codec = cv2.VideoWriter_fourcc(*"XVID")

FileName = "k.avi"

FPS = 120
Prev = 0
Output = cv2.VideoWriter(FileName, codec, FPS, Resolution)

cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)

while True: 
    img = pyautogui.screenshot()
    TimeElapsed = time.time() - Prev

    
    Prev = time.time()
    Frame = np.array(img)
    Frame = cv2.cvtColor(Frame, cv2.COLOR_BGR2RGB)
    
    if cv2.waitKey(1) == ord('9'):
        break

    
Output.release()
cv2.destroyAllWindows()

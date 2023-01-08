'''
This program captures a screenshot of the current screen every 1/fps seconds and writes it to an output video file. 
    The output video file is encoded with the XVID codec at a frame rate of 20 fps and has a resolution of 1920x1080. 
    The code also creates a window called "Live" and displays the captured screenshot in it. 
    The window is resized to 480x270. 
    The code runs in a loop until the user presses the '9' key, at which point it breaks out of the loop and releases 
    the output video file. It then closes all windows.
'''

import cv2
import pyautogui
import numpy as np
import time

# Set the resolution for the video
Resolution = (1920, 1080)

# Set the codec for the video
fourcc = cv2.VideoWriter_fourcc(*"XVID")

# Set the frame rate for the video
fps = 60.0

# Initialize a previous time variable
prev = 0

# Create a VideoWriter object to save the video to a file
Output = cv2.VideoWriter("output.avi", fourcc, 20.0, (Resolution))

# Create a window to display the video
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# Resize the window to a smaller size
cv2.resizeWindow("Live", 480, 270)

# Start a loop to continuously capture and save video frames
while True: 

    # Calculate the time elapsed since the last frame was captured
    TimeElapsed = time.time() - prev

    # Capture a screenshot
    img = pyautogui.screenshot()

    # If the elapsed time is greater than the time needed to capture a frame at the specified frame rate
    if TimeElapsed > 1.0/fps:
        # Update the previous time variable to the current time
        prev = time.time()

        # Convert the screenshot to a numpy array
        Frame = np.array(img)

        # Convert the frame from BGR to RGB
        Frame = cv2.cvtColor(Frame, cv2.COLOR_BGR2RGB)

        # Write the frame to the video file
        Output.write(Frame)

    # If the user presses the '9' key, break out of the loop
    if cv2.waitKey(100) == ord('9'):
        break

# Release the video file and close all windows
Output.release()
cv2.destroyAllWindows()

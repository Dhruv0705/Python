'''
This program is a Python program that creates a graphical user interface (GUI) using the Tkinter library. 
    The GUI has four buttons that, when clicked, perform different actions related to shutting down the computer.
'''

# Import Tkinter module and os module
from tkinter import *
import os

# Create the main window
ShutDownApp = Tk()

# Set the title of the window
ShutDownApp.title("ShutDown App")

# Set the size of the window
ShutDownApp.geometry("1000x1000")

# Set the background color of the window
ShutDownApp.config(bg="Black")

# Define a function to restart the system
def Restart():

    # Run the command to restart the system in 1 second
    os.system("shutdown /r /t 1")

# Define a function to restart the system with a timer
def RestartTimer():

    # Run the command to restart the system with a 20 second timer
    os.system("shutdown /r /t 20")

# Define a function to log out of the current user
def LogOut():

    # # Run the command to log out of the current user
    os.system("shutdown -1")

# Define a function to shutdown the system
def Shutdown():

    # Run the command to shutdown the system
    os.system("shutdown /s /t 1")

# Create a button to restart the system, & Set the position and size of the button
RestartButton = Button(ShutDownApp, command=Restart(), text="Restart", font=("Time New Roman", 20, "bold"), relief=RAISED, cursor="Plus")
RestartButton.place(x=300, y=50, height=60, width=400)

# Create a button to restart the system with a timer
RestartTimerButton = Button(ShutDownApp, command=RestartTimer, text="Restart Timer", font=("Time New Roman", 20, "bold"), relief=RAISED, cursor="Plus")
RestartTimerButton.place(x=300, y=250, height=60, width=400)

# Create a button to log out of the current user, & Set the position and size of the button
LogOutButton = Button(ShutDownApp, command=LogOut ,text="Log-Out", font=("Time New Roman", 20, "bold"), relief=RAISED, cursor="Plus")
LogOutButton.place(x=300, y=450, height=60, width=400)

# Create a button to shutdown the system, & Set the position and size of the button
ShutDownButton = Button(ShutDownApp, command=Shutdown , text="Shut Down", font=("Time New Roman", 20, "bold"), relief=RAISED, cursor="Plus")
ShutDownButton.place(x=300, y=650, height=60, width=400)

# Run the main loop for the window
ShutDownApp.mainloop()
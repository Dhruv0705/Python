from tkinter import *
from PIL import ImageTk, Image


# Define Widget
root = Tk()
root.title('Tkinter App')


class HelloWorld:

    # Creating a Label Widget
    MyLabel1 = Label(root, text = "Hello World!")
    MyLabel2 = Label(root, text = "My Name Is Dhruv")

    # Grid Layout
    MyLabel1.grid(row = 0, column = 0, columnspan=3, padx=10, pady=10)
    MyLabel2.grid(row = 1, column = 0, columnspan=3, padx=10, pady=10)

class ClickMeButton:
    def MyClick():
        MyLabel3 = Label(root, text = "Look! I Clicked A Button!")
        MyLabel3.grid(row = 2, column =0, columnspan=3, padx=10, pady=10)

    # Execute MyClick Function79
    # text = string input
    # state = DISABLED (Disables Button)
    # padx = Padding x-axis
    # pady = Padding y-axis
    # fg = Foreground Color ("Text Color")
    # bg = Background Color
    MyButton = Button(root, text="Click Me", padx=50 , pady = 50, command = MyClick, fg = "white", bg="black")
    MyButton.grid(row = 3, column =0, columnspan=3, padx=10, pady=10)

class InputFields:
        
    InputField = Entry(root, width = 35, bg = "grey")
    InputField.grid(row = 4, column =0, columnspan=3, padx=10, pady=10)
    InputField.insert(0, "Enter Your Name: ")

    def InputClick():

        hello = "Hello " + InputFields.InputField.get()
        InputLabel = Label(root, text = hello)
        InputLabel.grid(row = 5, column =0, columnspan=3, padx=10, pady=10)
        
    InputButton = Button(root, text="Enter Your Name", command=InputClick)      
    InputButton.grid(row = 6, column =0, columnspan=3, padx=10, pady=10)

class IconsImagesExitButtons:
    
    # Change Icon Image of App
    root.iconbitmap('')

    ButtonQuit = Button(root, text="Exit Program", padx=41, pady=20, command=root.destroy)
    ButtonQuit.grid(row=17, column=0, columnspan=3)

    #MyImage = ImageTk.PhotoImage()








# Creates Widget
root.mainloop()
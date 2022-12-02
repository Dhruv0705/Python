from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')
#root.iconbitmap('')

class ImageList:

    # Define Images
    MyImage1 = ImageTk.PhotoImage(Image.open('Images/desert.jpg'))
    MyImage2 = ImageTk.PhotoImage(Image.open('Images/desert2.jpg'))
    MyImage3 = ImageTk.PhotoImage(Image.open('Images/forest.jpg'))
    MyImage4 = ImageTk.PhotoImage(Image.open('Images/molten.jpg'))
    MyImage5 = ImageTk.PhotoImage(Image.open('Images/pinkSky.jpg'))

    # Store all Images within a list
    ImagesList = [MyImage1, MyImage2, MyImage3, MyImage4, MyImage5]

    # Create MyImage
    MyImage = Label(image = MyImage1)
    MyImage.grid(row=0, column=0, columnspan=3)

    # Create StatusBar
    StatusBar = Label(root, text="Image 1 of " + str(len(ImagesList)), bd=1, relief=SUNKEN, anchor=E)
    StatusBar.grid(row=2, column=0, columnspan=3, sticky=W+E)

class Buttons:

    # Define Forwards and Back Button to cycle thorough images.
    class ButtonFunction:

        def GoForward(ImageNumber):
            
            # Forget Previous
            ImageList.MyImage.grid_forget()

            ImageList.MyImage = Label(image= ImageList.ImagesList[ImageNumber - 1])

            # Global Variables defining each command button for next and previous to command within list to either go forward +1 or go back -1
            Buttons.NextButton = Button(root, text='Next', command=lambda: Buttons.ButtonFunction.GoForward(ImageNumber + 1))
            Buttons.BackButton = Button(root, text='Previous', command=lambda: Buttons.ButtonFunction.GoBack(ImageNumber - 1))

            # If ImageNumber is the fifth image:
            if ImageNumber == 5:

                # Then Disable NextButton
                Buttons.NextButton = Button(root, text="Next", state=DISABLED)

            ImageList.MyImage.grid(row=0, column=0, columnspan=3)
            Buttons.BackButton.grid(row=1, column=0)
            Buttons.NextButton.grid(row=1, column=2)

            # Update StatusBar
            ImageList.StatusBar = Label(root, text="Image " + str(ImageNumber) + " of " + str(len(ImageList.ImagesList)), bd=1, relief=SUNKEN, anchor=E)
            ImageList.StatusBar.grid(row=2, column=0, columnspan=3, sticky=W+E)


        def GoBack(ImageNumber):

            ImageList.MyImage.grid_forget()
            ImageList.MyImage = Label(image= ImageList.ImagesList[ImageNumber - 1])
            Buttons.NextButton = Button(root, text='Next', command=lambda: Buttons.ButtonFunction.GoForward(ImageNumber + 1))
            Buttons.BackButton = Button(root, text='Previous', command=lambda: Buttons.ButtonFunction.GoBack(ImageNumber - 1))

            # If ImageNumber is the fifth image:
            if ImageNumber == 1:

                # Then Disable BackButton
                Buttons.BackButton = Button(root, text="Previous", state=DISABLED)
            
            ImageList.MyImage.grid(row=0, column=0, columnspan=3)
            Buttons.BackButton.grid(row=1, column=0)
            Buttons.NextButton.grid(row=1, column=2)
            
            # Update StatusBar
            ImageList.StatusBar = Label(root, text="Image " + str(ImageNumber) + " of " + str(len(ImageList.ImagesList)), bd=1, relief=SUNKEN, anchor=E)
            ImageList.StatusBar.grid(row=2, column=0, columnspan=3, sticky=W+E)


    BackButton = Button(root, text='Previous', command=lambda : Buttons.ButtonFunction.GoBack())
    ExitButton = Button(root, text='Exit Program', command=root.destroy)
    NextButton = Button(root, text='Next', command=lambda: Buttons.ButtonFunction.GoForward(2))

    BackButton.grid(row=1, column=0)
    ExitButton.grid(row=1, column=1)
    NextButton.grid(row=1, column=2, pady=10)
    ImageList.StatusBar.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
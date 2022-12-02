from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')
root.iconbitmap('')

MyImage = ImageTk.PhotoImage(Image.open(''))
MyImage = Label(image = MyImage)
MyImage.pack()


root.mainloop()
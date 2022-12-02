from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


# Define Widget
root = Tk()
root.title('Tkinter App')

class TkinterDef:
    def TKINTER():
        # Tkinter is the most commonly used library for developing GUI (Graphical User Interface) in Python. 
            # It is a standard Python interface to the Tk GUI toolkit shipped with Python. 
            # As Tk and Tkinter are available on most of the Unix platforms as well as on the Windows system, developing GUI applications with Tkinter becomes the fastest and easiest.
        
        # Tkinter is the inbuilt python module that is used to create GUI applications. 
            # It is one of the most commonly used modules for creating GUI applications in Python as it is simple and easy to work with. 
            # You don’t need to worry about the installation of the Tkinter module separately as it comes with Python already. 
            # It gives an object-oriented interface to the Tk GUI toolkit.
        ''
    def GRAPHICAL_USER_INTERFACE():
        # (GUI) is a form of user interface which allows users to interact with computers through visual indicators using items such as icons, menus, windows, etc. 
            # It has advantages over the Command Line Interface(CLI) where users interact with computers by writing commands using keyboard only and whose usage is more difficult than GUI.
        ''
    def WIDGETS():
        
        # Widgets in Tkinter are the elements of GUI application which provides various controls to users to interact with the application.
        # Widget is an element of Graphical User Interface (GUI) that displays/illustrates information or gives a way for the user to interact with the OS.  
            # In Tkinter , Widgets are objects ; instances of classes that represent buttons, frames, and so on. 
        # Each separate widget is a Python object. When creating a widget, you must pass its parent as a parameter to the widget creation function. 
            # The only exception is the “root” window, which is the top-level window that will contain everything else and it does not have a parent.
            
            # WIDGET CLASSES
                # LABEL :        It is used to display text or image on the screen
                # Button:        It is used to add buttons to your application
                # Canvas:	     It is used to draw pictures and others layouts like texts, graphics etc.
                # ComboBox:      It contains a down arrow to select from list of available options
                # CheckButton:   It displays a number of options to the user as toggle buttons from which user can select any number of options.
                # RadioButton:   It is used to implement one-of-many selection as it allows only one option to be selected
                # Entry:         It is used to input single line text entry from user
                # Frame:         It is used as container to hold and organize the widgets
                # Message:       It works same as that of label and refers to multi-line and non-editable text
                # Scale:         It is used to provide a graphical slider which allows to select any value from that scale
                # Scrollbar:     It is used to scroll down the contents. It provides a slide controller.
                # SpinBox:       It is allows user to select from given set of values
                # Text:          It allows user to edit multiline text and format the way it has to be displayed
                # Menu:          It is used to create all kinds of menu used by an application

        # GEOMETRY MANAGEMENT: 
                # pack()	The Pack geometry manager packs widgets in rows or columns.
                # grid()	The Grid geometry manager puts the widgets in a 2-dimensional table. 
                    # The master widget is split into a number of rows and columns, and each “cell” in the resulting table can hold a widget.
                # place()	The Place geometry manager is the simplest of the three general geometry managers provided in Tkinter. 
                    # It allows you explicitly set the position and size of a window, either in absolute terms, or relative to another window.
        ''
    def LABEL():
        # Tkinter Label is a widget that is used to implement display boxes where you can place text or images. 
            # The text displayed by this widget can be changed by the developer at any time you want. 
            # It is also used to perform tasks such as to underline the part of the text and span the text across multiple lines. 
            # It is important to note that a label can use only one font at a time to display text. 
            # To use a label, you just have to specify what to display in it (this can be text, a bitmap, or an image).
        
        # PARAMETERS:
            #master:    This represents the parent window
            #options:   Below is the list of most commonly used options for this widget. These options can be used as key-value pairs separated by commas:
        
        # LABEL CLASSES:
            #anchor:        This options is used to control the positioning of the text if the widget has more space than required for the text. The default is anchor=CENTER, which centers the text in the available space.
            #bg:            This option is used to set the normal background clior displayed behind the label and indicator.
            #height:        This option is used to set the vertical dimension of the new frame.
            #width:         Width of the label in characters (not pixels!). If this option is not set, the label will be sized to fit its contents.
            #bd:            This option is used to set the size of the border around the indicator. Default bd value is set on 2 pixels.
            #font:          If you are displaying text in the label (with the text or textvariable option), the font option is used to specify in what font that text in the label will be displayed.
            #cursor:        It is used to specify what cursor to show when the mouse is moved over the label. The default is to use the standard cursor.
            #textvariable:  As the name suggests it is associated with a Tkinter variable (usually a StringVar) with the label. If the variable is changed, the label text is updated.
            #bitmap:        It is used to set the bitmap to the graphical object specified so that, the label can represent the graphics instead of text.
            #fg:            The label clior, used for text and bitmap labels. The default is system specific. If you are displaying a bitmap, this is the clior that will appear at the position of the 1-bits in the bitmap.
            #image:         This option is used to display a static image in the label widget.
            #padx:          This option is used to add extra spaces between left and right of the text within the label.The default value for this option is 1.
            #pady:          This option is used to add extra spaces between top and bottom of the text within the label.The default value for this option is 1.
            #justify:       This option is used to define how to align multiple lines of text. Use LEFT, RIGHT, or CENTER as its values. Note that to position the text inside the widget, use the anchor option. Default value for justify is CENTER.
            #relief:        This option is used to specify appearance of a decorative border around the label. The default value for this option is FLAT.
            #underline:     This option used to represent the index of the character in the text which is to be underlined. The indexing starts with zero in the text.
            #wraplength:    Instead of having only one line as the label text it can be broken into to the number of lines where each line has the number of characters specified to this option.
        ''

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

    # Opens Image using Pil
    'MyImage = ImageTk.PhotoImage(Image.open(''))'

    # command=root.destroy (Quits out of program)
    ButtonQuit = Button(root, text="Exit Program", padx=41, pady=20, command=root.destroy)
    ButtonQuit.grid(row=17, column=0, columnspan=3)

class Frames:

    # Define Frame
    Frame = LabelFrame(root, text='This is my Frame....', padx=50, pady=50)
    Frame.grid(row=18, column=0, columnspan=3, padx=10, pady=10)

    FrameButton = Button(Frame, text="Don't Click Here!")
    FrameButton2 = Button(Frame, text="... or here!")

    FrameButton.grid(row=19, column=0)
    FrameButton2.grid(row=20, column=1)

class RadioButtons:


    # Pass Integer Variable IntVar()
    # Pass String Variable StrVar()
    Radio = IntVar()
    Radio.get()

    def RadioClicked(value):
        RadioLabel = Label(root, text=value)
        RadioLabel.grid(row=23, column=0, columnspan=3)

    Radiobutton(root, text="Option 1", variable=Radio, value=1, command=lambda: RadioButtons.RadioClicked(RadioButtons.Radio.get())).grid(row=21, column=0, columnspan=3)
    Radiobutton(root, text="Option 1", variable=Radio, value=2, command=lambda: RadioButtons.RadioClicked(RadioButtons.Radio.get())).grid(row=22, column=0, columnspan=3)

    RadioLabel = Label(root, text=Radio.get())
    RadioLabel.grid(row=23, column=0, columnspan=3)

    '''class Pizza:
        
        TOPPINGS = [
            ("Pepperoni", "Pepperoni"),
            ("Cheese", "Cheese"),
            ("Mushroom", "Mushroom"),
            ("Onion", "Onion"),
        ]

        Pizza = StringVar()
        Pizza.set("Pepperoni")
      

        for text, Topping in TOPPINGS:
            #Radiobutton(root, text=text, variable=Pizza, value=Topping).pack()

            Radiobutton(root, text=text, variable=Pizza, value=Topping).grid(row=24, columnspan=3)


        def RadioClicked(value):
            RadioLabel = Label(root, text=value)
            RadioLabel.grid(row=28, column=0, columnspan=3)
        
        RadioButton = Button(root, text="Click Me!", command=lambda: RadioButtons.Pizza.RadioClicked(RadioButtons.Pizza.Pizza.get()))
        RadioButton.grid(row=29, column=0, columnspan=3)
        '''

class MessageBoxes:
    # MESSAGEBOX WIDGET:
        # Message Boxes Module provides a template base class as well as a variety of convenience methods for commonly used configurations. 
            # The message boxes are modal and will return a subset of (True, False, OK, None, Yes, No) based on the user’s selection.
    
    # PARAMETERS:
        # Function_Name: This parameter is used to represents an appropriate message box function.
        # title: This parameter is a string which is shown as a title of a message box.
        # message: This parameter is the string to be displayed as a message on the message box.
        # options: There are two options that can be used are:
            # default: This option is used to specify the default button like ABORT, RETRY, or IGNORE in the message box.
            # parent: This option is used to specify the window on top of which the message box is to be displayed.

    # FUNCTION NAME:
        # showinfo(): Show some relevant information to the user.
        # showwarning(): Display the warning to the user.
        # showerror(): Display the error message to the user.
        # askquestion(): Ask question and user has to answered in yes or no.
        # askokcancel(): Confirm the user’s action regarding some application activity.
        # askyesno(): User can answer in yes or no for some action.
        # askretrycancel(): Ask the user about doing a particular task again or not.

    def PopUp():
        
        # Creates a Popup on screen, (Title, Text)
        messagebox.showinfo("This is my Popup!", "Hello World")    

        '''
        messagebox.showinfo("showinfo", "Information")
  
        messagebox.showwarning("showwarning", "Warning")
  
        messagebox.showerror("showerror", "Error")
  
        messagebox.askquestion("askquestion", "Are you sure?")
  
        messagebox.askokcancel("askokcancel", "Want to continue?")
  
        messagebox.askyesno("askyesno", "Find the value?")
  
        messagebox.askretrycancel("askretrycancel", "Try again?")  
        
        ''' 

    # Creates Button Displayed as PopUp
    Button(root, text="PopUp", command=PopUp).grid(row=30, columnspan=3)


# Creates Widget
root.mainloop()
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox, filedialog, ttk
import numpy as np
import matplotlib.pyplot as plt

# Define Widget
root = Tk()
root.title('Tkinter App')
#root.geometry("1000x1000")

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
    MyLabel1.grid(row = 0, column = 0, columnspan=1, padx=10, pady=10)
    MyLabel2.grid(row = 1, column = 0, columnspan=1, padx=10, pady=10)

class ClickMeButton:
    def MyClick():
        MyLabel3 = Label(root, text = "Look! I Clicked A Button!")
        MyLabel3.grid(row = 2, column =0, columnspan=1, padx=10, pady=10)

    # Execute MyClick Function79
    # text = string input
    # state = DISABLED (Disables Button)
    # padx = Padding x-axis
    # pady = Padding y-axis
    # fg = Foreground Color ("Text Color")
    # bg = Background Color
    MyButton = Button(root, text="Click Me", padx=20 , pady = 20, command = MyClick, fg = "white", bg="black")
    MyButton.grid(row = 3, column =0, columnspan=1, padx=10, pady=10)

class InputFields:
        
    InputField = Entry(root, width = 35, bg = "grey")
    InputField.grid(row = 4, column =0, columnspan=1, padx=10, pady=10)
    InputField.insert(0, "Enter Your Name: ")

    def InputClick():

        hello = "Hello " + InputFields.InputField.get()
        InputLabel = Label(root, text = hello)
        InputLabel.grid(row = 5, column =0, columnspan=1, padx=10, pady=10)
        
    InputButton = Button(root, text="Enter Your Name", command=InputClick)      
    InputButton.grid(row = 6, column =0, columnspan=1, padx=10, pady=10)

class IconsImagesExitButtons:
    
    # Change Icon Image of App
    root.iconbitmap('')

    # Opens Image using Pil
    'MyImage = ImageTk.PhotoImage(Image.open(''))'

    # command=root.destroy (Quits out of program)
    ButtonQuit = Button(root, text="Exit Program", padx=41, pady=20, command=root.destroy)
    ButtonQuit.grid(row=17, column=0, columnspan=1)

class Frames:

    # Define Frame
    Frame = LabelFrame(root, text='This is my Frame....', padx=50, pady=50)
    Frame.grid(row=18, column=0, columnspan=1, padx=10, pady=10)

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
        RadioLabel.grid(row=23, column=0, columnspan=1)

    Radiobutton(root, text="Option 1", variable=Radio, value=1, command=lambda: RadioButtons.RadioClicked(RadioButtons.Radio.get())).grid(row=21, column=0, columnspan=1)
    Radiobutton(root, text="Option 2", variable=Radio, value=2, command=lambda: RadioButtons.RadioClicked(RadioButtons.Radio.get())).grid(row=22, column=0, columnspan=1)

    RadioLabel = Label(root, text=Radio.get())
    RadioLabel.grid(row=23, column=0, columnspan=1)

    '''class Pizza:

        RadioWindow = Toplevel()

        TOPPINGS = [
            ("Pepperoni", "Pepperoni"),
            ("Cheese", "Cheese"),
            ("Mushroom", "Mushroom"),
            ("Onion", "Onion"),
        ]

        Pizza = StringVar()
        Pizza.set("Pepperoni")
      
        # Loop is used to create multiple Radiobutton rather than creating each button separately
        for Text, Topping in TOPPINGS:
            Radiobutton(RadioWindow, text=Text, variable=Pizza, value=Topping).pack()


        def RadioClicked(value):
            RadioLabel = Label(RadioButtons.Pizza.RadioWindow, text=value)
            RadioLabel.pack()
        
        RadioButton = Button(RadioWindow, text="Click Me!", command=lambda: RadioButtons.Pizza.RadioClicked(RadioButtons.Pizza.Pizza.get()))
        RadioButton.pack()
        '''

class CheckBoxButtons:
    # SYNTAX:
        # Button = (master, option)
    # PARAMETERS:
        # master:               This parameter is used to represents the parent window.
        # options:              There are many options which are available and they can be used as key-value pairs separated by commas.
    # OPTIONS:
        # activebackground:     This option used to represent the background color when the checkbutton is under the cursor.
        # activeforeground:     This option used to represent the foreground color when the checkbutton is under the cursor.
        # bg:                   This option used to represent the normal background color displayed behind the label and indicator.
        # bitmap:               This option used to display a monochrome image on a button.
        # bd:                   This option used to represent the size of the border around the indicator and the default value is 2 pixels.
        # command:              This option is associated with a function to be called when the state of the checkbutton is changed.
        # cursor:               By using this option, the mouse cursor will change to that pattern when it is over the checkbutton.
        # disabledforeground:   The foreground color used to render the text of a disabled checkbutton. The default is a stippled version of the default foreground color.
        # font:                 This option used to represent the font used for the text.
        # fg:                   This option used to represent the color used to render the text.
        # height:               This option used to represent the number of lines of text on the checkbutton and it’s default value is 1.
        # highlightcolor:       This option used to represent the color of the focus highlight when the checkbutton has the focus.
        # image:                This option used to display a graphic image on the button.
        # justify:              This option used to control how the text is justified: CENTER, LEFT, or RIGHT.
        # offvalue:             The associated control variable is set to 0 by default if the button is unchecked. We can change the state of an unchecked variable to some other one.
        # onvalue:              The associated control variable is set to 1 by default if the button is checked. We can change the state of the checked variable to some other one.
        # padx:                 This option used to represent how much space to leave to the left and right of the checkbutton and text. It’s default value is 1 pixel.
        # pady:                 This option used to represent how much space to leave above and below the checkbutton and text. It’s default value is 1 pixel.
        # relief:               The type of the border of the checkbutton. It’s default value is set to FLAT.
        # selectcolor:          This option used to represent the color of the checkbutton when it is set. The Default is selectcolor=”red”.
        # selectimage:          The image is shown on the checkbutton when it is set.
        # state:                It represents the state of the checkbutton. By default, it is set to normal. We can change it to DISABLED to make the checkbutton unresponsive. The state of the checkbutton is ACTIVE when it is under focus.
        # text:                 This option used use newlines (“\n”) to display multiple lines of text.
        # underline:            This option used to represent the index of the character in the text which is to be underlined. The indexing starts with zero in the text.
        # variable:             This option used to represents the associated variable that tracks the state of the checkbutton.
        # width:                This option used to represents the width of the checkbutton. and also represented in the number of characters that are represented in the form of texts.
        # wraplength:           This option will be broken text into the number of pieces.
    # METHODS:
        # deselect():           This method is called to turn off the checkbutton.
        # flash():              The checkbutton is flashed between the active and normal colors.
        # invoke():             This method will invoke the method associated with the checkbutton.
        # select():             This method is called to turn on the checkbutton.
        # toggle():             This method is used to toggle between the different Checkbutton.
    
    CheckBoxButton1 = IntVar()  
    CheckBoxButton2 = IntVar()  
    CheckBoxButton3 = IntVar()

    
    Button1 = Checkbutton(root, text = "Tutorial", 
                        variable = CheckBoxButton1,
                        onvalue = 1,
                        offvalue = 0,
                        height = 2,
                        width = 10)
    
    Button2 = Checkbutton(root, text = "Student",
                        variable = CheckBoxButton2,
                        onvalue = 1,
                        offvalue = 0,
                        height = 2,
                        width = 10)
    
    Button3 = Checkbutton(root, text = "Courses",
                        variable = CheckBoxButton3,
                        onvalue = 1,
                        offvalue = 0,
                        height = 2,
                        width = 10)   

    Button1.grid(row=30, column=0, columnspan=1)
    Button2.grid(row=31, column=0, columnspan=1)
    Button3.grid(row=32, column=0, columnspan=1)

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
        Response = messagebox.showinfo("This is my Popup!", "Hello World")   

        # Returns Response in app ("ok") 
        Label(root, text=Response).grid(row=34, column=0, columnspan=1)
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
    Button(root, text="PopUp", command=PopUp).grid(row=33, columnspan=1)

class NewWindows:

    def OpenNewWindow():

        # Creates a New Window inside Tkinter App
        TopWindow = Toplevel()
        WindowLabel = Label(TopWindow, text="Hello World").pack()
        CloseButton = Button(TopWindow, text="Close Window", command= TopWindow.destroy).pack()
    
    NewWindowButton = Button(root, text="Open New Window", command= OpenNewWindow).grid(row=35, column=0, columnspan=1)

class OpenFilesDialogBox:

    def OpenFile():
        global DialogBoxImage
        root.filename = filedialog.askopenfilename(initialdir='', title="Select A File", filetypes= (("jpg Files", "*.jpg"), ("All Files", "*.*")) )
        DialogBoxLabel = Label(root, text=root.filename).grid(row=37, column=0, columnspan=1)
        DialogBoxImage = ImageTk.PhotoImage(Image.open(root.filename))
        DialogBoxImageLabel = Label(image=DialogBoxImage).grid(row=38,column=0, columnspan=1)
    

    DialogBoxButton = Button(root, text="Open File", command=OpenFile).grid(row=36, column=0, columnspan=1)

class Sliders:

    '''def Slider():
        global SliderLabel

        SliderLabel = Label(root, text=Sliders.Horizontal.get()).grid(row=41, column=0, columnspan=1)
        root.geometry(str(Sliders.Horizontal.get()) + "x" + str(Sliders.Vertical.get()))
    ''' 
    
    # Vertical Slider
    Vertical = Scale(root, from_=0, to=200).grid(row=39, column=0, columnspan=1) 

    # Horizontal Slider
    Horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL).grid(row=40, column=0, columnspan=1)

    SliderLabel = Label(root, text=Horizontal).grid(row=41, column=0, columnspan=1)
    SliderButton = Button(root, text="Slide", ).grid(row=42, column=0, columnspan=1)

class DropdownMenu:

    # Function to get all 
    def ShowSelection():
        DropDownLabel = Label(root, text=DropdownMenu.Clicked.get()).grid(row=46, column=0, columnspan=1, padx=10, pady=10)
    
    # List containing all options
    DropDownOptions = [
        "Monday", 
        "Tuesday", 
        "Wednesday", 
        "Thursday", 
        "Friday",
        "Saturday",
        "Sunday",
    ]

    Clicked = StringVar()
    
    # Set Variable to the first option within list
    Clicked.set(DropDownOptions[0])

    # Displays Option Menu show all (*) DropDownOptions 
    DropDown = OptionMenu(root, Clicked, *DropDownOptions).grid(row=44, column=0, columnspan=1, padx=10, pady=10)

    DropDownButton = Button(root, text='Show Selection', comma=ShowSelection).grid(row=45, column=0, columnspan=1)

class ComboBoxWidget:
    # combobox = ttk.Combobox(master, option=value, ...)

    # Label
    ttk.Label(root, text = "Select the Month :", font = ("Times New Roman", 10)).grid(row = 0, column = 1, padx = 10, pady = 10)
    
    n = StringVar()
    MonthChosen = ttk.Combobox(root, width = 27, 
                                textvariable = n)
    
    # Adding combobox drop down list
    MonthChosen['values'] = (' January', 
                              ' February',
                              ' March',
                              ' April',
                              ' May',
                              ' June', 
                              ' July', 
                              ' August', 
                              ' September', 
                              ' October', 
                              ' November', 
                              ' December')
    
    MonthChosen.grid(row = 0, column = 2)
    
    # Shows february as a default value
    MonthChosen.current(1) 

class Canvas:
    # The Canvas widget lets us display various graphics on the application. 
        # It can be used to draw simple shapes to complicated graphs. We can also display various kinds of custom widgets according to our needs.
    # SYNTAX:
        # C = Canvas(rot, height, width, bd, bg,...)
    # PARAMETERS:
        # root =            root window.
        # height =          height of the canvas widget.
        # width =           width of the canvas widget.
        # bg =              background color for canvas.
        # bd =              border of the canvas window.
        # scrollregion (w, n, e, s) =  tuple defined as a region for scrolling left, top, bottom and right.
        # highlightcolor =  color shown in the focus highlight.
        # cursor =          It can be defined as a cursor for the canvas which can be a circle, a do, an arrow etc.
        # confine =         decides if canvas can be accessed outside the scroll region.
        # relief =          type of the border which can be SUNKEN, RAISED, GROOVE and RIDGE.
    # DRAWING METHODS
        # Creating an Oval
            # oval = C.create_oval(x0, y0, x1, y1, options)
        # Creating an arc
            # arc = C.create_arc(20, 50, 190, 240, start=0, extent=110, fill="red")
        # Creating a Line
            # line = C.create_line(x0, y0, x1, y1, ..., xn, yn, options)
        # Creating a polygon
            # oval = C.create_polygon(x0, y0, x1, y1, ...xn, yn, options)
    C = Canvas(root, bg="yellow",
           height=150, width=200)
 
    line = C.create_line(108, 120,
                     320, 40,
                     fill="green")
 
    arc = C.create_arc(180, 150, 80,
                   210, start=0,
                   extent=220,
                   fill="red")
 
    oval = C.create_oval(80, 30, 140,
                     150,
                     fill="blue")
 
    C.grid(row = 2, column = 2)

class EntryWidget:
    # The Entry Widget is a Tkinter Widget used to Enter or display a single line of text. 
    # SYNTAX:
        # entry = tk.Entry(parent, options)
    # PARAMETERS:
        # bg :      The normal background color displayed behind the label and indicator. 
        # bd :      The size of the border around the indicator. Default is 2 pixels. 
        # font :    The font used for the text. 
        # fg :      The color used to render the text. 
        # justify : If the text contains multiple lines, this option controls how the text is justified: CENTER, LEFT, or RIGHT. 
        # relief :  With the default value, relief=FLAT. You may set this option to any of the other styles like : SUNKEN, RIGID, RAISED, GROOVE 
        # show :    Normally, the characters that the user types appear in the entry. To make a .password. entry that echoes each character as an asterisk, set show=”*”. 
            # textvariable :    In order to be able to retrieve the current text from your entry widget, you must set this option to an instance of the StringVar class.
    # METHODS:
        # get() :           Returns the entry’s current text as a string. 
        # delete() :        Deletes characters from the widget 
        # insert ( index, ‘name’) :     Inserts string ‘name’ before the character at the given index. 

    # Declaring string variable for storing name and password
    Name = StringVar()
    Password = StringVar()
    
    
    # Defining a function that will get the name and password and print them on the screen
    def Submit():
        Name = EntryWidget.Name
        Password = EntryWidget.Password

        Name = Name.get()
        Password = Password.get()

        print("The name is : " + Name)
        print("The password is : " + Password)

    Name.set("")
    Password.set("")


    # creating a label for name using widget Label
    NameLabel = Label(root, text = 'Username: ', font=('calibre',10, 'bold'))
    
    # creating a entry for input
    # name using widget Entry
    NameEntry = Entry(root,textvariable = Name, font=('calibre',10,'normal'))
    
    # creating a label for password
    PasswordLabel = Label(root, text = 'Password: ', font = ('calibre',10,'bold'))
    
    # creating a entry for password
    PasswordEntry= Entry(root, textvariable = Password, font = ('calibre',10,'normal'), show = '*')
    
    # creating a button using the widget
    # Button that will call the submit function
    SubmitButton= Button(root,text = 'Submit', command = Submit)
    
    # placing the label and entry in
    # the required position using grid
    # method
    NameLabel.grid(row=3,column=1)
    NameEntry.grid(row=3,column=2)
    PasswordLabel.grid(row=4,column=1)
    PasswordEntry.grid(row=4,column=2)
    SubmitButton.grid(row=5,column=2)

class ScrollbarWidget:
    # The scrollbar widget is used to scroll down the content. We can also create the horizontal scrollbar to the Entry widget.
    # SYNTAX:
        # w = Scrollbar(master, options) 
    # PARAMETERS:
        # master: This parameter is used to represents the parent window.
        # options: There are many options which are available and they can be used as key-value pairs separated by commas.
    # OPTIONS:
    # activebackground:     This option is used to represent the background color of the widget when it has the focus.
    # bg:                   This option is used to represent the background color of the widget.
    # bd:                   This option is used to represent the border width of the widget.
    # command:              This option can be set to the procedure associated with the list which can be called each time when the scrollbar is moved.
    # cursor:               In this option, the mouse pointer is changed to the cursor type set to this option which can be an arrow, dot, etc.
    # elementborderwidth:   This option is used to represent the border width around the arrow heads and slider. The default value is -1.
    # Highlightbackground:  This option is used to focus highlighcolor when the widget doesn’t have the focus.
    # highlighcolor:        This option is used to focus highlighcolor when the widget has the focus.
    # highlightthickness :  This option is used to represent the thickness of the focus highlight.
    # jump:                 This option is used to control the behavior of the scroll jump. If it set to 1, then the callback is called when the user releases the mouse button.
    # orient:               This option can be set to HORIZONTAL or VERTICAL depending upon the orientation of the scrollbar.
    # repeatdelay:          This option tells the duration up to which the button is to be pressed before the slider starts moving in that direction repeatedly. The default is 300 ms.
    # repeatinterval:       The default value of the repeat interval is 100.
    # takefocus:            You can tab the focus through a scrollbar widget
    # troughcolor:          This option is used to represent the color of the trough.
    # width:                This option is used to represent the width of the scrollbar.
    ''

class Graphs:
    def PlotGraph():
        HousePrices = np.random.normal(20000,25000,5000)
        plt.polar(HousePrices)
        plt.show()
    
    GraphButton = Button(root, text="Graph It!", command= PlotGraph)
    GraphButton.grid(row=10, column=2)


# Creates Widget
root.mainloop()
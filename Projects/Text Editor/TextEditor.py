import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os

MainApplication = tk.Tk()
MainApplication.geometry('500x500')
MainApplication.title("Dhruv Text Editor")


# Main Menu
class MainMenu:

    MainMenu = tk.Menu()

    # File Icon
    NewIcon = tk.PhotoImage(file='icons/new.png')
    OpenIcon = tk.PhotoImage(file='icons/open.png')
    SaveIcon = tk.PhotoImage(file='icons/save.png')
    SaveAsIcon = tk.PhotoImage(file='icons/save_as.png')
    ExitIcon = tk.PhotoImage(file='icons/exit.png')

    class File:
        File = tk.Menu(MainMenu, tearoff=False)
        
        File.add_command(label='New', image=NewIcon, command=tk.LEFT, accelerator='Ctrl+N')
        File.add_command(label='Open', image=NewIcon, command=tk.LEFT, accelerator='Ctrl+O')
        File.add_command(label='Save', image=NewIcon, command=tk.LEFT, accelerator='Ctrl+S')
        File.add_command(label='Save As', image=NewIcon, command=tk.LEFT, accelerator='Ctrl+Alt+S')
        File.add_command(label='Exit', image=NewIcon, command=tk.LEFT, accelerator='Ctrl+Q')

    class Edit:
        Edit = tk.Menu(MainMenu, tearoff=False)

    View = tk.Menu(MainMenu, tearoff=False)
    Theme = tk.Menu(MainMenu, tearoff=False)

    # Cascade
    MainMenu.add_cascade(label='File', menu=File)
    MainMenu.add_cascade(label='Edit', menu=Edit)
    MainMenu.add_cascade(label='View', menu=View)
    MainMenu.add_cascade(label='Theme', menu=Theme)


# Toolbar

# Text Editor

# Status Bar

# Functionality


MainApplication.config(menu=MainMenu.MainMenu)
MainApplication.mainloop()
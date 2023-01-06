import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os

MainApplication = tk.Tk()
MainApplication.geometry('500x500')
MainApplication.title("Dhruv Text Editor")

MainMenu = tk.Menu()

# Main Menu
class MainMenuBar:


    class File:
        
        # File Icon
        NewIcon = tk.PhotoImage(file='icons/new.png')
        OpenIcon = tk.PhotoImage(file='icons/open.png')
        SaveIcon = tk.PhotoImage(file='icons/save.png')
        SaveAsIcon = tk.PhotoImage(file='icons/save_as.png')
        ShareIcon = ''
        DownloadIcon = ''
        ExitIcon = tk.PhotoImage(file='icons/exit.png')
        
        File = tk.Menu(MainMenu, tearoff=False)
        
        File.add_command(label='New', image=NewIcon, command=tk.LEFT, accelerator='Ctrl+N')
        File.add_command(label='Save', image=SaveIcon, command=tk.LEFT, accelerator='Ctrl+S')
        File.add_command(label='Open', image=OpenIcon, command=tk.LEFT, accelerator='Ctrl+O')
        File.add_command(label='Save As', image=SaveAsIcon, command=tk.LEFT, accelerator='Ctrl+Alt+S')
        File.add_command(label='Exit', image=ExitIcon, command=tk.LEFT, accelerator='Ctrl+Q')

    class Edit:

        UndoIcon = ''
        RedoIcon = ''
        CopyIcon = ''
        PastIcon = ''
        ClearIcon = ''
        FindIcon= ''

        Edit = tk.Menu(MainMenu, tearoff=False)


    class View:
        
        ToolBarIcon = ''
        StatusBarIcon = ''
        FullScreenIcon = ''

        View = tk.Menu(MainMenu, tearoff=False)

    class Theme:

        Theme = tk.Menu(MainMenu, tearoff=False)

    # Cascade
    MainMenu.add_cascade(label='File', menu=File.File)
    MainMenu.add_cascade(label='Edit', menu=Edit.Edit)
    MainMenu.add_cascade(label='View', menu=View.View)
    MainMenu.add_cascade(label='Theme', menu=Theme.Theme)


# Toolbar

# Text Editor

# Status Bar

# Functionality


MainApplication.config(menu=MainMenu)
MainApplication.mainloop()
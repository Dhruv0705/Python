from tkinter import *

# Define Widget
root = Tk()
root.title('Basic Calculator')

class BasicCalculatorApp:

    Calculator = Entry(root, width=35, borderwidth=5)
    Calculator.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

    def ButtonClick(Number):
        Current = BasicCalculatorApp.Calculator.get()
        BasicCalculatorApp.Calculator.delete(0, END)
        BasicCalculatorApp.Calculator.insert(0, str(Current) + str(Number))

    def button_clear():
        BasicCalculatorApp.Calculator.delete(0, END)

    def button_add():
        first_number = BasicCalculatorApp.Calculator.get()
        global f_num
        global math
        math = "addition"
        f_num = int(first_number)
        BasicCalculatorApp.Calculator.delete(0, END)

    def button_equal():
        second_number = BasicCalculatorApp.Calculator.get()
        BasicCalculatorApp.Calculator.delete(0, END)
        
        if math == "addition":
            BasicCalculatorApp.Calculator.insert(0, f_num + int(second_number))

        if math == "subtraction":
            BasicCalculatorApp.Calculator.insert(0, f_num - int(second_number))

        if math == "multiplication":
            BasicCalculatorApp.Calculator.insert(0, f_num * int(second_number))

        if math == "division":
            BasicCalculatorApp.Calculator.insert(0, f_num / int(second_number))

        

    def button_subtract():
        first_number = BasicCalculatorApp.Calculator.get()
        global f_num
        global math
        math = "subtraction"
        f_num = int(first_number)
        BasicCalculatorApp.Calculator.delete(0, END)

    def button_multiply():
        first_number = BasicCalculatorApp.Calculator.get()
        global f_num
        global math
        math = "multiplication"
        f_num = int(first_number)
        BasicCalculatorApp.Calculator.delete(0, END)

    def button_divide():
        first_number = BasicCalculatorApp.Calculator.get()
        global f_num
        global math
        math = "division"
        f_num = int(first_number)
        BasicCalculatorApp.Calculator.delete(0, END)


    # Define Buttons

    button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: BasicCalculatorApp.ButtonClick(1))
    button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: BasicCalculatorApp.ButtonClick(2))
    button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: BasicCalculatorApp.ButtonClick(3))
    button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: BasicCalculatorApp.ButtonClick(4))
    button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: BasicCalculatorApp.ButtonClick(5))
    button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: BasicCalculatorApp.ButtonClick(6))
    button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: BasicCalculatorApp.ButtonClick(7))
    button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: BasicCalculatorApp.ButtonClick(8))
    button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: BasicCalculatorApp.ButtonClick(9))
    button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: BasicCalculatorApp.ButtonClick(0))
    button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
    button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
    button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)

    button_subtract = Button(root, text="-", padx=41, pady=20, command=button_subtract)
    button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
    button_divide = Button(root, text="/", padx=41, pady=20, command=button_divide)

    # Put the buttons on the screen

    button_1.grid(row=13, column=0)
    button_2.grid(row=13, column=1)
    button_3.grid(row=13, column=2)

    button_4.grid(row=12, column=0)
    button_5.grid(row=12, column=1)
    button_6.grid(row=12, column=2)

    button_7.grid(row=11, column=0)
    button_8.grid(row=11, column=1)
    button_9.grid(row=11, column=2)

    button_0.grid(row=14, column=0)
    button_clear.grid(row=14, column=1, columnspan=2)
    button_add.grid(row=15, column=0)
    button_equal.grid(row=15, column=1, columnspan=2)

    button_subtract.grid(row=16, column=0)
    button_multiply.grid(row=16, column=1)
    button_divide.grid(row=16, column=2)

# Creates Widget
root.mainloop()
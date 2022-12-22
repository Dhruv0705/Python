# CS50P Introduction to Python
class CS50PLecture0:

    class HelloWorld:
        print("Hello, World")

    class FunctionsNVariableNStrings:
        # Functions are verbs or actions that the computer or computer language will already know how to perform.
        # Variable is just a container for a value within your own program.
        # String, known as a str in Python, is a sequence of text.
        # def is custom functions we created.
            # Chain methods
            # .strip() - Strip all the whitespaces on the left and right of the users input.
            # .title() - Capitalize first letter of every new string
            # .capitalize - Capitalize first letter only

        # Ask the user for their name, remove whitespace from the str and capitalize the first letter of each word
        Name = input("What is your name? ").strip().title()

        # Concatenate variable function
        # Formate function
        print("Hello, " + Name)
        print(f"Hello, {Name} ")

        # Print Quotation within print
        print('Hello, "friend" ')
    
    class Integers:
        # In Python, an integer is referred to as an int.
        # Declared variable function
        def Int1():
            x = 1
            y = 2
            z = x + y
            print(z)
        Int1()

        # Ask user to input x and y
        def InputInt():
            
            # The most inner function is run first, and then the outer one is run.
            x = int(input('What is x? '))
            y = int(input('What is y? '))
            z = x + y 
            print(z)
        InputInt()

    class Float:
        # A floating point value is a real number that has a decimal point in it, such as 0.52.
        def Float1():
            x = float(input("What is x? "))
            y = float(input('What is y? '))

            w = x + y 

            # round() - rounds the total to the nearest integer.
            z = round(x + y)
            print(w)
            print(z)
            
            # format the output of long numbers
            print(f"{z:,}")
        Float1()
    
    class ReturnValue:

        # You can imagine many scenarios where you don’t just want a function to perform an action, 
        # but also to return a value back to the main function. 
        # For example, rather than simply printing the calculation of x + y, 
        # you may want a function to return the value of this calculation back to another part of your program. 
        # This “passing back” of a value we call a return value.

        # Effectively, x is passed to square. Then, the calculation of x * x is returned back to the main function.
        def square(n):
            return n * n

        def main():
            x = int(input("What's x? "))
            print("x squared is", CS50PLecture0.ReturnValue.square(x))

        # Runs main function
        main()
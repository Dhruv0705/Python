class CS50PLecture1:

    class Conditional:

        # Conditionals allow you, the programmer, to allow your program to make decisions: As if your program has the choice between taking the left-hand road or the right-hand road based upon certain conditions.
        # Built within Python are a set of “operators” that can are used to ask mathematical questions.
            # > and < symbols are probably quite familiar to you.
            # >= denotes “greater than or equal to.”
            # <= denotes “less than or equal to.”
            # == denotes “equals, though do notice the double equal sign! A single equal sign would assign a value. Double equal signs are used to compare variables.
            # != denotes “not equal to.
        # Conditional statements compare a left-hand term to a right-hand term.
        ''

        class IFStatement:

            x = int(input("What's x? "))
            y = int(input("What's y? "))

            # If statements use bool or boolean values (true or false) to decide whether or not to execute. 
                # If the statement of x > y is true, the compiler will register it as true and execute the code.
            if x < y:
                print("x is less than y")

        class ElifElseStatement:

            x = int(input("What's x? "))
            y = int(input("What's y? "))

            # First, the if statement is evaluated. If this statement is found to be true, 
                # all the elif statements not be run at all. 
                # However, if the if statement is evaluated and found to be false, 
                # the first elif will be evaluated. 
                # If this is true, it will not run the final evaluation.
            if x < y:
                print("x is less than y")
            elif x > y:
                print("x is greater than y")
            else:
                print("x is equal to y")
        
        class ORStatement:
           
            x = int(input("What's x? "))
            y = int(input("What's y? "))

            # or allows your program to decide between one or more alternatives. 
                # For example, we could further edit our program as follows: 
            if x < y or x > y:
                print("x is not equal to y")
            else:
                print("x is equal to y")

            class NotEqualTo:
                x = int(input("What's x? "))
                y = int(input("What's y? "))

                # if x is not equal to y then:
                    # Or else print is equal to
                if x != y:
                    print("x is not equal to y")
                else:
                    print("x is equal to y")

            class EqualTo:

                x = int(input("What's x? "))
                y = int(input("What's y? "))

                # if x is equal to y then:
                    # Or else print not equal to
                # A switch of not equal to statement.

                # == operator evaluates if what is on the left and right are equal to one another. 
                    # That use of double equal signs is very important. 
                    # If you use only one equal sign, an error will likely be thrown by the compiler.
                if x == y:
                    print("x is equal to y")
                else:
                    print("x is not equal to y")

        class AndStatement:

            # Similar to or, and can be used within conditional statements.
            score = int(input("Score: "))

            if score >= 90 and score <= 100:
                print("Grade: A")
            elif score >=80 and score < 90:
                print("Grade: B")
            elif score >=70 and score < 80:
                print("Grade: C")
            elif score >=60 and score < 70:
                print("Grade: D")
            else:
                print("Grade: F")

            class SimplifiedAndStatement:

                score = int(input("Score: "))

                if score >= 90:
                    print("Grade: A")
                elif score >= 80:
                    print("Grade: B")
                elif score >= 70:
                    print("Grade: C")
                elif score >= 60:
                    print("Grade: D")
                else:
                    print("Grade: F")
            
            class Match:
                Name = input("What's your name? ")

                if Name == "Harry" or Name == "Hermine" or Name == "Ron": 
                    print("Gryffindor")
                elif Name == "Draco":
                    print("Slytherin")
                else:
                    print("Who?")

        
        class Modulo:
            # In mathematics, parity refers to whether a number is either even or odd.
            # The modulo % operator in programming allows one to see if two numbers divide evenly or divide and have a remainder.
            # For example, 4 % 2 would result in zero, because it evenly divides. 
                # However, 3 % 2 does not divide evenly and would result in a number other than zero!

            x = int(input("What's x? "))

            if x % 2 == 0:
                print("Even")
            else:
                print("Odd")
            
            class ModuloFunction: 

                # We can create our own function to check whether a number is even or odd. 
                
                def IsEven(n):
                    if n % 2 == 0:
                        return True
                    else:
                        return False
                
                # Revision
                '''
                def is_even(n):
                    return True if n % 2 == 0 else False
                '''

                def main():
                    # The if statement simply evaluates whether or not IsEven of x is true or false.
                    x = int(input("What's x? "))
                    
                    if CS50PLecture1.Conditional.Modulo.ModuloFunction.IsEven(x):
                        print("Even")
                    else:
                        print("Odd")

                main()
            
            
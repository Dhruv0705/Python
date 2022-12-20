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
                    # Or else print is equl to
                if x != y:
                    print("x is not equal to y")
                else:
                    print("x is equal to y")

            class EqualTo:

                x = int(input("What's x? "))
                y = int(input("What's y? "))

                # if x is equal to y then:
                    # Or else print not equl to
                # A switch of notqual to statement.

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
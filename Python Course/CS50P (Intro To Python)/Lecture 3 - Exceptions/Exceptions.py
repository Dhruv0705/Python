class CS50PLecture3:

    class Exceptions:

    # Exceptions are things that go wrong within our coding.

        class Error:

            class RuntimeError:
                # Runtime errors refer to those created by unexpected behavior within your code. 
                    # For example, perhaps you intended for a user to input a number, but they input a character instead. 
                    # Your program may throw an error because of this unexpected input from the user.

                x = int(input("What's x? "))
                # f, we tell Python to interpolate what is in the curly braces as the value of x. 
                print(f"x is {x}")

                # consider “corner cases” such as -1, 0, or cat.
                # If we run this program and type in “cat”, we’ll suddenly see 
                    # ValueError: invalid literal for int() with base 10: 'cat' 
                    # Essentially, the Python interpreter does not like that we passed “cat” to the print function.

                # An effective strategy to fix this potential error would be to create “error handling” to ensure the user behaves as we intend.
        
        class TryNExcept:

            # try and except are ways of testing out user input before something goes wrong.
            try:
                x = int(input("What's x?"))
            except ValueError:
                print("x is not an integer")
            # if no exception occurs, it will then run the block of code within else. 
            else:
                print(f"x is {x}")
            
            class GetIntegerFunction:

                '''
                def main():
                    x = get_int()
                    print(f"x is {x}")


                def get_int()
                    while True:
                        try:
                            x = int(input("What's x?"))
                        except ValueError:
                            print("x is not an integer")
                        else:
                            return x


                main()
                '''

                def main():
                    x = CS50PLecture3.Exceptions.TryNExcept.GetIntegerFunction.get_int()
                    print(f"x is {x}")

                def get_int():
                    while True:
                        try:
                            return int(input("What's x?"))
                        except ValueError:
                            print("x is not an integer")

                main()

            class Pass:
                ''

class CS50PLecture5:

    class UnitTests:

        # Testing your code is a natural part of the programming process. 
            # Unit tests allow you to test specific aspects of your code. You can create your own programs that test your code. 
            # Alternatively, you can utilize frameworks like pytest to run your unit tests for you.
        
        def square(n):
            return n * n

def main():
    x = int(input("What's x? "))
    print(f"{x} squared is", CS50PLecture5.UnitTests.square(x))
        # Runs main function
main()
        
            
class Assert:

    def test_square():

        try:
            assert CS50PLecture5.UnitTests.square(2) == 4
        except AssertionError:
            print("2 squared is not 4")
        try:
            assert CS50PLecture5.UnitTests.square(3) == 9
        except AssertionError:
            print("3 squared is not 9")
        try:
            assert CS50PLecture5.UnitTests.square(-2) == 4
        except AssertionError:
            print("-2 squared is not 4")
        try:
            assert CS50PLecture5.UnitTests.square(-3) == 9
        except AssertionError:
            print("-3 squared is not 9")
        try:
            assert CS50PLecture5.UnitTests.square(0) == 0
        except AssertionError:
            print("0 squared is not 0")

    test_square()

class PyTest:

    # pytest is a third-party library that allows you to unit test your program. That is, you can test your functions within your program.

    def test_assert():

        #  asserts all the conditions that we want to test.
        assert CS50PLecture5.UnitTests.square(2) == 4
        assert CS50PLecture5.UnitTests.square(3) == 9
        assert CS50PLecture5.UnitTests.square(-2) == 4
        assert CS50PLecture5.UnitTests.square(-3) == 9
        assert CS50PLecture5.UnitTests.square(0) == 0
    
    
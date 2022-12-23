class CS50PLecture2:

    class Loops:
        
        # Loops enable you to create a block of code that executes over and over again.
        
        class While:

            # The while loop is nearly universal throughout all coding languages.

            # Initialize variable 
            i = 0

            # i < 3 allows our code to function as intended. We begin by counting with 0 and it iterates through our loop three times, producing three meows. 
            # while i variable does not equal to 0 then:
            while i < 3:

                # prints meow
                print("meow")

                # adds 1 and re loops adding 1 to i each time
                i += 1

                # i=1
                # i=2
                # i=3
                # end loop
            
            class WhileInput:
                
                def GetNumber():
                    while True:
                        n = int(input("What's n? "))
                        if n > 0:
                            break
                    return n


                def meow(n):
                    for _ in range(n):
                        print("meow")

                def main():
                    Number = CS50PLecture2.Loops.While.WhileInput.GetNumber()
                    CS50PLecture2.Loops.While.WhileInput.meow(Number)
        
        class For:

            # To best understand a for loop, it’s best to begin by talking about a new variable type called a list in Python. 
                # As in other areas of our lives, we can have a grocery list, a to-do list, etc.

            # A for loop iterates through a list of items.
            for i in [0, 1, 2]:

                # i begins with 0, meows, i is assigned 1, meows, and, finally, i is assigned 2, meows, and then ends.
                print("meow")

            # range(3) provides back three values (0, 1, and 2) automatically. This code will execute and produce the intended effect, meowing three times.
            for i in range(3):
                print("meow")

            # In Python, if such a variable does not have any other significance in our code, 
                # we can simply represent this variable as a single underscore _.
            for _ in range(3):
                print("meow")
    
        class List:

            # a list is a list of multiple values

            students = ["Hermoine", "Harry", "Ron"]

            # for each student in the students list, it will print the student as intended. 
            for student in students:
                print (student)

            class Length:

                # We can utilize len as a way of checking the length of the list called students.

                students = ["Hermoine", "Harry", "Ron"]

                # Don’t simply want to print the name of the student, but also their position in the list. 
                # Notice how executing this code results in not only getting the position of each student plus one using i + 1, but also prints the name of each student. 
                    # len allow you to dynamically see how long the list of the students is regardless how much it grows.
                for i in range(len(students)):
                    print(i + 1, students[i])
        
        class Dictionaries: 
            
            # dicts or dictionaries is a data structure that allows you to associate keys with values.
            # a dict associates a key with a value.
            # None designation where there is no value associated with a key.

            # creates a list of dicts. The list called students has four dicts within it: One for each student. 
            students = [
            {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
            {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
            {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
            {"name": "Draco", "house": "Slytherin", "patronus": None},
            ]
            
            # the for loop will iterate through each of the dicts inside the list called students.
            for student in students:
                print(student["name"], student["house"], student["patronus"], sep=", ")
        
        class Mario:

            def print_square(size):

                # For each row in square
                for i in range(size):

                    # For each brick in row
                    for j in range(size):

                        #  Print brick
                        print("#", end="")

                    # Print blank line
                    print()

            def main():
                CS50PLecture2.Loops.Mario.print_square(3)

            main()
class CS50PLecture6:

    class FileIO:

        # File I/O is the ability of a program to take a file as input or create a file as output.
        # list is a data structure that allows us to store multiple values into a single variable.
        names = []

        for _ in range(3):

            # The append method is used to add the name to our names list.  
            names.append(input("What's your name?" ))

            '''
            name = input("What's your name?" )
            
            names.append(name)
            '''

        # print the list of names as a sorted list.
        for name in sorted(names):
            print(f"hello, {name}")
    
        class OpenFile:

            class W:

                # open is a functionality built into Python that allows you to open a file and utilize it in your program. 
                    # The open function allows you to open a file such that you can read from it or write to it.
            
                name = input("What's your name? ")

                # Open function opens a file called names.txt with writing enabled, as signified by the w. 
                    # The code above assigns that opened file to a variable called file. 
                    # The line file.write(name) writes the name to the text file. The line after that closes the file.
                file = open("names.txt", "w")
                file.write(name)
                file.close()

            class A:


                name = input("What's your name? ")

                # w has been changed to a for “append”. Rerunning this program multiple times, you will notice that names will be added to the file. 
                    # However, you will notice a new problem!

                file = open("names.txt", "a")

                # add a line break at the end of each name.
                file.write(f"{name}\n")
                file.close()
            
            class With:

                # with allows you to automate the closing of a file.
                name = input("What's your name? ")

                # "r" = reads text file
                with open("names.txt", "r") as file:
                    lines = file.readlines()

                for line in lines:

                    # rstrip has the effect of removing the extraneous line break at the end of each line.
                    print("hello,", line.rstrip())

                '''
                with open("names.txt", "r") as file:
                    for line in file:
                        print("hello,", line.rstrip()) 
                '''

                class Sorting:
                    # sorting of the names:
                    names = []

                    with open("names.txt") as file:
                        for line in file:
                            names.append(line.rstrip())

                    for name in sorted(names):
                        print(f"hello, {name}")
        
        class CSV:

            # “comma separated values”.
            # csv library comes with an object called a reader.
            class Houses:
                import csv

                students = []

                with open("students.csv") as file:
                    for line in file:

                        # split function actually returns two values: The one before the comma and the one after the comma. 
                        name, house = line.rstrip().split(",")
                        print(f"{name} is in {house}")
                    
                    for student in sorted(students):
                        print(student)

                        '''
                        # rstrip removes the end of each line in our CSV file. 
                            # split tells the compiler where to find the end of each of our values in our CSV file. 
                        row = line.rstrip().split(",")

                        # row[0] is the first element in each line of our CSV file. row[1] is the second element in each line in our CSV file.
                        print(f"{row[0]} is in {row[1]}")
                        '''
                
                print("____________________________________")

            class Street:
                students = []

                with open("students.csv") as file:
                    for line in file:
                        name, home = line.rstrip().split(",")
                        students.append({"name": name, "home": home})

                for student in sorted(students, key=lambda student: student["name"]):
                    print(f"{student['name']} is in {student['home']}")
            '''
            class DictionaryWriter:

                import csv
                name = input("What's your name? ")
                home = input("Where's your home? ")

                # "a" = Appends to csv file
                with open("students.csv", 'a') as file:

                    # DictWriter, which takes two parameters: the file being written to and the fieldnames
                    writer = csv.DictWriter(file, fieldnames=["name", "home"])
                    writer.writerow({"name": name, "home": home})
            '''

        class BinaryFilesNPIL:
            # A binary file is simply a collection of ones and zeros. 
                # This type of file can store anything including, music and image data.
            # PIL that works well with image files.
            # Animated GIFs are a popular type of image file that has many image files within it that are played in sequence over and over again, 
                # creating a simplistic animation or video effect.
            ''

            class Gif:

                import glob
                from PIL import Image

                # Create the frames
                frames = []
                images = glob.glob("*.png")
                for i in images:
                    new_frame = Image.open(i)
                    frames.append(new_frame)

                # Save into a GIF file that loops forever
                frames[0].save('png_to_gif.gif', format='GIF', append_images=frames[1:], save_all=True, duration=300, loop=0)


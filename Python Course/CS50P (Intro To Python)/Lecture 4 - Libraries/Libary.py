class CS50PLecture4:

    class Libraries:

        # Generally, libraries are bits of code written by you or others can you can use in your program.
        # Python allows you to share functions or features with others as “modules”.    
        # If you copy and paste code from an old project, chances are you can create such a module or 
            # library that you could bring into your new project.
        
        class Random: 
            
            class Import:

                # random is a library that comes with Python that you could import into your own project.
                # import allows us to load a module into this file program.
                import random

                # Inside the random module, there is a built-in function called random.choice(seq). random
                    # Inside that module, there is the choice function. That function takes into it a seq or sequence that is a list.
                coin = random.choice(["heads", "tails"])
                print(coin)

            class From:

                # From allows us to be very specific about what we’d like to import. 
                    # Prior, our import line of code is bringing the entire contents of the functions of random

                # Now can import just the choice function of random. From that point forward, we no longer need to code random.choice. 
                    # We can now only code choice alone. choice is loaded explicitly into our program. 
                    # This saves system resources and potentially can make our code run faster!
                from random import choice

                coin = choice(["heads", "tails"])
                print(coin)

            class Randint:

                import random

                # random.randint(a, b). This function will generate a random number between a and b. 
                number = random.randint(1, 10)
                print(number)

            class Shuffle:

                import random

                # random.shuffle(x) where it will shuffle a list into a random order.
                cards = ["jack", "queen", "king"]

                # random.shuffle will shuffle the cards in place. Unlike other functions, it will not return a value. 
                    # Instead, it will take the cards list and shuffle them inside that list. 
                random.shuffle(cards)
                for card in cards:
                    print(card)
        
        class Statistics:

            # Python comes with a built-in statistics library. 
            import statistics
            
            # The mean function takes a list of values. This will print the average of these values
            print(statistics.mean([100,90]))
        
        class CommandLineArguments:
            
            # sys is a module that allows us to take arguments at the command line.
            # argv is a function within the sys module that allows us to learn about what the user typed in at the command line. 
                # Notice how you will see sys.argv utilized in the code below. 
            import sys

            if len(sys.argv) < 2:
                sys.exit("Too few arguments")
            elif len(sys.argv) > 2:
                sys.exit("Too many arguments")

            print("hello, my name is", sys.argv[1])
        
        class Packages:
            # There are numerous powerful third-party libraries that add functionality. 
                # We call these third-party libraries, implemented as a folder, “packages”.
            # PyPI is a repository or directory of all available third-party packages currently available.
            # Python has a package manager called pip that allows you to install packages quickly onto your system.

            # pip install cowsay allows us to instal package to terminal.
            # cowsay is a well-known package that allows a cow to talk to the user.
            '''
            import cowsay
            import sys

            if len(sys.argv) == 2:

                #  cow saying “hello”
                cowsay.cow("hello, " + sys.argv[1])
            '''

            '''
            import cowsay
            import sys

            if len(sys.argv) == 2:

                # t-rex is now saying “hello”.
                cowsay.trex("hello, " + sys.argv[1])
            '''

        class APIs:
            # APIs or “application program interfaces” allow you to connect to the code of others.
            # requests is a package that allows your program to behave as a web browser would.
            import json
            import requests
            import sys

            if len(sys.argv) != 2:
                sys.exit()

            response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

            o = response.json()
            for result in o["results"]:
                print(result["trackName"])
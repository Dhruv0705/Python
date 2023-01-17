'''
    Cows And Bulls Games

    Dhruv Patel 
'''

# imports the random module, which allows the program to generate random numbers.
import random

# sets a variable called DigitsInRandomNumber to 4, which is the number of digits in the randomly generated number for the game.
DigitsInRandomNumber = 4

# sets a variable called Cows to 0, which will be used to keep track of the number of cows the player has guessed.
Cows = 0

# sets the Bulls variable to 0, which will be used to keep track of the number of bulls the player has guessed.
Bulls = 0

# sets a variable called Attempts to 0, which will be used to keep track of the number of attempts the player has made.
Attempts = 0

print(f'''Welcome to Cows and Bulls Game! In this game, you will attempt to guess a randomly generated {DigitsInRandomNumber}-digit number with no repeating digits. 
\tIf you correctly guess a digit and it is in the correct place, you have a cow. 
\tIf you correctly guess a digit but it in in the wrong position, you have a bull. 
\tAfter each guess the computer will tell you hom many cows and bulls your guess had. Enjoy! 
Created by : Dhruv Patel''')

# sets a variable called DigitCounter to 0, which will be used to check if all the digits are unique in the random number.
DigitCounter = 0 

# starts a while loop that will continue to execute as long as the DigitCounter is not equal to the number of digits in the randomly generated number.
while (DigitCounter != DigitsInRandomNumber):

    # resets the DigitCounter to 0, then generates a random 4-digit number between 1000 and 9999 and converts it to a string, and assigns it to the variable RandomNumber.
    DigitCounter = 0
    RandomNumber = str(random.randint(1000, 9999))

    # creates an empty list called DigitsList, which will be used to store the digits of the random number.
    DigitsList = []

    # for loop iterates through each digit in the random number, and checks if it is already in the DigitsList. If it is, the loop breaks, if not, it adds the digit to the DigitsList and increments the DigitCounter by 1.
    for Digit in RandomNumber:
        if Digit in DigitsList:
            break
        else:
            DigitsList.append(Digit)
            DigitCounter += 1

# starts the main game loop, which will continue to execute as long as the player has not guessed all the digits correctly.
while Cows != DigitsInRandomNumber:

    # prompts the player to input their guess for the number, and assigns it to the variable UserInput.
    UserInput = input(f"\nGuess a {DigitsInRandomNumber}-digit number: ")

    # checks if the user input is not a digit, and if it is not, it prints an error message and continues to the next iteration of the loop.
    if UserInput.isdigit()==False:
        print("\tInvalid Guess. Cannot enter a non-integer character.")
        continue
    
    # if the user input is not the same length as the number of digits in the randomly generated number
    elif (len(UserInput) != DigitsInRandomNumber):
        print(f"\tInvalid Guess. Number must contain precisely {DigitsInRandomNumber} digits.")
        continue
    
    # starts the else block of the previous if-else statement. It will only execute if the user input is a digit and is the same length as the number of digits in the randomly generated number.
    else:

        # sets a variable called RepeatedDigits to False, which will be used to check if the user input has any repeating digits.
        RepeatedDigits = False

        # creates an empty list called UserInputList, which will be used to store the digits of the user input.
        UserInputList = []

        # for loop iterates through each digit in the user input, and checks if it is already in the UserInputList. If it is, it sets the RepeatedDigits variable to True, if not, it adds the digit to the UserInputList.
        for Digit in UserInput:
            if Digit in UserInputList:
                RepeatedDigits = True
            else:
                UserInputList.append(Digit)

        # checks if the user input has any repeating digits, and if it does, it prints an error message and continues to the next iteration of the loop.
        if RepeatedDigits == True:
            print("\tInvalid Guess. Number cannot repeat digits. ")
            continue

        # increments the Attempts variable by 1, keeping track of the number of attempts the player has made.
        Attempts += 1

        # for loop iterates through each digit in both the randomly generated number and the user input, and if they are the same at the same position, it increments the Cows variable by 1.
        for i in range(0, 4):
            if RandomNumber[i] == UserInput[i]:
                Cows += 1

        # nested for loop iterates through each digit in the user input, and for each digit, it checks if it is in the DigitsList. If it is, it increments the Bulls variable by 1.
        for i in range(0, 4):
            for Digit in DigitsList:
                if Digit == UserInput[i]:
                    Bulls += 1

        # subtracts the number of cows from the number of bulls, so that bulls only counts the number of correct digits in the wrong position
        Bulls -= Cows

        # checks if the player has guessed all the digits correctly and if they have, it continues to the next iteration of the loop without printing the cow and bull count.
        if Cows == 4:
            continue    
        
        # prints the number of cows and bulls the player has guessed.
        print(f"\tCow(s): {Cows} \n\tBull(s): {Bulls}")

# prints a message to the console when the player has correctly
print(f"\tCorrect! The number was {RandomNumber}! You got it in {Attempts} tries.")



            
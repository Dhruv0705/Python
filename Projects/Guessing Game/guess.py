import random

def user_guess(x):
    random_number = random.randint(1,x)
    user_guess = 0
    while user_guess != random_number:
        user_guess = int(input(f"Guess a Number between 1 and {x}: "+ " "))
        if user_guess < random_number:
            print("Sorry, guess again. Your guess was low.")
        elif user_guess > random_number:
            print("Sorry, guess again. Your guess was high")
    print("Congrats, the number" , random_number, "was Correct, Congrats.")

user_guess(10)

def computer_guess(x):
    low = 1 
    high = x 
    feedback = " "
    while feedback != "c":
        user_guess = random.randint(low, high)
        feedback = input('Is', user_guess, "too high (H), too low (L), or correct (C)??").lower
        if feedback == "h":
            high = user_guess - 1
        if feedback == "l":
            low = user_guess + 1
        
    print("The computer guessed your number,", user_guess, "correctly!")
    
computer_guess(10)
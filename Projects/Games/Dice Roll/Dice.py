import random
import time

# Initial amount of money user has
UserMoney = 1000

def DiceRoll(NumberOFRolls=1):
    """
    This function simulates rolling a dice.
    The number of rolls can be passed as an argument
    (default is 1 roll).
    """
    
    print("Please wait as the dealer rolls the dice")
    time.sleep(2)
    DiceSum = 0

    # Roll the dice for the number of times specified
    for i in range(NumberOFRolls):
        Roll = random.randint(1,6)
        DiceSum += Roll
        print(F"\tOn roll number {i+1}, we got {Roll}.")
        time.sleep(1)
    
    return DiceSum

while True:
    UserBet = int(input("How much do you want to bet? "))

    # Check if user has enough money
    if UserBet > UserMoney:
        print("You do not have enough money.")
        continue
    else:
        UserGuess = input("\n[C/H]:")
        
        Sum = DiceRoll(2)

        # Check if the sum of the rolls is even or odd
        if(Sum % 2 == 0):
            if(UserGuess == "C" or UserGuess == "c"):
                print("You Win!")
                UserMoney += UserBet

            else:
                print("You Lose!")
                UserMoney -= UserBet
            
        else:
            if(UserMoney == "H" or UserGuess == "h"):
                print("You Win!")
                UserMoney += UserBet
            
            else:
                print("You Lose!")
                UserMoney -= UserBet
    print(f"You have {UserMoney} dollars.")

    PlayAgain = input("\nWould you like to play again>? [Y/N] ")
    if PlayAgain == "N" or PlayAgain == 'n':
        print("Thank You for playing")
        break

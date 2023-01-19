import random

# Initialize scores for user and computer
UserScore = 0
ComputerScore = 0
TotalPoints = 0

def ShowRules():
    """
    This function prints the rules of the game.
    """
    print("\n*** Rock-Paper-Scissors ***\n")

    print("\nEach player chooses either Rock, Paper, or Scissors."
          "\nThe winner is determined by the following rules:"
          "\n   Scissors cuts Paper   ->  Scissors wins"
          "\n   Paper covers Rock     ->  Paper wins"
          "\n   Rock smashes Scissors ->  Rock wins\n")
ShowRules()

def ComputerMoves():
    """
    This function returns a random move chosen by the computer
    """
    Moves = ["Rock", "Paper", "Scissors"]
    ChosenMove = random.choice(Moves)
    return ChosenMove

# Get the user's name
UserName = input("What is your name? ")

while True:
    # Get user's choice
    UserChoice = input("Rock, Paper, or Scissors? ").title()
    # Get computer's choice
    ComputerChoice = ComputerMoves().title()
    print(f"\nUser Guessed: {UserChoice}")
    print(f"Computer Guessed: {ComputerChoice}")
    
    # Check for a tie
    if UserChoice == ComputerChoice:
        print("Its a Tie!")

    elif UserChoice == "Rock":
        if ComputerChoice == "Scissors":
            print(f"{UserName} Won!")
            UserScore += 1

        else:
            print("The Computer Won!")
            ComputerScore += 1

    elif UserChoice == "Scissors":
        if ComputerChoice == "Paper":
            print(f"{UserName} Won!")
            UserScore += 1
        else:
            print("The Computer Won!")
            ComputerScore += 1

    elif UserChoice == "Paper":
        if ComputerChoice == "Rock":
            print(f"{UserName} Won!")
            UserScore += 1
        else:
            print("The Computer Won!")
            ComputerScore += 1

    # Print the current score
    print(f"Score: {UserName}: {UserScore} Computer: {ComputerScore}\n")

    # Check if either the user or computer has reached the total points
    TotalPoints = int(10)
    if UserScore == TotalPoints or ComputerScore == TotalPoints:
        if UserScore > ComputerScore:
            print(f"{UserName} WINS!")
        else:
            print("The Computer Wins.")

        # Ask the user if they want to play again
        PlayAgain = (input("Would you like to play again? [y/n]"))
        if PlayAgain == 'y':
            # Reset the scores for another game
            UserScore = 0
            ComputerScore = 0
        else:
            # Exit the game
            break

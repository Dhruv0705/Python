class LeftORRightGame:
    class Game:
        print("Welcome to Choices The Game")
        Name = str(input("What is your name? "))
        Age = int(input("What is your age? "))
        Health = 10
        print(f"Hello {Name} your are {Age} years old.")

        if Age >= 18:
            print("You are old enough to play!")

            wants_to_play = input("Do you want to play? ").lower()
            if wants_to_play == "yes":
                print("You are staring with", Health, "health")
                print("Let's play!")

                left_or_right = input("First choice... Left or Right (left/right)? ")
                if left_or_right == "left":
                    ans = input("Nice, you follow the path and reach a lake... Do you swim across or go around (across/around)? ")

                    if ans == "around":
                        print("You went around and reached the other side of the lake.")
                    elif ans == "across":
                        print("You managed to get across, but were bit by a fish and lost 5 health.")
                        Health -= 5

                    ans = input("You notice a house and a river. Which do you go to (river/house)? ")
                    if ans == "house":
                        print("You go to the house and are greeted by the owner... He doesn't like you and you lose 5 health")
                        Health -= 5

                        if Health <= 0:
                            print("You now have 0 health and you lost the game...")
                        else:
                            print("You have survived... You win!")

                    else:
                        print("You fell in the river and lost...")


                else:
                    print("You fell down and lost...")

            else:
                print("Cya...")
        else:
            print("You are not old enough to play...")

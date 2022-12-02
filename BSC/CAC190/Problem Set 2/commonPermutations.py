#Dhruv Patel
#CAC 190
#9/16/2022
#Problem 4 Strings

# Compares two strings to output the same letter comparing the two.
# Creates a list to store all input the users enters. 
common_Permutation_List = []

# Loops over input until no more entries exist
def Permutation ():
    first_Permutation = input("Please enter the first phrase to compare: ")

    # Keeps the loop going until user presses enter.
    while first_Permutation != "":
        
        # Ask the user to enter next phrase to comapre.
        second_Permutation = input("Please enter the second phrase to compare: ")
        
        # Append the two permutation input.
        common_Permutation_List.append([first_Permutation,second_Permutation])
        
        # Print Spaces
        print("____________________________________________________________")

        # Ask the user to either keep asking the permutations or exit the loop.
        first_Permutation = input("Please enter the next phrase to compare or press enter: ")
        

    # For loop to loop through collected pairs to find matching letters between the append above.
    for collected_Pair in common_Permutation_List:

        # Places common matches in list.
        common_Matches = []

        # Sorts the first word and puts them in order
        pair = sorted(collected_Pair[0])

        # Loops through letter 
        for letter in pair:

            # If loops that outputs the letter from the first word is in the second but not in the matches adds the letter. 
            if letter in collected_Pair[1] and letter not in common_Matches:
                common_Matches.append(letter)

        #print matching letters per multiple of different input entered
        print (*common_Matches)
Permutation()
       
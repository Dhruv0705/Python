# Dhruv Patel
# 10/31/2022
# CAC190
# Problem 11 Tower of Hanoi

# Sets the totalmoves variable to 0
totalMoves = 0

# Function to fill all parameters set gathering the disk input in the main function
def TowerOFHanoi(source, auxiliary, destination, disks):

    totalMoves = 0

    # If loop if disk input is 1, will increment totalmoves to 1
    if disks == 1:
        totalMoves += 1
    
    # Else the function will keep 
    else:

        # Calls the function again moving all of the disk of the bottom one to the auxiliary or middle disk
        TowerOFHanoi(source, auxiliary, destination, disks-1)

        # Moves the bottom disk to the end as implied incremented the total moves counter to +1 each loop 
        totalMoves += 1

        # Move all of the disks back on top of the largest one until all disk are moved from the end position to destination. 
        TowerOFHanoi(source, auxiliary, destination, disks-1)

# main function to have the user input number of disk resulting in the amount of total moves made
def main():

    totalMoves = 0

    # Ask user the amount of disk for input
    disks = input("Enter the amount of disks: ")

    # Empty array
    testCases = []

    # While the disk is not a empty string
    while disks != '':

        # Adds the testcase to the array and loops through the next input until the user enter a empty string
        testCases.append(int(disks))
        disks = input("Enter another amount of disk or press enter to exit: ")

    # For each loop to gather all of the testcase and calculate the number of moves
    for case in testCases:
        TowerOFHanoi('A','B','C',case)
        print(totalMoves)
        totalMoves = 0

# Return the main function 
main()
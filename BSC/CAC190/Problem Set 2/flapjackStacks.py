#Dhruv Patel
#CAC 190
#9/16/2022
#Problem 6 FlapJack
#Note: some variable was help 

# Function to find the position within the index. 
def findMaximum(flapJack_Pancakes):
    
    # Returns the largest value of the list or variable of pancakes. 
    return flapJack_Pancakes.index(max(flapJack_Pancakes))

# Function to find stack position
def fliped_Pancakes(flapJack_stack, position):
    
    # Empty list to store the values. 
    newStack = []

    # Loop to reverse from the largest pancake to the beginning of the stack
    for i in range(position,-1,-1):
        newStack.append(flapJack_stack[i])

    # Loop to for the bottom of the stack.
    for i in range(position+1,len(flapJack_stack)):
        newStack.append(flapJack_stack[i])
    return newStack

# Function for the flipAll command.
def flipAll(flapJack_stack,size):

    # Creats a new empty list for new stack.
    newStack = []

    # Loop to reverse the stack from the designated position to the beginning
    for i in range(size-1, -1, -1):
        newStack.append(flapJack_stack[i])
    return newStack

# Main function
def main():

    # Ask the user to  input stack filling the list and empty list below. 
    flapJack_stack = input()
    pancake_stacks = []
    flapJack_fliped = []
    
    # Loop to continue the flapjack program until user enters nothing or enter.
    while flapJack_stack != '':
        pancake_stacks.append(flapJack_stack)

        # ask user to input stack
        flapJack_stack = input()
        
    # loop to store the value in the empty list. 
    for flapJack_stack in pancake_stacks:
        listStack = []

        # Loop to convert the values to integers within the list
        for val in flapJack_stack:
            listStack.append(int(val))

        # List to store flipStack
        flipStack = []

        # length within the stacklist. 
        size = len(listStack)

        # Empty Variable. 
        flipCount = 0

        #starting at the bottom of the stack...
        while size > 0:

            # Find the position of the largest within stack.
            largest = findMaximum(listStack[:size])
           
            # Loop to find the largest within stack and size variable return value. 
            if largest != size-1:

                # Flips the stack so the largest goes on the top of the listed stack.
                listStack= fliped_Pancakes(listStack,largest)

                # Flips the stack as the value return to the bottom. 
                listStack = flipAll(listStack, size)

                # Flip Counter.
                flipCount += 1
                flipStack.append(flipCount) 

            # -size finds the new largest one in variable.
            size -= 1 

        # Adds the 0 to stack.
        flipStack.append(0)
        flapJack_fliped.append(flipStack)

    # Print out the original stack plus the flips within the loop and index. 
    for i in range(len(pancake_stacks)):           
        print(*pancake_stacks[i])
        print(*flapJack_fliped[i])

# Return the main funciton 
main()
# Dhruv Patel
# CAC 190
# 11/27/2022
# Problem 16 Minimum

# Function to Add within list
def Add(AList):

    # Counter
    Sum = 0

    # For number in list
    for Number in AList:

        # Add each number and set it to sum value
        Sum += Number
    
    # Return Sum
    return Sum

# Function To Subtract within list
def Subtract(AList):

    # variable value begin at length 0 
    Diff = AList[0]

    # For loop to loop through the range starting at second position ending in the last position
    for i in range(1,len(AList)):

        # loops through each array within list subtracting each value 
        Diff -= AList[i]

    # Return value
    return Diff

# Function to find highest value
def Highest(AList):

    # Max Value counter set to 0
    Max = 0
    
    # For loop to loop through each Number in List
    for Number in AList:

        # If number greater then Max Continue:
        if Number > Max:

            # Then Set max to number
            Max = Number
            
    # Return Max value
    return Max

# Function to find the smallest variable within list
def Smallest(AList):

    # Set Min Value to first number within array
    Min = AList[0]
    
    # For Number in list:
    for Number in AList:

        # If Number is less then Min value:
        if Number < Min:

            # Set Min to Number
            Min = Number
    
    # Return Min
    return Min

if __name__ == '__main__':
    myList = [1,2,3,4,5]
    print(Add(myList))  
    print(Subtract(myList))
    print(Highest(myList))
    print(Smallest(myList))
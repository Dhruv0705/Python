# Dhruv Patel
# 10/6/2022
# CAC190
# Problem 9
# Arithmetic and Algebra

# Method to find the exponent of a number
def findExponent(givenNumber):

    # Exponent start at the value of 1
    exponent = 1

    # sets power to 2 of the power of exponent value
    setPower = 2**exponent

    #NOTE: This while loop was helped loop explination: 
    # while the length of power string is less then the length of the given number or keep running if the number is not equal to the substring of power the while loop will rerun and return the exponent of the user input. 
    # This loop will determine the smallest exponent in why input of 2 is equal to 8 as 2**8 is the smalle exponenet to begin with a 2 = 256. 
    while len(str(setPower)) <= len(givenNumber) or givenNumber != str(setPower)[0:len(str(givenNumber))]:
    #for n in range (power):
        
        #increase the exponent by 1 to loop through the while loop to find the smallest exponent
        exponent += 1

        #compute the new power of the smallest exponenet
        setPower = 2**exponent

    #return the found exponent
    return exponent 

# Method for storing the values in a list and printing integers 
def archaeologistDilemma():

    # Empty List to store the values
    archaeologistList = []

    # User will input a integer
    integerValue = input("Please enter an integer ")

    # While input value is not blank:
    while integerValue != '':
        
        # Appends the value to the end of the list 
        archaeologistList.append(integerValue)

        # Reruns loop until value is equal to '' (blank)
        integerValue = input("Please enter next integer or press enter to exit ")

    # For the values in the gathered list print the smallest positive integer exponent of each inputed value
    for smallestPositiveInteger in archaeologistList:
        print(findExponent(smallestPositiveInteger))

# Prints Method    
archaeologistDilemma()

from math import log10, log
 
# Function to return smallest
# power of 2 with N digits
def smallestNum(n):
 
    res = 1
 
    # Iterate through all
    # powers of 2
    i = 2
    while (True):
        length = int(log10(i) + 1)
         
        if (length == n):
            return int(log(i) // log(2))
             
        i *= 2
 
# Driver Code
n = 4
n = 2
 
print(smallestNum(n))
 
# This code is contributed by SHIVAMSINGH67
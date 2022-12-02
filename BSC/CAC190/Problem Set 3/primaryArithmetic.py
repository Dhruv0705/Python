# Dhruv Patel
# 10/6/2022
# CAC190
# Problem 7
# Primary Arithmetic

# Function to determine the number of carries from adding two numbers
# Carry operation was helped as explained
def carriesCount(num1, num2):

    # Sets the value of carry and count to nothing or 0
    carry = 0
    count = 0

    # Find the length of num1 and num2
    lengthOfNum1 = len(num1)
    lengthofNum2 = len(num2)

    # While lengthofnum1 and 2 is not equal to 0 then:
    while (lengthOfNum1 !=0 or lengthofNum2 !=0):

        # Sets the value of the counter to 0
        num1carryCount = 0
        num2carryCount = 0

        # If the length of num1 is greather then 0:
        if (lengthOfNum1 > 0):

        # Will loop thorugh until the lengthofnum1 and lengthofnum2 is less then 0 this method will start in order 2 adding the values of the given input in order to find the remainer as the if statment will reloop until there is no remianers.
            num1carryCount = int(num1[lengthOfNum1 - 1]) + int('0')
            lengthOfNum1 -= 1
         
        if (lengthofNum2 > 0):
            num2carryCount = int(num2[lengthofNum2 - 1]) + int('0')
            lengthofNum2 -= 1
 
        # Add operation to total sum 
        totalSum = num1carryCount + num2carryCount + carry
 
        # If totalsum > 10
        if (totalSum >= 10):

            # Set carry to 1
            carry = 1

            # Then increment count by 1
            count += 1
 
        # Else, set carry to 0
        else:
            carry = 0

    # Return function
    return count

# Functtion to print the amount of carriesCount withint the inputed values. 
def PrimaryArithmetic():

    # empty list to store the values
    arithmeticList = []
    arithmeticNumbers = input("Enter 3 number followed by a space with 3 additional number to calculate number of carry operation: ")

    # While user does not input 0 0 keep looping or exit program when user inputs 0 0:
    while arithmeticNumbers != '0 0':

        # appends the value of number to the end of the list
        arithmeticList.append(arithmeticNumbers)
        arithmeticNumbers = input("Plese enter next operation to calculate or enter 0 0 to exit: ")
    # For the inputed digits in the list:
    for digits in arithmeticList:

        # Values will be split
        values = digits.split()

        # Calculate using the carriesCount method to add the values of order 0 and 1 to find the carryOperations
        # Loop will end with carry operations have been found outputing the if statment determined by the amount of carries. 
        carryOperations = carriesCount(values[0], values[1])

        # If statment to print the number of carry opeartions.
        if carryOperations == 0:
            print( '0 Carry Operation.')
        else:
            print(carryOperations, 'Carry Operations.')

# Prints primaryArithmetic function
PrimaryArithmetic()
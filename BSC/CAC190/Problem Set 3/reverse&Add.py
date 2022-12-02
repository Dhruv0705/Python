# Dhruv Patel
# 10/6/2022
# CAC190
# Problem 8 Reverse and Add

# method to determine if the number is a palindrome
def DeterninePalindrome(number):

    # return number if number is equal to the reversed order then is palindrone else it is not. 
    return number == number[::-1]

# Method to reverse digits of num and add the two together
def ReverseAndAdd(number):

    # reverse the digit of the number within length ::-1 will reverse the order - 123 = 321
    reversedNumber = number[len(number)::-1]

    # Adding the original number and the reversed number
    addedNumber = int(number) + int(reversedNumber)
    
    # Returns the value of sum ending method
    return str(addedNumber)

# Method to output the resulting palindrome adding and revering the string. 
def main():

    # Ask user the enter amount of test cases
    testCases = int(input("Please enter number of test cases "))

    # Stores testcases within a empty list
    testCasesList = []

    # For the amount of test cases within the range of test cases add them to the end of the testcaseList taken by from the user input 
    for testCases in range(testCases):
        testCasesList.append(input())
    
    # For the amount of testcases there are in the list:
    for testCases in testCasesList:

        # the addition value is equal to 0 to be later incremented by one in order to find the minimum palidrone 
        minimumIterationsValue = 0

        # While the testcase addition is not a palindrome keep loop until it is detected as a palindrome: 
        while not DeterninePalindrome(testCases):

            # method to keep reversing and adding testcases 
            testCases = ReverseAndAdd(testCases)

            # incremented value by one until 
            minimumIterationsValue += 1

        # print the minimum numbner of iterations to find the palidrone and the list within testcases stored values to output the added and reversed string
        print(minimumIterationsValue, testCases)

# prints main method
main()
        
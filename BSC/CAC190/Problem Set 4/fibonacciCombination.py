# Dhruv Patel
# 10/31/2022
# CAC190
# Problem 11 Fibonacci Combination

# Ask the user to input testcases
testcase = input("Please Enter Fibonacci Test Case: ")

# Empty list
testcases = []

# While loop to loop through the testcases that enters testcases not equal to 0 0
while testcase != '0 0':

    # Adds to the list and get the next input from user. 
    # Will rerun until user enters 0 0.
    testcases.append(testcase)
    testcase = input("Please Enter Next Fibonacci Test Case or enter 0 0 to exit: ")

# For loop to iterate through each testcases
for case in testcases:

    # Prints the inputed value 
    #print(case)

    values = case.split()

    # Set value for the very first value within the array
    a = int(values[0])

    # Set value for the second value within the array w
    b = int(values[1])
    
    #start counter at 0
    counter = 0
    
    # Begins computing fibonacci sequence setting each variable to 1 
    fibonacciNumber1 = 1
    fibonacciNumber2 = 1
    fibonacciCombination = fibonacciNumber1 + fibonacciNumber2

    # While loop will continue to compute fibonacci numbers until we each the stop value
    while fibonacciCombination < b:

        # If the fibonacciCombination is greater than or equal to the start
        if fibonacciCombination >= a:

            # Increase the counter each loop adding one
            counter += 1

        # If while loop is true will calculate the next fibonacci combinatino within the two numbers.
        # Setting the value of fibonacciNumber 1 to equal fibonacciNumber2 
        fibonacciNumber1 = fibonacciNumber2

        # Set the fibonacciNumber2 new value to the combonation
        fibonacciNumber2 = fibonacciCombination

        # Set the cobination new value to add the two fibonacci numbers together.
        fibonacciCombination = fibonacciNumber1 + fibonacciNumber2

    # Prints the amount of loops accored  
    print(counter)
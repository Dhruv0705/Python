# Dhruv Patel
# 11/14/2022
# CAC190
# Problem 13
# Combinatorics


# Function to find the min amount of steps
def Steps(StartStep, EndStep):
    
    # Counter
    StepSize = 1
    StepCount = 0

    # Find the midpoint
    Midpoint = (EndStep-StartStep)//2 + StartStep

    # Begins Counter
    StartStep += StepSize
    StepCount += 1

    # Take the last step
    EndStep -= StepSize
    StepCount += 1
            
    # While loop continue as long as StartStep is not equal to end step
    while StartStep != EndStep:
        Distance = EndStep - StartStep

        # If the distance is larger than the current step size and haven't reached the midpoint loop through
        if Distance > StepSize and StartStep < Midpoint:

            # Increase the step size and take the stepSize value
            StepSize += 1
            StartStep += StepSize
            StepCount += 1

        # Else If StartStep is greater then or equal to the midpoint, start decreasing the StepSize
        elif StartStep >= Midpoint and StepSize > 1:
                
            # Decrease step size and take the stepSize value
            StepSize -= 1
            StartStep += StepSize
            StepCount += 1
    
        # Else the StepSize is 1 but haven't reached the end.
        else:
            StartStep += StepSize
            StepCount += 1
    return StepCount
    
# Main method to ask user for testcases and calculation for smallest amount of steps
def main():

    # Ask user number of testcases
    testcases = int(input("Please enter a number of testcases: "))
        
    # Empty list
    cases = []

    # For loop to ask the user to enter a number to illiterate through the testcases
    for i in range(testcases):

        # Append each input into case
        cases.append(input("Enter value: "))
        
    # Iterate through testcases to solve each cases
    for case in cases:

        # Split to get the start and stop
        values = case.split()

        # StartStep value is the first within the array
        StartStep = int(values[0])

        # EndStep value is second within the array
        EndStep = int(values[1])
        print(Steps(StartStep,EndStep))
            
main()

        
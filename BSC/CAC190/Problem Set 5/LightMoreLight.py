# Dhruv Patel
# 11/14/2022
# CAC190
# Problem 14
# Number Theory


# Class Attribute


# Method ToggleLight
def ToggleLights(LightList):

        # Empty counter Variable
        WalkCounter = 1

        # While the walkcounter is not less then the length of the LightList continue loop
        while WalkCounter <= len(LightList):

            # For index of i in range of lightList
            for i in range(len(LightList)):

                # If walkcount is divisiabel by i+1 and is =0 then
                if (i+1) % WalkCounter == 0:

                    # Lightlist index is not within the list 
                    LightList[i] = not LightList[i]
                    
            # Adds to counter
            WalkCounter += 1
         # Returning the LightList
        return LightList
    
# Main Method
def main():
        
        # Ask user to input a bulb
        lights = int(input("Enter Lightbulb: "))

        # Empty list for amount of testcases
        testcases = []

        # While loop continues as long as the input is not 0
        while lights != 0:
            
            # Adds light number to the end of the list
            testcases.append(lights)

            # Reloops to ask the user to reenter another number or press 0 to exit loop
            lights = int(input("Enter Next LightBuild Or enter 0: "))
        
        # Loops through the amount of testcases
        for case in testcases:
            
            # Creates a empty list
            LightList = []

            # For loop to illiterate through the range of the cases
            for i in range(case):

                # Appended to the LightList
                LightList.append(False)

            # resets the variable to the class attribute of ToggleLight 
            LightList = ToggleLights(LightList)

            # Prints if the light number is on or off
            if LightList[-1]:
                print(f'Yes Lightbulb: {case} Is on')
            else:
                print(f'No Lightbulb: {case} Is Off')
main()

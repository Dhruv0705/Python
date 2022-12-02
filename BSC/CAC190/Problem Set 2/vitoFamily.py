#Dhruv Patel
#CAC 190
#9/16/2022
#Problem 5 Sorting

# Ask the user to enter a number they want divisibly by in interger type. 
vito_family = int(input("Enter number to calculate the absolute difference: "))

# Loop throught function 
while (vito_family):

    # Splits the input as the user enter the next number and prints. 
    vito = input("Enter next number: ").split(" ")
    print(vito)

    # Places variable in the first postion. 
    vito_room = vito[0]

    # Remove duplicate to places the integer.  
    vito.remove(vito_room)
    vito_room = int(vito_room)

    # For loop for range in the variable starting from the first position. 
    for i in range(0, vito_room):

        # 
        vito[i] = int(vito[i])

    # Sorts the input in the range
    vito.sort()

    # Finds the absolute difference between the middle distance amoung vito variable. 
    mid = vito[vito_room // 2]
    
    # empty variable
    vito_relatives = 0

    # For loop to calculate the absolute difference. 
    for i in vito:

        vito_relatives += abs(i - mid)

    # Prints the divisible number.
    print(vito_relatives)

    # 
    vito_family -= 1
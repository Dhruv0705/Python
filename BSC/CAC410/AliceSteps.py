# Get the number of Alice's steps from user input
alice_steps = int(input())

# Initialize row, column, to zero
row, column = 0, 0

# Determine the square root of Alice's steps
current_step = 0

# Iterate until the square of current_step is greater than Alice's steps
while current_step ** 2 <= alice_steps:

    # Increment current_step
    current_step += 1

# Decrement current_step because it was incremented one too many times
current_step -= 1

# Check if the square of current_step equals Alice's steps
if current_step ** 2 == alice_steps:

    # If the square of current_step is even
    if current_step % 2 == 0:

        # Set the column to current_step and the row to 1
        column = current_step
        row = 1
    # If the square of current_step is odd
    else:
        # Set the column to 1 and the row to current_step
        column = 1
        row = current_step
# If the square of current_step does not equal Alice's steps
else:
    # If the square of current_step is even
    if current_step % 2 == 0:
        # Set the column to current_step plus 1 and the row to 1
        column = current_step + 1
        row = 1
        # Set p to the square of current_step plus 1
        p = current_step ** 2 + 1

        # for i in the number of steps 
        for i in range(current_step):
            # If p equals Alice's steps, break out of the loop
            if p == alice_steps:
                break
            # Increment row and p
            row += 1
            p += 1
        # Iterate a times
        for i in range(current_step):
            # If p equals Alice's steps, break out of the loop
            if p == alice_steps:
                break
            # Decrement column and p
            column -= 1
            p += 1
    # If the square of current_step is odd
    else:
        # Set the column to 1 and the row to current_step plus 1
        column = 1
        row = current_step + 1
        # Set p to the square of current_step plus 1
        p = current_step ** 2 + 1
        # Iterate a times
        for i in range(current_step):
            # If p equals Alice's steps, break out of the loop
            if p == alice_steps:
                break

            # Increment column and p
            column += 1
            p += 1
        # Iterate a times
        for i in range(current_step):
            
            # If p equals Alice's steps, break out of the loop
            if p == alice_steps:
                break
            # Decrement row and p
            row -= 1
            p += 1

# Print the column and row
print(column, row)

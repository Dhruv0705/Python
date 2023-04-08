# 1

def search_words(grid, words):
    rows = len(grid) # get number of rows in the grid
    cols = len(grid[0]) # get number of columns in the grid
    output = [] # create an empty list to hold the output

    for word in words: # loop through each word in the list of words to search for
        found = False # initialize a flag to indicate whether the word has been found

        # search rows forward
        for i in range(rows): # loop through each row in the grid
            row = "".join(grid[i]) # concatenate the characters in the row into a string
            if word in row: # check if the word is in the row
                output.append("Yes") # if it is, add "Yes" to the output list
                found = True # set the flag to True
                break # exit the loop

        # search rows backward
        if not found: # if the word has not been found yet
            for i in range(rows): # loop through each row in the grid
                row = "".join(grid[i])[::-1] # concatenate the characters in the row in reverse order
                if word in row: # check if the word is in the reversed row
                    output.append("Yes") # if it is, add "Yes" to the output list
                    found = True # set the flag to True
                    break # exit the loop

        # search columns forward
        if not found: # if the word has not been found yet
            for j in range(cols): # loop through each column in the grid
                col = "".join([grid[i][j] for i in range(rows)]) # concatenate the characters in the column into a string
                if word in col: # check if the word is in the column
                    output.append("Yes") # if it is, add "Yes" to the output list
                    found = True # set the flag to True
                    break # exit the loop

        # search columns backward
        if not found: # if the word has not been found yet
            for j in range(cols): # loop through each column in the grid
                col = "".join([grid[i][j] for i in range(rows)])[::-1] # concatenate the characters in the column in reverse order
                if word in col: # check if the word is in the reversed column
                    output.append("Yes") # if it is, add "Yes" to the output list
                    found = True # set the flag to True
                    break # exit the loop

        # word not found
        if not found: # if the word has not been found in any row or column
            output.append("No") # add "No" to the output list

    return " ".join(output) # join the output list into a string separated by spaces and return it

# 2 

def identify_non_twin(N, identities):
    counts = {}
    for identity in identities:
        if identity not in counts:
            counts[identity] = 1
        else:
            counts[identity] += 1
    for identity, count in counts.items():
        if count % 2 != 0:
            return identity
    return -1


# 3 

def find_largest_in_row_smallest_in_column(matrix):
    # Initialize two empty sets to store the largest element in each row and the smallest element in each column
    max_set = set()
    min_set = set()
    
    # Loop through each row in the matrix
    for row in matrix:
        # Find the maximum element in the row and add it to the max_set
        max_set.add(max(row))
    
    # Loop through each column in the matrix
    for j in range(len(matrix[0])):
        # Find the minimum element in the column using a generator expression and add it to the min_set
        min_set.add(min(matrix[i][j] for i in range(len(matrix))))
    
    # Find the intersection of max_set and min_set, and return the largest element in the intersection set as the answer
    intersection_set = max_set.intersection(min_set)
    return max(intersection_set) if intersection_set else None

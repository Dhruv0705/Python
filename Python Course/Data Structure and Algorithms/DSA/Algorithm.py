class DSA:
    class Lesson1:
        class BinarySearch:

            '''
            # QUESTION 1: 
                Alice has some cards with number written on them.
                She arranges the cards in decreasing order
                and lays them out face down in a sequence on a table.
                She challenges Bob to pick out the card
                containing a given number by turning over as few cards as possible.
                Write a function to help Bob locate the card. 
            '''
            '''
            SOLUTION:
                Need to write a program to find the position of a given number
                in a list of numbers arranged in decreasing order.
                Also need to minimize the number of times we access elements from the list. 
            '''
            '''
            EDGE CASES: (Possible)
                The Number Query occurs somewhere in the middle of the list Cards
                Query is the first element in Cards
                Query is the last element in Cards
                The list Cards contains just one element which is Query
                The list Cards does not contain number Query
                The list Cards is empty
                The list Cards contains repeating numbers
                The number Query  occurs at more than one position in Card
            '''
            '''
            INPUT:
                Cards: A list of numbers sorted in decreasing order (EG: [13, 11, 10, 7, 4, 3, 1])
                Query: A number, whose position in the array is to be determined (EG: 7)
            '''
            '''
            OUTPUT:
                Position: The position of Query in the list Cards (EG: 3 (counting from 0))
            '''
            # Method:
            
            def LocateCard(Card, Query):
                
                # Create a variable position as counter
                Position = 0 

                # While loop for repetition
                while True:

                    # Check if element at the current position match the query
                    if Card[Position] == Query:

                        # If true then return and exit
                        return Position
                    
                    # Increment Position
                    Position += 1

                    # Check if we have reached the end of the array
                    if Position == len(Card):
                        
                        # if number not found, return -1
                        return -1




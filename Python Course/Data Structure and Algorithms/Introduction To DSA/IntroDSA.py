class Algorithms:

    '''
    What is a Algorithms?
        A set of steps or instructions fro completing a task.
            Recipe, To-Do, GPA
        A set of steps a program takes to finish a task.
    
    What makes an Algorithm an algorithm:
        Clearly defined:  problem statement, input and output.
        The steps in the algorithm needs to be in a very specific order.
        The steps also needs to be distinct.
        The algorithm should produce a result.
        The algorithm should complete in a finite amount of time.
    
    Complexity (Measuring Efficiency):
        BigO:
            Theoretical definition of the complexity of an algorithm as a function of the size.
            How the algorithm preforms in the worst case scenario
            Notation used to describe complexity through a single variable: O(n)
            O - Order of magnitude of complexity
        Time Complexity:
            Measure of how long it take the algorithm to run
            Running Time:
                Defines time complexity
            Best Case scenario:
                The least amount of times the program can finished
            Average case scenario:
                Average case with multiple cases
            Worst case scenario:
                The most amount of time a program can finished
                The algorithm will never perform worse than we expect

        Space Complexity:
            Measures the amount of memory taken up on the computer
    '''

    
    class SearchAlgorithm:

        class LinearSearch:
            '''
            Linear Search:
                Algorithm:
                    1. Start at beginning or range of values
                    2. Move sequentially to the next value in the list and repeat step 2
                    3. Compare current value to target
                    4. Reach end of list
                BigO: O(n)
            '''
            print("______LINEAR SEARCH:______")

            # Function that takes two arguments:
                # The list we are searching through
                # The target value we are looking for
            def LinearSearchAlgo(List, Target):
                '''
                # Method: Returns the index position of the target if found
                    # else return None
                '''
                # illiterate from starting at position 0 to the end of the list
                for i in range(0, len(List)):
                    
                    # If index within list is equal to target : return i value
                    if List[i] == Target:
                        return i

                # else if index is not within the target then return None
                return None 

            # Function to verify index if not None:
            def Verify(index):
                if index is not None:
                    print(f"Target Found at index: {index}")
                else:
                    print(f"Target not found in list")

            # Driver Code
            # Defining List Parameter
            Numbers = [1,2,3,4,5,6,7,8,9,10]

            # Test Case 1
            Result = LinearSearchAlgo(Numbers, 12)
            Verify(Result)

            # Test Case 2
            Result = LinearSearchAlgo(Numbers, 8)
            Verify(Result)

        
        class BinarySearch:
            '''
            Binary Search:
                Algorithm:
                    1. Determine the middle position of the sorted list
                    2. Compare the element in the middle position to the target element
                    3. IF the element match we return the middle position and end
                    4. IF the element DO NOT match Check whether the element in the middle position
                        is smaller then the target element
                        IF True then go back to step 2 with a new list
                            that goes form the middle position of current list to the end of the current list
                    5. IF the element in the middle position is greater then the target element then go back to step 2
                        with a new list that goes from the start of the current list to the middle position of the current list
                    Repeat process until the target element is found or until a sublist contains only one element
                        IF that single element sublist does not match the target element end the algorithm
                            indicating the element does not exist within the list. 
                BigO: 
                    O(log n) 
            '''
            print("______BINARY SEARCH:______")
            # Function that takes two arguments:
                # The list we are searching through
                # The target value we are looking for
            def BinarySearchAlgo(List, Target):
                
                # Defining/ Setting the first length of the list
                First = 0

                # Defining the last position within the list
                Last = len(List) - 1
                
                # Counter Variable:
                Counter = 0

                # Keep executing until the value of first is less then or qual to last value
                while First <= Last:

                    Counter += 1
                    # Calculate the midpoint of list
                        # //2 Divide by 2 of First + Last values but round down to even known as floor division
                    Midpoint = (First + Last)//2   

                    # Check to see whether the value at this Midpoint is the same as the Target
                    # If Midpoint within List value is equal to Target : 
                        # exit loop and return Midpoint
                    if List[Midpoint] == Target:
                
                        return Midpoint
                    
                    # Elif Midpoint with List value is less then Target : 
                        # Then set the new variable first to equal Midpoint + 1 
                        # Then return back to the while statement and rerun while loop until First If statement is true
                    elif List[Midpoint] < Target:
                        First = Midpoint + 1

                    # Else: if the List[Midpoint] is greater then Target :
                        # Then Set the new variable last to the Midpoint - 1
                        # And return back to the while statement and rerun while loop until condition are met
                    else:
                        Last = Midpoint - 1
                
                # If While Loop if false or not within list then return None
                return None

                
            # Function to verify index if not None:
            def Verify(index):
                if index is not None:
                    print(f"Target Found at index: {index}")
                else:
                    print(f"Target not found in list")
            
            # Driver Code
            # Define Test Case List
            Numbers =  [1,2,3,4,5,6,7,8,9,10]

            # Test Case 1
            Result = BinarySearchAlgo(Numbers, 12)
            Verify(Result)

            # Test Case 2
            Result = BinarySearchAlgo(Numbers, 6)
            Verify(Result)
        
        class RecursiveBinarySearch:

            def RecursiveBinarySearchAlgo(List, Target):
                ''

    class SortingAlgorithms:
        '''
        Merge Sort:
            Algorithm:
                Split a list into two lists down the middle.
                Then takes each sub list and splits that in half down the middle.
            BigO: 
                O(n log n)
        '''
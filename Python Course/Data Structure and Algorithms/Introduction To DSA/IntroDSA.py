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
        

        # Function that takes two arguments:
            # The list we are searching through
            # The target value we are looking for within the list
        print("______RECURSIVE BINARY SEARCH:______")
        class RecursiveBinarySearch:
                
            def RecursiveBinarySearchAlgo(List, Target):
                '''
                Return true value if it exists and a false if it doesn't
                '''

                # If the length of the List is equal to 0 : return False
                if len(List) == 0:
                    return False

                # Else if the list is not empty
                else:
                    Midpoint = (len(List))//2

                    # IF the Midpoint value within the list is equal to Target value: return true
                    if List[Midpoint] == Target:
                        return True
                        
                    '''
                    # Else if the midpoint is not equal to the target:
                    else:
                        
                        # If the midpoint is less then the target
                        if List[Midpoint] < Target:

                            # Recursion the function again creating a new list starting from the midpoint
                            return Algorithms.SearchAlgorithm.RecursiveBinarySearch.RecursiveBinarySearchAlgo(List[Midpoint + 1:], Target)
                        
                        # Else if the midpoint is greater then the target
                        else:

                            # Re-loop the function creating a new list starting from the midpoint
                            return Algorithms.SearchAlgorithm.RecursiveBinarySearch.RecursiveBinarySearchAlgo(List[:Midpoint], Target)    
                    '''

            def Verify(Result):
                print("Target found: ", Result)

            Numbers = [1,2,3,4,5,6,7,8]

            # Test Cases
            Result = RecursiveBinarySearchAlgo(Numbers, 12)
            Verify(Result)

            Result = RecursiveBinarySearchAlgo(Numbers, 5)
            Verify(Result)

    class SortingAlgorithms:
        '''
        Merge Sort:
            Algorithm:
                Split a list into two lists down the middle.
                Then takes each sub list and splits that in half down the middle.
            BigO: 
                O(n log n)
        '''

class DataStructure:
    def __init__(self):
        self.name = 'DataStructure'
        self.ARY = self.Array()
        self.LL = self.LinkList()
    
    '''
    A data storage format. It is the collection of values and the format they are stored in, 
        the relationships between the values in th collection as well as the operations applied
        on the data stored in the structures. 
    Data structures are methods of storing and organizing data in a computer system 
        so that operations can be performed upon them more efficiently. 
    '''
    '''
    Operations on Data Structures:
        Access and read values
        Search for an arbitrary values
        Insert values at any point into the structure
        Delete values in the structure
    '''

    print("______ARRAY:______")
    class Array:
        
        '''
        Fundamental data structure that can be used to represent a collection of values.
            where each value is referenced using an index or a key.
            Are also used as building blocks to create more custom data types and structures. 
        Elements in a array are identified using a value knows as an index
            to access and read the value
        '''

        '''
        An array is a collection of items that are stored sequentially. 
            An array contains values or variables—known as “elements”—of the same data type and is of a fixed size, 
            so you cannot change the size of an array. 
            Each item in an array is indexed starting with 0.
        Arrays are commonly used as structures for building other, more complicated data structures. 
            They are also used for sorting algorithms.

        Arrays are better at access the value then searching
        Worst Case: Linear Runtime
        '''

        '''
        Implementations:
            Operations:
                Insert:
                    Using a index value where we can insert an element anywhere in the list
                    Will shift all elements at position inserted to the right
                    Linear Runtime O(n)
                Append:
                    Adds the item to the end of the list
                    Constant Runtime
                Extend:
                    Adds one list to another
                    O(k)
                Delete:
                    Delete Operation shifts each element to the left at position target delete
                    Linear Runtime O(n)
        '''

        def CheckList(): 
            NewList = [1,2,3.4,5]
            Result = NewList[0]

            # weather a list contains a item or value
            if 1 in NewList:
                print(True)
            
            # Linear Search to check within a list if it contain a value
            for i in NewList:
                if i == 1:
                    print(True)
                break
        CheckList()
        
        def OperationArray():
            # empty list
            Numbers = []
            
            # adds 2, 200 to the end of the list
            Numbers.append(2)
            Numbers.append(200)

            # 1 inserted at index 0
            Numbers.insert(0, 1)

            # new list added to the end of first list
            Numbers.extend([4,5,6])
            print(Numbers)
        OperationArray()

    print("______LINKED LIST:______")
    class LinkList():
        pass
        '''
        
        A linked list is a sequence of items arranged in a linear order all connected to each other. 
            This means you must access data in order, so random access to data is not possible.

        Each element in a linked list is contained in a separate object called a “node,” 
            and each node contains a key and a pointer. 
            The pointer directs you to the next node, called a “next.” 
            The sequence starts with a “head,” which directs you to the first element within the list. 
            The last element of this list is known as the “tail.”

        You can create a singly linked list, which lets you traverse each item in a forward direction from the head to the tail. 
            Similarly, you can create a doubly-linked list, which can be traversed both forward and backward. 
            And finally, you can create a circular linked list in which the next pointer of the tail points to the head
            and vice versa, forming a circle.

        Linked lists are used for symbol table management in switching between programs using Alt + Tab 
        '''

        class Node:

                # An object for storing a single node of a linked list
                # Models two attributes - data and teh link to the next node in the list
                # instance variables

                Data = None
                NextNode = None

                

                def __init__(self, Data):
                    self.Data = Data

                def __repr__(self):
                    return "<Node Data: %s>" % self.Data
                    
        class SingleLinkedList:

            

            '''
            Returns the number of nodes in the list
            Takes O(n) Linear Time
            '''
            def __init__(self):
                self.Head = None
            
            def IFISEmpty(self):
                return self.Head == None

            def __repr__(self):
                
                # Returns a string representation of the list
                Nodes = []
                Current = self.Head

                while Current:
                    if Current is self.Head:
                        Nodes.append(f"[Head: {Current.Data}]")
                    elif Current.NextNode is None:
                        Nodes.append(f"[Tail: {Current.Data}]")
                    else:
                        Nodes.append(f"[{Current.Data}]")

            def Size(self):

                # Reference to the first element
                Current = self.Head

                # Counter variable
                Count = 0

                # Keep looping until there are no more nodes
                while Current:

                    # Increment 1
                    Count += 1

                    # Assigning next node to current
                    Current = Current.NextNode
                return Count

            # Add function is going to accept some data to add to the list inside of a node
            def Add(self, Data):
                
                # Adds new node containing data at head of the list
                # O(1)
                NewNode = DataStructure.LinkList.SingleLinkedList.Node(Data)
                NewNode.NextNode = self.Head
                self.Head = NewNode
            
            

        Node1 = Node(10)
        print(Node1)

        l = SingleLinkedList()
        l.Head = Node1
        print(l.Add(1))
        print ("Size = ", l.Size())



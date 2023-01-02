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

    '''
The Node class represents a single node in a linked list data structure. 
    It has two attributes: data and next_node. 
    The data attribute stores the data that is stored in the node, 
    and the next_node attribute stores a reference to the next node in the linked list. 
    The Node class has an __init__ method that is used to initialize a new Node object, and a __repr__ method that is used to specify how a Node object should be represented as a string.
'''

    # An object for storing a single node of a linked list
    # Models two attributes - data and teh link to the next node in the list
    # instance variables

    Data = None
    NextNode = None
    PrevNode = None
                

                

    def __init__(self, Data, PrevNode, NextNode):
        self.Data = Data
        self.PrevNode = PrevNode
        self.NextNode = NextNode

    def __repr__(self):
        return "<Node Data: %s>" % self.Data
            
class SinglyLinkedList:

    '''
The SinglyLinkedList class represents a linked list data structure that stores a sequence of nodes. 
    It has a single attribute, head, which is a reference to the first node in the list. 
    The SinglyLinkedList class has several methods that can be used to perform various operations on the linked list, 
    such as adding and removing nodes, searching for specific nodes, and inserting nodes at specific positions in the list.
'''


    '''
    Linear data structure that stores values in nodes. 
        The list maintains a reference to the first node, also called head. 
        Each node points to the next node in the list
    '''

    '''
    Returns the number of nodes in the list
    Takes O(n) Linear Time
    '''


    def __init__(self):
        self.Head = None

    
    def __repr__(self):

        '''
        __repr__: This method specifies how a SinglyLinkedList object should be represented as a string.
        '''
        
        # Returns a string representation of the list

        # Empty List
        Nodes = []

        # Set current to head pointer to head 
        Current = self.Head

        # As long as Current does not equal None:
        while Current != None:

            # If the current node is the same as the head
            if Current is self.Head:

                # Append as head marker
                Nodes.append(f"[Head: {Current.Data}]")
            
            # If pointer is rather at the tail then mark as tail
            elif Current.NextNode is None:
                Nodes.append(f"[Tail: {Current.Data}]")

            # Else if pointer is not at head or tail append each data point to list
            else:
                Nodes.append(f"[{Current.Data}]")
            
            # Each iteration of loop move current value to the next mode 
            Current = Current.NextNode
        
        # Joins all the string using .join into one string 
        return  '-> '.join(Nodes)
    
    def NodeAtIndex (self, Index):
        if Index == 0:
            return self.Head
        
        # Traversing the linked list and counting up to the index
            # visiting each node
        else:
            Current = self.Head
            Position = 0
            
            while Position < Index:
                Current = Current.NextNode
                Position += 1

            return Current

    def ISEmpty(self):
        '''
        ISEmpty: This method returns True if the linked list is empty, and False otherwise. 
            It takes constant time (O(1)) to execute.
        '''
        # Determines if the linked list is empty
        return self.Head == None

    def Size(self):

        # Reference to the first element
        Current = self.Head

        # Counter variable
        Count = 0

        # Keep looping until there are no more nodes as long as Current is not equal to none
        while Current != None:

            # Increment 1
            Count += 1

            # Assigning next node to current
            Current = Current.NextNode

        return Count

    def Add(self, Data):

        '''
        add: This method adds a new node containing the specified data to the head of the linked list. 
            It is also known as the "prepend" operation. 
            It takes constant time (O(1)) to execute.
        '''
        
        # Adds new node containing data at head of the list
        # O(1)
        NewNode = Node(Data)
        NewNode.NextNode = self.Head
        self.Head = NewNode
    
    def Remove(self, Key):
        '''
        Removes Node containing data that matches the key
        Returns the node or None iff key doesn't exit
        Take O(n) time
        '''
        Current = self.Head
        Previous = None
        Found = False

        while Current != None and not Found != False:
            if Current.Data == Key and Current == self.Head:
                Found = True
                self.Head = Current.NextNode
            elif Current.Data == Key:
                Found = True
                Previous.NextNode = Current.NextNode
            else:
                Previous = Current
                Current = Current.NextNode
        return Current
    
    def Search(self, Key):
        '''

        search: This method searches for the first node containing data that matches the specified key. 
            It returns the node if it is found, or None if it is not found. 
            It takes linear time (O(n)) to execute, where n is the length of the linked list.
        '''

        # pointer to the head
        Current = self.Head

        # While current is not none
        while Current != None:

            # if the CurrentData is equal to the key return current value
            if Current.Data == Key:
                return Current
            
            # else move to the next node setting the value of the next node to current
            else:
                Current = Current.NextNode
        
        # Returns the node or None if not found
        return None
    
    def Insert(self, Data, Index):
        '''

        insert: This method inserts a new node containing the specified data at the specified index position in the linked list. 
            It takes overall linear time (O(n)) to execute, where n is the length of the linked list.

        '''
        '''
        The method takes three arguments:
            self: This is a reference to the current instance of the object that the method is being called on. 
                In Python, the self keyword is used to refer to the current instance of a class.
            Data: This is the data that will be stored in the new node that the method will insert into the linked list.
            Index: This is the position at which the new node will be inserted into the linked list.
        '''

        # If the index is 0, add the new node to the beginning of the list
        if Index == 0:
            self.Add(Data)
        
        # If the index is greater than 0, insert the node at the specified position
        elif Index > 0:

            # Create a new node with the given data
            NewNode = Node(Data)

            # Set the position to the index and the current node to the head of the list
            Position = Index
            Current = self.Head

            # Keep moving the current node to the next node in the list until we reach the desired position
            while Position > 1:
                Current = Node.NextNode
                Position -= 1

            # Set the next node of the node preceding the new node to the new node
            PreviousNode = Current
            NextNode = Current.NextNode

            # Set the next node of the new node to the node originally in that position
            PreviousNode.NextNode = NewNode
            NewNode.NextNode = NextNode
      
# Driver Code for SinglyLinkedList
Node1 = Node(10)
print(Node1)

List = SinglyLinkedList()
List.Add(10)
List.Add(2)
List.Add(45)
List.Add(15)
NodeData = List.Search(45)
print(NodeData)
print(List)

print("______DOUBLY LINKED LIST:______")
class DoublyLinkedList:
    
    def __init__(self):
        self.Head = None
        self.__count = 0
    
    def __iter__(self):
        Current = self.Head

        while Current:
            yield Current
            Current = Current.NextNode


    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        Nodes = []
        Current = self.Head
        while Current:
            if Current is self.Head:
                Nodes.append(f"[Head: {Current.Data}]")
            elif Current.NextNode is None:
                Nodes.append(f"[Tail: {Current.Data}]")
            else:
                Nodes.append(f"[{Current.Data}]")
            Current = Current.NextNode
        return  '-> '.join(Nodes)
    
    def ISEmpty(self):
        return self.Head is None
    
    def __len__(self):
        return self.__count
    
    def Add(self, Data):
        '''
        Adds new Node containing data to head of the list
        prepend
        O(1)
        '''

        NewHead = Node(Data, PrevNode=None, NextNode=self.Head)

        if not self.ISEmpty():
            self.Head.PrevNode = NewHead
        
        self.Head = NewHead
        self.__count += 1
    
    def Search(self, Key):
        '''
        Search for the first node containing data that match the key
        Returns the node or 'None' if not found
        O(n)
        '''

        Current = self.Head

        while Current != None:
            if Current.Data == Key:
                return Current
            else:
                Current = Current.NextNode
        return None

    def NodeAtIndex(self, Index):
        '''
        Return the Node at specified index
        O(n)
        '''
        if Index >= self.__count:
            raise IndexError('Index out of range')
        
        if Index == 0:
            return self.Head
        
        Current = self.Head
        Position = 0

        while Position < Index :
            Current = Current.NextNode
            Position += 1
        
        return Current
    
    def Insert(self, Data, Index):
        '''
        Inserts a new node containing data at index position
        Insertion takes O(1) but finding node at insertion point takes O(n) time
        overall O(n)
        '''

        if Index >= self.__count:
            raise IndexError('Index out of range')
        
        if Index == 0:
            self.Add(Data)
            return
        
        if Index > 0:
            CurrentNode = self.NodeAtIndex(Index)
            PrevNode = CurrentNode.PrevNode
            NewNode = Node(Data, PrevNode=PrevNode, NextNode=CurrentNode)
            CurrentNode.PrevNode = NewNode
            PrevNode.NextNode = NewNode
        
        self.__count += 1
    
    def Remove(self, Key):
        '''
        Remove Node containing data that matches the key 
        Returns the node or 'None' if key doesn't exist
        O(n)
        '''

        Current = self.Head
        Found = False

        while Current != None and not Found != None:
            if Current.Data == Key and Current is self.Head:
                Found = True
                self.Head = Current.NextNode
                self.Head.PrevNode = None
                self.__count -= 1
                return Current
            elif Current.Data == Key:
                Found = True
                PrevNode = Current.PrevNode
                NextNode = Current.NextNode
                PrevNode.NextNode = NextNode
                NextNode.PrevNode = PrevNode
                self.__count -= 1
                return Current
            else:
                Current = Current.NextNode

    def RemoveAtIndex(self, Index):
        """
        Removes Node at specified index
        Takes O(n) time
        """

        if Index >= self.__count:
            raise IndexError('index out of range')

        Current = self.Head

        if Index == 0:
            self.Head = Current.NextNode
            self.Head.PrevNode = None
            self.__count -= 1
            return Current

        Current = self.NodeAtIndex(Index)
        PrevNode = Current.PrevNode
        NextNode = Current.NextNode
        PrevNode.NextNode = NextNode
        NextNode.PrevNode = PrevNode

        self.__count -= 1

        return Current

print("______MERGE SORT:______")
class MergeSort:

    def MergeSort(List):
        '''
        Sorts a list in ascending order
        Returns a new sorted list

        Divide: Find the midpoint of the list and divide into sublist
        Conquer: Recursively sort the sublist created in Divide step 
        Combine: Merge the sorted sublist created in Conquer step

        O(n log n)
        '''

        # IF a list is empty or has one element the list is already sorted: Return Lists
        if len(List) <= 1:
            return List
        
        # Divide Step to set left half and right half variable using split function of the list
        LeftHalf, RightHalf = MergeSort.Split(List)

        # Conquer Step where we sort each sub-list and return a new sorted sub-list
        Left = MergeSort.MergeSort(LeftHalf)
        Right = MergeSort.MergeSort(RightHalf)
        
        return MergeSort.Merge(Left, Right)
    
    def Split(List):
        '''
        Divide the unsorted list at midpoint into sublist
        Returns two sublist - left and right
        '''

        # Determine Midpoint using floor division  
        Midpoint = len(List)//2

        # Starting at the very begging of the list towards the midpoint but not including midpoint
        Left = List[:Midpoint]

        # Starting at Midpoint including midpoint towards the end at the end of the list
        Right = List[Midpoint:]

        return Left, Right
    
    def Merge(Left, Right):
        '''
        Merge two lists (arrays), sorting them in the process
        Returns a new merged lists

        Overall Runtime:  linear time O(n) time
        '''

        # empty list
        l = []
        
        # keep track for indexes in the left list
        i = 0

        # keep track for indexes in the right list
        j = 0

        # keep looping as long as i is less then the length of the left list as well as j is less then the length of the right list
        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                l.append(Left[i])
                i += 1
            else:
                l.append(Right[j])
                j += 1
        
        while i < len(Left):
            l.append(Left[i])
            i +=1

        while j < len(Right):
            l.append(Right[j])
            j +=1
        return l 

    def VerifySorted(List):
        n = len(List)
        
        if n == 0 or n == 1:
            return True
        
        return List[0] < List[1] and MergeSort.VerifySorted(List[1:])

AList = [54,62,93,71,17,77,31,44,55,20]
l = MergeSort.MergeSort(AList)
print(l)
l = MergeSort.VerifySorted(AList)
print(l)

class MergeSortLinkedList(SinglyLinkedList):

    def MergeSortLL():
        '''
        Sorts a linked list in ascending order
        - Recursively divides the linked list into sublists containing a single node
        - Recursively merge the sublist to produce sorted subsists until one remains

        Returns a sorted Linked List

        Takes O(n log n) time
        Takes O(n) space
        '''
        if SinglyLinkedList.Size() == 1:
            return SinglyLinkedList
        elif SinglyLinkedList.Head is None:
            return SinglyLinkedList
        
        LeftHalf, RightHalf = MergeSort.Split(SinglyLinkedList)
        Left = MergeSort(LeftHalf)
        Right = MergeSort(RightHalf)

        return MergeSort.Merge(Left, Right)
    
    def Split():
        '''
        Divide the unsorted list at midpoint into sublists
        '''

        if SinglyLinkedList == None or SinglyLinkedList.Head == None:
                LeftHalf = SinglyLinkedList
                RightHalf = None

                return LeftHalf, RightHalf
        else:

            # To calculate Size
            Size = SinglyLinkedList.Size()

            # Calculate Midpoint
            Midpoint = Size//2

            MidpointNode = SinglyLinkedList.NodeAtIndex(Midpoint-1)

            LeftHalf = SinglyLinkedList
            LinkedList = []
            RightHalf = LinkedList()
            RightHalf.Head = MidpointNode.NextNode
            MidpointNode.NextNode = None
        return LeftHalf, RightHalf
    
    def Merge(Left, Right):
        """
        Merges two linked lists, sorting by data in nodes
        Returns a new merged list
        Takes O(n) space
        Runs in O(n) time
        """
        
        LinkedList = []
        # Create a new linked list that contains nodes from merging left and right
        Merged = LinkedList()
        # Add a fake head that is discarded later.
        Merged.Add(0)
        # Set current to the head of the linked list
        Current = Merged.Head

        # Obtain head nodes for left and right linked lists
        LeftHead = Left.Head
        RightHead = Right.Head

        # Iterate over left and right as long until the tail node of both
        # left and right
        while LeftHead or RightHead:
            # If the head node of left is None, we're at the tail
            # Add the tail node from right to the merged linked list
            if LeftHead is None:
                Current.NextNode = RightHead
                # Call next on right to set loop condition to False
                RightHead = RightHead.NextNode 
            # If the head node of right is None, we're at the tail
            # Add the tail node from left to the merged linked list
            elif RightHead is None:
                Current.NextNode = LeftHead
                # Call next on left to set loop condition to False
                LeftHead = LeftHead.NextNode
            else:
                # Not at either tail node
                # Obtain node data to perform comparison operations
                LeftData = LeftHead.Data
                RightData = RightHead.Data

                # If data on left is lesser than right set current to left node
                # Move left head to next node
                if LeftData < RightData:
                    Current.NextNode = LeftHead
                    LeftHead = LeftHead.NextNode
                # If data on left is greater than right set current to right node
                # Move right head to next node
                else:
                    Current.NextNode = RightHead
                    RightHead = RightHead.NextNode

            # Move current to next node
            Current = Current.NextNode

        # Discard fake head and set first merged node as head
        Head = Merged.Head.NextNode
        Merged.Head = Head

        return Merged



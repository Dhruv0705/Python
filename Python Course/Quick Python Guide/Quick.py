class Variable:
    
    # Variables are dynamically typed
    # Single Assignments 
    N = 0 
    print ('N =' , N)

    N = "abc"
    print('N =', N)

    # Multiple Assignments
    N, M, Z = 0, "abc", False
    print(f"Multiple Assignments: N = {N} M = {M} Z = {Z}") # print(N, M, Z)

    # Increment
    N = N + 1
    N += 1
    print(f"Incrementing: N = {N}")

    # None is null (absence of value)
    N = 4
    N = None
    print(f"Null: N = {N}")

class IfElse:

    # If statements dont need parentheses
    N = 1
    if N > 2:
        N -= 1
    elif N == 2:
        N *= 2
    else:
        N += 2
    print(N)

    # Needed for multi-line conditions
        # and = &&
        # or = ||
        
    N, M = 1 , 2
    if N > 2 and N != M or N == M:
        N += 1
    print(N, "\n")

class Loops:
    # While loops are similar
    N = 0
    while N < 5:
        print (N)
        N += 1
    
    print("\n")

    # Looping from i = 2 to i = 2
    for i in range(2, 5):
        print(i)

    print("\n")
    # Looping from i = 5 to i = 2
    for i in range(5, 1, -1):
        print(i)
    
class Math:

    print("____")
    # Division is decimal by default
    print(5/2) # 2.5

    # Division round down (Floor Division)
    print(5 //2) # 2

    # Negative number will also round down
    print(-3 // 2) # -2

    # Modulo Operations 
    # Modulo finds remainders
    print(10 % 3) # 1

    # Math helpers
    import math
    print(math.floor(3/2)) # 1
    print(math.ceil(3/2)) # 2
    print(math.sqrt(2)) # 1.414
    print(math.pow(2, 3)) # 8.0

    print("\n")

# Lists
class Arrays:

    print("____ARRAYS____")
    # also called lists
    Array = [1, 2, 3]
    print(Array)

    # Can be used as a stack
    # appends to the end of list
    Array.append(4)
    Array.append(5)
    print(Array)
    
    # pop removes last in list
    Array.pop()
    print(Array)

    # insert position, value
    Array.insert(1, 7)
    print(Array)

    # Reassign
    Array[0] = 8
    Array[3] = 27
    print(Array)

    # -1 is not out of bounds, its the last value
    Array = [1,2,3]
    print(Array[-1])

    # Sublists (Slicing)
    Array = [1,2,3,4]

    # start : end : step
    print(Array[1:3])
    print(Array[0:4])
    print(Array[0:4:2])

    # Unpacking
    A, B, C = [1, 2, 3]
    print(A, B, C , "\n")

    class LoopingArray:

        print("____LOOPINGARRAYS____")
        # Looping through arrays
        Nums = [1,2,3]
        for i in range(len(Nums)):
            print(Nums[i])

        print("\n")
        # without index
        for n in Nums:
            print(n)

        print("\n")
        # index and value
        for i, n in enumerate(Nums):
            print(i,n)

        print("\n")
        # Loop through multiple arrays simultaneously with unpacking
        # Zip combines two arrays        
        Nums1 = [1,3,5]
        Nums2 = [2,4,6]

        for n1, n2 in zip(Nums1, Nums2):
            print(n1, n2)
        
        print("\n")
    
    class ReversingArray:

        print("____REVERSINGARRAYS____")

        
        # Reversing Array
        ReverseNums = [1,2,3]
        ReverseNums.reverse()
        print(ReverseNums)
        print("\n")

    class SortingArray:

        print("____SORTINGARRAYS____")
        
        # Sorting Array
        Array = [5,4,7,3,8]
        Array.sort()
        print(Array)

        Array.sort(reverse=True)
        print(Array)

        print("\n")
        # Sort Strings
        AlphaArray = ["Bob", "Alice", "Jane", "David"]
        AlphaArray.sort()
        print(AlphaArray)

        # Custom Sort (by length of string)
        # key = function without a name in which takes every value from the array 
            # call it x and return the length of x 
        AlphaArray.sort(key=lambda x: len(x))
        print(AlphaArray)

    class ListComprehension:

        print("____LISTCOMPREHENSION____")
        # List Comprehension 
        InterArrayLoop = [i for i in range(5)]
        print(InterArrayLoop)

        InterArrayLoop = [i+i for i in range(5)]
        print(InterArrayLoop)

        print("\n")

    class TwoDArray:

        print("____2DARRAYS____")
        GridArray = [[0] * 4  for i in range(4)]
        print(GridArray)

        print("\n")

class Queues:

    print("____QUEUES____")
    from collections import deque

    Queue = deque()
    Queue.append(13)
    Queue.append(27)
    print(Queue)

    Queue.popleft()
    print(Queue)

    Queue.appendleft(10)
    print(Queue)

    Queue.pop()
    print(Queue)

    print("\n")


class HashSet :

    print("____HASSETS____")
    My_Set = set()
    My_Set.add(1)
    My_Set.add(2)
    print(My_Set)
    print(len(My_Set))

    print(1 in My_Set)
    print(2 in My_Set)
    print(3 in My_Set)

    My_Set.remove(2)
    print(2 in My_Set)

    #list to set
    print(set([1,2,3,4]))

    # set comprehension
    My_Set = { i for i in range(5)}
    print(My_Set)

    print("\n")

# Dictionaries
class HaspMap:
    print("____HASHMAPS____")
    # setting key to value
    My_Map = {}
    My_Map["Alice"] = 88
    My_Map["Bob"] = 77
    print(My_Map)

    My_Map["Alice"] = 80
    print(My_Map["Alice"])

    print("Alice" in My_Map)
    My_Map.pop("Alice")
    print("Alice" in My_Map)
    print(My_Map)

    # manually setting key and value
    My_Map = {"Alice" : 40, "Bob": 72}
    print(My_Map)

    
    # Dict comprehension
        # Setting i as value X 2 each looping through range of 3 setting key to 0 - 3 with value 0 +*2
    My_Map = {i: 2*i for i in range(3) }
    print(My_Map)

    print("\n")
    # Looping through Maps
    My_Map = { "Alice" : 60, "Bob": 23}

    for key in My_Map:
        print(key, My_Map[key])
    
    for val in My_Map.values():
        print(val)
    
    for key, values in My_Map.items():
        print(key, values)

    print("\n")

class Tuples:

    print("____TUPLES____")
    # can be used as keys for has map/set
    # Mapping a pair of values 1,2 to 3
    Tuple = { (1,2):3}
    print(Tuple)

    My_Set = set()
    My_Set.add((1,2))
    print((1,2) in My_Set)

    # lists cant be keys
    # My_Map [[3,4]] = 5

    print("\n")

class Heaps:
    print("____HEAPS____")

    import heapq

    # Under the hood are arrays
    # Smallest to largest
    Min_Heap = []
    heapq.heappush(Min_Heap, 3)
    heapq.heappush(Min_Heap, 2)
    heapq.heappush(Min_Heap, 4)

    # Min is always at index 0 
    print(Min_Heap[0])

    while len(Min_Heap):
        print(heapq.heappop(Min_Heap))
    
    print("\n")
    # From largest to smallest multiply by - using min heap push and pop

    # Build Heap from values
    Array = [2,1,8,4,5]
    heapq.heapify(Array)
    while Array:
        print(heapq.heappop(Array))
    
    print("\n")

class Functions:

    print("____FUNCTIONS____")
    
    def MyFunction(n,m):
        return n * m
    print(MyFunction(3,4))

    def Outer(a,b):
        c = "C"
    
        def Inner():
            return a+b+c
        return Inner()
    
    print(Outer("a", "b"))

    # Can modify objects but not reassign unless using nonlocal keywords
    def double (arr, val):
        def helper():
            # Modifying array works
            for i, n in enumerate(arr):
                arr[i] *= 2
    
            # will only modify val in the helper scope
            # val *=2
            
            # to modify val outside helper scope
            nonlocal val
            val *= 2

        helper()
        print(arr, val)
    nums = [1,2]
    val = 3
    double(nums, val)

class MyClass:
    # constructor
    def __init__(self, nums):
        
        # Create member variables
        self.nums = nums
        self.size = len(nums)

    # self key words requires as param
    def GetLength(self):
        return self.size
    
    def GetDoubleLength(self):
        return 2 * self.GetLength()

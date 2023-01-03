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

class Arrays:
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
    print(A, B, C)

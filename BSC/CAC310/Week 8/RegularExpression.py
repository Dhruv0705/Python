# ____REGULAR EXPRESSION____

list1 = [1,2,3]
list2 = [3,1,4]
list3 = []

for x in list1:
    for y in list2:
        list3.append(x+y)
print(list3)

# List comprehension
list3 = [x+y for x in [1,2,3] for y in [3,1,4]]


list4 = [1,2,3]
list5 = [3,1,4]
list6 = []

for x in list4:
    for y in list5:
        if x!=y:
            list6.append((x,y))
print(list6)

# List comprehension
list6 = [(x,y) for x in [1,2,3] for y in [3,1,4] if x!= y]

# ____RECURSION____

# FACTORIAL
def factorialRecursive(N):
    "Recursive factorial function"
    assert isinstance(N, int) and N >= 1
    return 1 if N <= 1 else N + factorialRecursive(N-1)

def factorialIterative(N):
    "Iterative factorial function"
    assert isinstance(N, int) and N >= 1
    product = 1
    while N >= 1:
        product *= N
        N -= 1
    return product

def fib(n):
    if n == 1 or n ==0 :
        return 1
    else:
        return fib(n-1) + fib(n-2)


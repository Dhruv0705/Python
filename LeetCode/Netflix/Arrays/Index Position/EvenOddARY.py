# Given an array, write a program to find the sum of values of even and odd index positions separately.

# Python program to find out
# Sum of elements at even and
# odd index positions separately
# Function to calculate Sum
def EvenOddSum(arr, n):
    even = 0
    odd = 0
    for i in range(n):
 
        # Loop to find even, odd Sum
        if i % 2 == 0:
            even += arr[i]
        else:
            odd += arr[i]
     
    print ("Even index positions sum ", even)
    print ("Odd index positions sum ", odd)
 
# Driver Function
 
arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
 
EvenOddSum(arr, n)

# Python program to find out
# Sum of elements at even and
# odd index positions separately
 
# Function to calculate Sum
 
 
def EvenOddSum(arr, n):
    even_sum = sum(arr[::2])
    odd_sum = sum(arr[1::2])
    print("Even index positions sum", even_sum)
    print("Odd index positions sum", odd_sum)
 
 
# Driver Function
 
arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
 
EvenOddSum(arr, n)
# In this solution, we first sort the array. 
# Then we fix one element ‘e’, 
# and try to find a pair (a, b) in the remaining array 
# such that required_sum - e = a + b.

# We start with the first element e in the array (at index i = 0) 
# and try to find such a pair (a, b) 
# in the remaining array (i.e A[i + 1] 
# to A[n - 1]) that satisfies the condition: a+b = required_sum - e. 
# We can find such a pair in linear time. 
# If we find such a pair, 
# we have found the solution: a, b and e 
# and thus, we can stop the iteration.

# Otherwise, we repeat the above steps 
# for all elements e 
# at index i = 1 to n - 3, 
# until we find a pair that meets the condition.

# Given an array of integers and a value, determine if there are any three integers in the array whose sum equals the given value.
# Consider this array and the target sums.

def find_sum_of_two(A, val, start_index):
  i = start_index
  j = len(A) - 1
  while i < j:
    s = A[i] + A[j]
    if s == val:
      return True

    if s < val:
      i += 1
    else:
      j -= 1

  return False

def find_sum_of_three_v3(arr, required_sum):
  arr.sort()
  for i in range(0, len(arr)-2):
    remaining_sum = required_sum - arr[i]
    if find_sum_of_two(arr, remaining_sum, i+1):
      return True

  return False
  
def test():
  arr = [-25, -10, -7, -3, 2, 4, 8, 10]
  print(find_sum_of_three_v3(arr, -8)) 
  print(find_sum_of_three_v3(arr, -25))
  print(find_sum_of_three_v3(arr, 0))
  print(find_sum_of_three_v3(arr, -42))
  print(find_sum_of_three_v3(arr, 22))
  print(find_sum_of_three_v3(arr, -7))
  print(find_sum_of_three_v3(arr, -3)) 
  print(find_sum_of_three_v3(arr, 2)) 
  print(find_sum_of_three_v3(arr, 4)) 
  print(find_sum_of_three_v3(arr, 8))
  print(find_sum_of_three_v3(arr, 7)) 
  print(find_sum_of_three_v3(arr, 1))
  
test()
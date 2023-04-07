'''
Fizz Buzz [Easy] [https://leetcode.com/problems/fizz-buzz/]

Given an integer n, return a string array answer (1-indexed) where:

    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i if non of the above conditions are true.

Example 1:

    Input: n = 3
    Output: ["1","2","Fizz"]

Example 2:

    Input: n = 5
    Output: ["1","2","Fizz","4","Buzz"]

'''

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        
        # Initialize an empty list
        answer = []
        
        # Loop through each number from 1 to n
        for i in range(1, n + 1):
            
            # If the number is divisible by 3 and 5
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            
            # If the number is divisible by 3
            elif i % 3 == 0:
                answer.append("Fizz")
            
            # If the number is divisible by 5
            elif i % 5 == 0:
                answer.append("Buzz")
            
            # If the number is not divisible by 3 or 5
            else:
                answer.append(str(i))
        
        # Return the answer list
        return answer
'''
def fizzBuzz(n):
    for i in range(1, n + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
            
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0: 
            print("Buzz")
'''
    
    
'''
Climbing Stairs
https://leetcode.com/problems/climbing-stairs/

    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

        Example 1:
            Input: n = 2
            Output: 2
            Explanation: There are two ways to climb to the top
                1. 1 step + 1 step
                2. 2 step
        
        Example 2:
            Input: n = 3
            Output: 3
            Explanation: There are three ways to climb to the top.
                1. 1 step + 1 step + 1 step
                2. 1 step + 2 step
                3. 2 step + 1 step
    
    The problem is asking to find the number of ways to climb a staircase, 
        given that at each step you can either take 1 or 2 steps. 
        The input is an integer n, representing the number of steps in the staircase, 
        and the output is an integer, representing the number of ways to climb the staircase.

    There are several ways to solve the Climbing Stairs problem, 
        including using recursion, dynamic programming, and mathematical approaches.

        Recursion: One way to solve this problem is by using recursion, 
            where we define a function that returns the number of ways to climb the stairs
            given the remaining number of steps. The base case of the recursion is when there 
            are 0 or 1 steps remaining, in which case there is only 1 way to reach the top. 
            The recursive case is when there are more than 1 steps remaining, in which case 
            we can either take 1 step or 2 steps and add the number of ways to reach the top for each case. 
            The time complexity of this approach is O(2^n), since there are 2 recursive calls for each step.

        Dynamic Programming: Another way to solve this problem is by using dynamic programming, 
            where we use an array to store the number of ways to reach each step and compute the number of ways 
            to reach the top in a bottom-up fashion. The time complexity of this approach is O(n), 
            since we only need to compute the number of ways to reach each step once.

        Mathematical Approach: We can also solve this problem using a mathematical approach, 
            by observing that the number of ways to reach the n-th step is the sum of the number of ways 
            to reach the (n-1)-th step and the (n-2)-th step. This is because we can either take 1 step 
            from the (n-1)-th step or 2 steps from the (n-2)-th step to reach the n-th step. 
            This approach has a time complexity of O(n).

    The runtime of this problem is O(n). 
        This means that the time it takes for the algorithm to complete increases linearly 
        with the input size. In linear time cashing the result memoization storing each subproblem in memory 
        as each subproblem depends on one another
    
    Bottom Up Dynamic Programming Approach
        Start at base case and work our way up
        
        Starting at the base case n = 5 creating a array Dp = [? , ? , ? , ? , ?,  ?]
                                                               0   1   2   3   4   5
            How many step does it take to get to  5 starting at 5 as we already reached 5: 1
                                                        Dp = [? , ? , ? , ? , ?,  1]  
                                                              0   1   2   3   4   5
            How many steps does it take to get to 5 starting at 4 : 1 step
                                                        Dp = [? , ? , ? , ? , 1,  1]
                                                              0   1   2   3   4   5
            How many steps does it take to get to 5 starting at 3 : 2 using 4 and 5 subproblem add two together to get 1 + 1 = 2
                                                        Dp = [? , ? , ? , 2 , 1,  1]   
                                                              0   1   2   3   4   5
            How many steps does it take to get to 5 starting at 2 : using fibonacci through dp add the last two values 2 + 1
                                                        Dp = [? , ? , 3 , 2 , 1,  1] 
                                                              0   1   2   3   4   5
            How many steps does it take to get to 5 starting at 1 : 3 + 2 = 5
                                                        Dp = [? , 5 , 3 , 2 , 1,  1]
                                                              0   1   2   3   4   5
            How many steps does it take to get to 5 starting at 0 : 5 + 3 = 8
                                                        Dp = [8 , 5. , 3 , 2 , 1,  1]
                                                              0   1    2   3   4   5

    

'''
# Bottoms Up Approach
class Solution:
    def ClimbStairs(self, n: int) -> int:
        '''
        This function returns the number of ways to climb n stairs
        using either 1 or 2 steps at a time.
        '''
        
        # Initialize two variables both as one
        One, Two = 1, 1

        # Loop through `n` - 1 times 
        for i in range (n - 1):

            # Continuing updating the two initialized variables:

            # Set Temporary value before we update One
            Temp = One

            # # Updating One by adding the value of Two 
            One = One + Two
            
            # Shift 2 to One original position
            Two = Temp

        return One
    
    # Test cases
    n = ClimbStairs(0, 5)
    print(n)

    n = ClimbStairs(0, 3)
    print(n)


'''
Other Methods:
'''

#Brute Force:
class BruteForce:

    def climbStairs(n: int) -> int:
        
    # base case: if n is 0 or 1, there is only 1 way to climb the stairs
        if n == 0 or n == 1:
            return 1

        # recursive case: the number of ways to climb the stairs is equal to the sum of the number of ways 
            # to climb the stairs from the previous two steps
        return BruteForce.climbStairs(n-1) + BruteForce.climbStairs(n-2)

# Recursion with memoization:
class Recursion:
    def climbStairs(n: int) -> int:
    # create a list to store the number of ways to climb each step
        ways = [0] * (n+1)
        
    # base case: if n is 0 or 1, there is only 1 way to climb the stairs
        if n == 0 or n == 1:
            return 1

    # recursive case: the number of ways to climb the stairs is equal to the sum of the number of ways to climb the stairs from the previous two steps
        if ways[n] == 0:
            ways[n] = Recursion.climbStairs(n-1) + Recursion.climbStairs(n-2)
            return ways[n]

# Iterative approach:
class Iterative:
    def climbStairs(n: int) -> int:

        # base case: if n is 0 or 1, there is only 1 way to climb the stairs
        if n == 0 or n == 1:
            return 1

        # initialize two variables to store the number of ways to climb the stairs from the previous two steps
        a, b = 1, 1

        # iterate through n-1 steps
        for i in range(n-1):

        # update the values of a and b: a becomes b and b becomes the sum of a and b
            a, b = b, a + b

        # return b, which is the number of ways to climb the stairs from the current step
            return b


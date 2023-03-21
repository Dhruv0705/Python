'''
Min Cost Climbing Stairs
https://leetcode.com/problems/min-cost-climbing-stairs/ [Easy]

    You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
    Once you pay the cost, you can either climb one or two steps.

    You can either start from the step with index 0, or with the step with index 1. 

    Return the minimum cost to reach the top of the floor
    (Other words whats the minimum cost to reach the out of bound index starting at index 0 or 1 to reach out of bound)

        Example 1:

            Input: cost = [10, 15, 20]
            Output: 15
            Explanation: Cheapest is: start on cost[1], pay the cost, and go to the top. 

        Example 2:

            Input: cost = [1,100,1,1,1,100,1,1,100,1]
            Output: 6
            Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].

    Brute Force
    Recursion
    Decision Tree 
    O(2^n)
    O(n) linear time
        [10, 15, 20]
        starting at index 0 jump one step, pay 15, jump 2 step reached top of the floor Minimum cost : 15
        starting at index 0 jump one step, pay 15, jump 1, pay 20, jump 1 step, Minimum cost : 35
        starting at index 0 jump two step, pay 20, jump 2, Minimum cost: 20
        starting at index 1 jump two step, pay 15, Minimum cost : 15 

    Dynamic Programming 
        - solving subproblem then solve original problem
        DP = [10, 15, 20] _
               0   1   2  3


    The problem is asking to find the minimum cost to reach the top of a staircase, 
        given an array of costs for each step. You can either start at index 0 or index 1, 
        and you can either take one or two steps at a time. 
        The goal is to find the minimum cost of reaching the top of the staircase.

    To solve this problem, we can use dynamic programming to keep track of the minimum cost to reach each step 
        on the staircase. We can initialize an array dp where dp[i] represents the minimum cost to reach the i-th step.

    We can then iterate through the cost array and for each i, 
        we can calculate the minimum cost to reach that step by adding the cost of the current step to the minimum 
        of the costs to reach the previous two steps.

    The minimum cost to reach the top of the staircase will be either the minimum cost to reach the last step 
        or the second to last step, as we have the option to start at either the first or second step.
    
    
'''

class Solution:
    def MinCostClimbingStairs(self, cost: list[int]) -> int:
        
        # Return 0 if input was empty
        if not cost:
            return 0

        # create an array to memorize the results, memorize the "min cost" at the i-th step
            # filled with zeros, with a length equal to the length of the list cost.
        dp = [0] * len(cost)

        # if the length of the list cost is greater than or equal to 2. Then:
        if len(cost) >= 2:

            # sets the second element of the list dp equal to the second element of the list cost.
            dp[1] = cost[1]

        # first element of the list dp equal to the first element of the list cost.
        dp[0] = cost[0]

        # starts a for loop that iterates over a range of integers from 2 to the length of the list cost.
        for i in range(2, len(cost)):

            # sets the ith element of the list dp equal to the ith element of the list cost plus the minimum of the i-1th 
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        # returns the minimum of the last element of the list dp and the second-to-last element of the list dp.
        return min(dp[-1], dp[-2])

    # Testcases:
    l = MinCostClimbingStairs(0, [10,15,20]  )
    print(l)

    l = MinCostClimbingStairs(0, [1,100,1,1,1,100,1,1,100,1])
    print(l)


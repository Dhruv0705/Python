'''
House Robber

    You are a professional robber planning to rob houses along a street. Each house
    has a certain amount of money stashed. The only constraint stopping you from robbing
    each of them is that adjacent houses have security systems connected and it will
    automatically contact the police if two adjacent houses were broken into on the same night. 

    Given a list of non-negative integers representing the amount of money of each house, determine
    the maximum amount of money you can rob tonight without alerting the police. 

        Example 1: 
            Input : nums = [1,2,3,1]
            Output: 4
            Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3 ) 
                Total amount can be robed = 1 + 3 = 4
    
    The problem is asking to find the maximum amount of money that can be robbed from a given list of 
        non-negative integers(representing the amount of money in each house) without robbing adjacent houses 
        on the same night. The solution should return the maximum amount of money that can be robbed.

    For example, in the input [1,2,3,1], the maximum amount of money that can be robbed is 4, 
        by robbing houses 1 and 3 (which contain 1 and 3 dollars, respectively).

    This problem can be solved using dynamic programming, where we create an array to store the maximum amount of money 
        that can be robbed from each house. We start from the first house and iterate through the list, 
        updating the maximum amount of money that can be robbed at each step. At each step, 
        we have the option to either rob the current house or not rob it, and we choose the option that results 
        in the maximum amount of money.
    The runtime of the House Robber problem is O(n), where n is the number of houses. 
        This is because the algorithm iterates through the input array once, 
        and performs constant time operations on each element.


'''

class Solution1:
    def rob1(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        # Initialize an array to store the maximum amount of money
        # that can be robbed from each house up to the current house
        dp = [0] * len(nums)
        
        # Set the maximum amount of money that can be robbed from the first two houses
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        # Iterate through the remaining houses
        for i in range(2, len(nums)):

            # The maximum amount of money that can be robbed from the current house
            # is either the money in the current house plus the maximum amount of money
            # that was robbed from the previous house, or the maximum amount of money
            # that was robbed from the house before the previous one
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        # Return the maximum amount of money that can be robbed from the last house
        return dp[-1]

class Solution:
    def rob2(self, nums: list[int]) -> int:
        
        # If list is empty
        if not nums:
            return 0
        
        
        # Initialize two variables to keep track of the maximum amount of money robbed so far
        robber1, robber2 = 0 , 0

        # Loop through the list of houses
        # The idea is to keep track of the maximum amount of money robbed 
            # so far by comparing the current house with the two previous houses
        # [robber1, robber2, n, n+1, ...]
        for n in nums:

            # Save the value of robber2 in a temporary variable before updating it
            temp = max(n + robber1, robber2)

            # Update robber1 with the value of robber2
            robber1 = robber2

            # Update robber2 with the maximum value between n + robber1 and robber2
            robber2 = temp

        # Return the maximum amount of money robbed so far
        return robber2

# TestCases:
l = Solution1.rob1(0, [1,2,3,1])
print(l)
l = Solution.rob2(0, [1,2,3,1])
print(l)
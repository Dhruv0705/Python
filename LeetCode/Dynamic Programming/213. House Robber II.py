'''
House Robber II
https://leetcode.com/problems/house-robber-ii/ [Medium]

    You are a professional robber planning to rob houses along a street. 
    Each house has a certain amount of money stashed.
    All houses at this place are arranged in a circle.
    That means the first house is the neighbor of the last one.
    Meanwhile, adjacent houses have a security system connected,
    and it will automatically contact the police if two adjacent houses were broken into on the same night.


    Given an integer array nums representing the amount of money of each house, 
    return the maximum amount of money you can rob tonight without alerting the police.

        Example 1:
            Input: nums = [2,3,2]
            Output: 3
            Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

'''
# O(n) time | O(1) space
class Solution:
    def rob(self, nums: list[int]) -> int:
    
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))  
      
    def helper(self, nums):

        # Store the maximum amount of money that can be robbed from the first house
        rob1, rob2 = 0, 0

        # Loop through the remaining houses
        for n in nums:

            # Store the maximum amount of money that can be robbed from the current house
            newRob = max(rob1 + n, rob2)

            # Set rob1 to the maximum amount of money that can be robbed from the previous house
            rob1 = rob2

            # Set rob2 to the maximum amount of money that can be robbed from the current house
            rob2 = newRob

        # Return the maximum amount of money that can be robbed from the last house
        return rob2

# O(n) time | O(n) space
class Solution1:
    def rob(self, nums: list[int]) -> int:

        # If the list is empty
        if not nums:
            return 0

        # If the list contains only one house
        if len(nums) == 1:
            return nums[0]

        # If the list contains only two houses
        if len(nums) == 2:
            return max(nums[0], nums[1])

        # Initialize an array to store the maximum amount of money
        # that can be robbed from each house up to the current house
        dp = [0] * len(nums)

        # Set the maximum amount of money that can be robbed from the first two houses
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # Iterate through the remaining houses
        for i in range(2, len(nums) - 1):

            # The maximum amount of money that can be robbed from the current house
            # is either the money in the current house plus the maximum amount of money
            # that was robbed from the previous house, or the maximum amount of money
            # that was robbed from the house before the previous one
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        # Return the maximum amount of money that can be robbed from the last house
        return dp[-2]

    l = rob(0, [2,3,2])
    print(l)

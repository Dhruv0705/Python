'''

Maximum Subarray [http://] [Easy]

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:

    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

    Input: nums = [1]
    Output: 1


'''

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
            
        # Initialize the maxSum to the first element in the array
        maxSum = nums[0]
        
        # Initialize the currentSum to the first element in the array
        currentSum = 0
        
        # Loop through each number in the array
        for i in nums:

            # If the currentSum is less than 0, set it to 0
            if currentSum < 0:
                currentSum = 0
            
            # Add the current number to the currentSum
            currentSum += i

            # If the currentSum is greater than the maxSum, set the maxSum to the currentSum
            maxSum = max(maxSum, currentSum)
        
        # Return the maxSum
        return maxSum
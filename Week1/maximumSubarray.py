class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        windowSum = nums[0]
        maxSum = nums[0]
        
        for i in range(1,len(nums)):
            windowSum = max(windowSum+nums[i], nums[i])
            maxSum = max(windowSum, maxSum)
        return maxSum
    
"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
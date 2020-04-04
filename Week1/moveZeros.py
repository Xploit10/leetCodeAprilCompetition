class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        count = 0
        for index in range(length):
            if nums[index] != 0:
                nums[count] = nums[index]
                count += 1
        for i in range(count, length):
            nums[i] = 0
"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
"""
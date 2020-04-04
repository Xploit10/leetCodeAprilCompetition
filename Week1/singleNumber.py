class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        for num in nums:
            x ^= num
        return x
    
"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Input: [2,2,1]
Output: 1

Input: [4,1,2,1,2]
Output: 4
"""
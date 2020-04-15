class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        for index in range(len(arr)):
            total_elements = arr[index] + 1
            for i in arr:
                if total_elements == i:
                    count += 1
                    break

        return count

"""
Given an integer array arr, count element x such that x + 1 is also in arr.

If there're duplicates in arr, count them seperately.

Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.

"""
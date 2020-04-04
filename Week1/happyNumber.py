class Solution:
    def isHappy(self, n: int) -> bool:
        def multiply(n):
            arr = [x for x in str(n)]
            temp = 0
            for i in arr:
                temp += int(i)*int(i)
            if temp == 1:
                return 1
            else:
                return temp
        seen = set()
        p = n
        while 1:
            p = multiply(p)
            if p == 1:
                return True
            elif p in seen:
                return False
            else:
                seen.add(p)
                continue
"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, 
replace the number by the sum of the squares of its digits, and repeat the process until the 
number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""
            
           
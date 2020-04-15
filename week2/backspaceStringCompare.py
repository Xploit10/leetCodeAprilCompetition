class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def check_equal(array):
            stack = []
            length = len(array)
            for index in range(length):
                if array[index] == '#':
                    if len(stack) > 0:
                        stack.pop()
                else:
                    stack.append(array[index])
            print(stack)
            return stack
        if check_equal(S) == check_equal(T):
            return True
        return False

"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
"""
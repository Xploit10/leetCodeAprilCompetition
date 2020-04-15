class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0 
        for index in range(1, len(prices)):
            if prices[index] > prices[index - 1]:
                diff += prices[index] - prices[index -1]
        return diff

"""
Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Input: [7,1,5,3,6,4]
Output: 7

"""
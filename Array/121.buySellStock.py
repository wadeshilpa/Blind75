# Easy
# Best Time to Buy and Sell Stock
# Array / single-pass greedy

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day 
# in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Input: prices = [7,1,5,3,6,4]             Output: 5
# Input: prices = [7,6,4,3,1]               Output: 0
# Input: prices = [1, 2, 3, 4, 5]           Output: 4
# Input: prices = [0]                       Output: 0
# Input: prices = [5,5,5,5,5]               Output: 0
# Input: prices = [3, 2, 6, 5, 0, 3]        Output: 4

# Edge cases        : empty, single, increasing, decreasing, duplicates, ups downs
# Time Complexity   : O(n) → single pass through prices
# Space complexity  : O(1) → only a few variables used
# Best case         : O(n) (must still check all prices, even if sorted)
# Worst Case        : O(n) (always one pass, regardless of values)
########################################################################
class Solution:
    def buySellStock(self, prices:list[int])->int:
        if not prices or len(prices) < 2:
            return 0
        
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            if price < min_price:
                min_price = price

            max_profit = max(max_profit, price - min_price) 

        return max_profit
    
if __name__ == '__main__':
    prices = list(map(int,input("enter prices array = ").split(",")))
    print(Solution().buySellStock(prices))

# Difficulty : Easy
# Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Input: prices = [7,1,5,3,6,4]                 Output: 5
# Input: prices = [7,6,4,3,1]                   Output: 0
# Input: prices = [3, 3, 5, 0, 0, 3, 1, 4]      Output: 4
# Input: prices = [5, 11, 2, 11]                Output: 9

# Edge cases : empty list, single element, same elements
# Time Complexity : O(n)
# Space Complexity : O(1)
# Best case : When input is sorted in asc order
# Worst case : When input is sorted in desc order

class Solution:
    def MaxProfit(self,prices:list[int])->int:
        buy_price=prices[0]
        profit=0

        for p in prices[1:]:
            if p < buy_price:
                buy_price=p

            current_profit=p-buy_price
            profit=max(profit,current_profit)

        return profit
    
if __name__=='__main__':
    try:
        prices=list(map(int,input("Enter prices separated by comma : ").split(',')))
        result=Solution().MaxProfit(prices)
        print(result)
    except ValueError:
        print("Invalid input")

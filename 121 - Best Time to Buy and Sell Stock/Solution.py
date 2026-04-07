"""
Solution for LeetCode #121 - 'Best Time to Buy and Sell Stock'

Time Complexity:  O(n)
Space Complexity: O(1)
"""
class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    res, buy = 0, prices[0]

    for sell in prices:
      buy = min(buy, sell)
      res = max(res, sell - buy)

    return res

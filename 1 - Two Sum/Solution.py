"""
Solution for LeetCode #1 - 'Two Sum'

Time Complexity:  O(n)
Space Complexity: O(n)
"""
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    mp = {}

    for i, n in enumerate(nums):
      diff = target - n
      if n in mp:
        return [mp[n], i]
      mp[diff] = i

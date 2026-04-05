"""
Solution for LeetCode #20 - 'Valid Parantheses'

Time Complexity:  O(n)
Space Complexity: O(n)
"""
class Solution:
  def isValid(self, s: str) -> bool:
    stack = []

    for c in s:
      if c == '(' or c == '[' or c == '{':
        stack.append(c)
        continue

      if not stack:
        return False

      top = stack.pop()
      if (c == ')' and top != '(') or (c == ']' and top != '[') or (c == '}' and top != '{'):
        return False

    return not stack

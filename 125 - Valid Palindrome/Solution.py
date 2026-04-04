"""
Solutions for LeetCode #125 - 'Valid Palindrome'
"""

"""
Soluition 1: Reconstruct String

Time Complexity:  O(n)
Space Complexity: O(n)
"""
class Solution1:
  def isPalindrome(self, s: str) -> bool:
    s = "".join(c for c in s.lower() if c.isalnum())

    l, r = 0, len(s) - 1
    while l < r:
      if s[l] != s[r]:
        return False
      l += 1
      r -= 1

    return True


"""
Soluition 2: No String Reconstruction

Time Complexity:  O(n)
Space Complexity: O(1)
"""
class Solution2:
  def isPalindrome(self, s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
      while l < r and not s[l].isalnum():
        l += 1
      while l < r and not s[r].isalnum():
        r -= 1
        
      if s[l].lower() != s[r].lower():
        return False
      l += 1
      r -= 1

    return True

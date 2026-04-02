"""
Solutions for LeetCode #242 - 'Valid Anagram'
"""

"""
Solution 1: Two hashmaps, two loops

Time Complexity:  O(2n) ≈ O(n)
Space Complexity: O(2n) ≈ O(n)
"""
class Solution1:
  def validAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False

    mp_s, mp_t = {}, {}

    for c in s:
      mp_s[c] = mp_s.get(c, 0) + 1
    for c in t:
      mp_t[c] = mp_t.get(c, 0) + 1

    return mp_s == mp_t


"""
Solution 2: One hashmap, two loops

Time Complexity:  O(2n) ≈ O(n)
Space Complexity: O(n)
"""
class Solution2:
  def validAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False

    mp = {}
    
    for c in s:
      mp[c] = mp.get(c, 0) + 1
      
    for c in t:
      if c not in mp:
        return False

      mp[c] -= 1
      
      if mp[c] == 0:
        del mp[c]

    return not mp


"""
Solution 3: One hashmap, One loop

Time Complexity:  O(n)
Space Complexity: O(n)
"""
class Solution3:
  def validAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False

    mp = {}
    
    for i in range(len(s)):
      c_s, c_t = s[i], t[i]

      mp[c_s] = mp.get(c_s, 0) + 1
      mp[c_t] = mp.get(c_t, 0) - 1

      if mp[c_s] == 0:
        del mp[c_s]
      if c_t in mp and mp[c_t] == 0:
        del mp[c_t]

    return not mp

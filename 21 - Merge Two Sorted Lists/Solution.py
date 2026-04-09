"""
Solution for LeetCode #21 - 'Merge Two Sorted Lists'

Time Complexity:  O(n + m)
Space Complexity: O(n + m)
Where n and m are the lengths of list1 and list2 respectively.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = nex

class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1:
      return list2
    if not list2:
      return list1

    if list1.val < list2.val:
      list1.next = self.mergeTwoLists(list1.next, list2)
      return list1
    list2.next = self.mergeTwoLists(list1, list2.next)
    return list2

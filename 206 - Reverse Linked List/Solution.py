"""
Solution for LeetCode #206 - 'Reverse Linked List'

Time Complexity:  O(n)
Space Complexity: O(n)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = nex

class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def helper(head: Optional[ListNode], prev: Optional[ListNode]) -> Optional[ListNode]:
      if not head:
        return prev

      next = head.next
      head.next = prev
      return helper(next, head)

    return helper(head, None)

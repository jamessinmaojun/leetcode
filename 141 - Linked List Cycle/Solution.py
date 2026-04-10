"""
Solution for LeetCode #141 - 'Linked List Cycle'

Time Complexity:  O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = nex

class Solution:
  def reverseList(self, head: Optional[ListNode]) -> bool:
    slow, fast = head, head

    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

      if slow == fast:
        return True

    return False

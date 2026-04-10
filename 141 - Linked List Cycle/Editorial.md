# 141. Linked List Cycle - Editorial

### Intuition

On first glance, this problem might seem trivial, since we could store visited nodes in a hashmap and easily check if a subsequent node has already been encountered.
If so, we can return `true` immediately.

However, this solution requires linear space, surely we can do better?

Introducing *[Floyd's Cycle Algorith](https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_tortoise_and_hare)*, or the *Toirtoise and Hare Algorithm*, which is specially used for detecting cycles in a sequence of nodes, perfect for our use case here.

This algorithm traverses the linked list with two pointers, with one pointer moving at twice the speed of the other (hence the name "Tortoise and Hare", which refer to the slow and fast pointers respectively).
The idea is that if there exists a cycle within the linked list, the fast pointer will eventually catch up with the slow pointer, since the fast pointer would have already reached the end of the linked list had there been no cycle.

### Solution

As discussed, we first initialise our slow and fast pointers.
```py
slow, fast = head, head
```
We then set up our loop, which we will use to advance the pointers.
Note that we have to check for both `fast` and `fast.next`, since we are advancing the `fast` pointer two nodes at once.
```py
while fast and fast.next:
```
We then advance our pointers.
The slow pointer moves one node at a time, while the fast pointer skips a node.
```py
  slow = slow.next
  fast = fast.next.next # Moves at twice the speed of the slow pointer
```
We then check if the two pointers point back to the same node after advancing.
If so, we have found a cycle, and can return `true` immediately.
```py
  if slow == fast:
    return True
```
Finally, if the algorithm exits the loop, we know that the fast pointer has reached the end of the list.
We can then conclude that there is no cycle and return `false`.
```py
  return False
```

### Complexity Analysis

Since we are traversing every node of the linked list, our time complexity is linear.

Since we are only using two additional variables regardless of the length of the linked list, our space complexity is constant.

# 206. Reverse Linked List - Editorial

### Intuition

This problem introduces us to the *Linked List* data structure, which is defined as follows:
```py
class LinkedListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
```

Intuitively, reversing a linked list entails reversing the directions of all links between nodes.
That is, every node now points at the **previous** node instead of the following node.

From this, we should be able to guess that we need to be able to keep track of all previous nodes in addition to the current node.
That way, we will be able to redirect the outgoing link of the current node to point towards the previous node instead of the following node.

### Solution

We approach this problem by traversing the linked list node by node via **recursion**.
Note that this problem may also be solved iteratively with a loop.
However, for the purposes of this solution, we will use recursion.

Before we start, since the signature of the provided function does not include a parameter to keep track of previous nodes (in addition to the current node, or the *head*), we will define a helper function ourselves as follows:
```py
def helper(head: Optional[LinkedListNode], prev: Optional[LinkedListNode]) -> Optional[LinkedListNode]:
```

Within the helper function, we first check if the current node is `null`.
If so, we know that we either have:
- an empty list to begin with, or;
- reached the last node of the list, which happens to be the head of the reversed linked list.

In either case, this is our terminating condition, and we return the previous node.
```py
  if not head:
    return prev
```
If we have cleared the terminating conditional guard clause, we know that we are somewhere in the middle or at the start of the list.
For each node of the linked list, we want to redirect its outgoing link to point towards the previous node rather than the following node.
To do so, we first initialise a variable `next` to keep track of the original following node.
```py
  next = head
```
We then redirect the outgoing link of the current node to point to the previous node.
```py
  head.next = prev
```
Finally, we then call the helper function recursively, this time updating its arguments with the new head as the following node, and the new previous node as the current node.
```py
  return helper(next, head)
```
Within the main function, we make the first call to the helper function with a `null` previous node.
This will point the current head (the new tail of the reverse linked list) to `null`, which is the required terminating flag of a linked list.
```py
return helper(head, None)
```

### Complexity Analysis

Since we are traversing every node of the linked list, our time complexity is linear.

Since we are making `n` recursive calls, where `n` is the number of elements in the linked list, our call stack could potentially contain up to `n` function calls and hence our space complexity is also linear.

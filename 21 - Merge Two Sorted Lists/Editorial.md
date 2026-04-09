# 206. Reverse Linked List - Editorial

### Intuition

In this problem, we are tasked to merge two **already sorted** linked lists in ascending order into a **single sorted list**.

This implies that we will have to do a **node-wise comparison** across both lists, which also means an exhaustive traversal of both lists, at least up till the length of the shorter list.

### Solution

For the purposes of this solution, we will be traversing the linked lists via **recursion**.
Note that this problem may also be solved iteratively with a loop.

We first define the exit conditions of our recursive function, which will be executed when we have reached the last node of one or both of the lists.
```py
if not list1:
  return list2
if not list2:
  return list1
```
Note that we do not need to check if we have reached the end of both lists, i.e. we do not need to run the following guard clause:
```py
if not list1 and not list2:
  return None
```
For example, looking at the first guard clause, if we have reached the end of `list1`, then we would return `list2`.
Even if we have also reached the end of `list2`, we would be returning it anyway.
Therefore we can do not need an additional clause to check for the end of both lists.

Next, we move on to the node-wise comparison.

First, we check if the current value of the the haed of `list1` is smaller than the current value of the head of `list2`.
```py
if list1.val < list2.val:
```
If so, we set the outgoing pointer of the current head of `list1` to point towards the next node of the merged list, which will be returned by a recursive call to our function.
Take special notice of the arguments passed to the recursive function call; in this case we are passing the next node of `list1` into the recursive function call, since we are extracting and returning the current head of `list1` separately.
```py
  list1.next = self.mergeTwoLists(list1.next, list2) # Take note of the first argument
```
We then return the head of `list1` as the head of the current sublist.
We need to do this as the function requires us to return the head of the newly merged list.
This returned head may also be the head of a sublist, which is the result that will be used by preceding recursive function calls.
```py
  return list1
```
Note that this method of assuming that the recursive function call will return us the accumulated result we need is called *wishful thinking*, which is a core principle of recursion.

If we got past the previous guard clause, we know that the value of the head of `list2` is less than or equal to the value of the head of `list1`, and so we repeat the linking steps.
```py
list2.next = self.mergeTwoLists(list1, list2.next)
return list2
```

### Complexity Analysis

Since we are traversing every node of both linked lists, our time complexity is linear.

Since we are potentially making `n + m` recursive calls in the worst case, where `n` and `m` are the number of elements in both linked lists respectively, our call stack could potentially contain up to `n + m` function calls. Hence, our space complexity is also linear.

# 704. Binary Search - Editorial

### Intuition

This problem actually tells us the algorithm to use in its title—*Binary Search*.

In this editorial, we will be using the standard version of Binary Search.
Other versions, such as the Upper Bound and Lower Bound Binary Searches exist.
However, they are out of the scope of this question and will be introduced later in other, more specific questions where they are required.

So, what is the Binary Search algorithm, and how does it work?

Performing a Binary Search allows us to locate elements (if they exist) in array-like data structures in logarithmic time, as compared to a trivial linear search.
However, there is an important caveat—the array that we are searching on **must be sorted**.

Binary Search leverages the fact that the array is sorted to iteratively narrow down the search space for a certain element, until the search space converges.
This allows the searching algorithm to search more efficiently, skipping the ranges of the array where the target element will never be found anyway.

### Solution

The idea here is to continually compare the element at the **middle index** of the current active search range with the target element, and then narrow down the active search range based on the results of the comparison.

If the middle element is larger than the target element, we can be sure that the element lies in the range from right after the middle element to the last element of the active search range.

If the middle element is smaller than the target element, we can be sure that the element lies in the range from the first element of the active search range to right before the middle element.

If the middle element is equal to the target element, then we have found our solution and can return the middle index immediately.

To keep track of the active search range, we will initialise two pointers, one pointing to the start of the range and one to the end.
```py
l, r = 0, len(nums) - 1
```
Next, we run a loop which will continue to run until the start pointer exceeds the end pointer.
Take special notice of the `<=` sign.
The equal sign is required because we could end up in a situation where both the left and right pointers are pointing to the same index, and the index in question happens to be the one that we are looking for.
```py
while l <= r: # Note the equal sign
```
In each iteration, we first compute the middle index and the element corresponding to it.
Take extra attention to the way are are calculating the middle index.
```py
  m = l + (r - l) // 2 # Note the method of calculating the middle index here
  curr = nums[m]
```
We compute the middle index this way (instead of the usual `(l + r) // 2`) because we want to avoid adding the start and end pointers.
This is to avoid integer overflow (if we are using other languages) which can potentially occur if the values of the start and end pointers are large enough.

Next, we perform a series of comparisons between the middle element and the target element.

First, we check if the target element is smaller than the middle element.
If so, this means that the target element is somewhere in the range to the left of the middle element, hence we reduce the search space by setting the end pointer to the index right before the middle index.
```py
  if target < curr:
    r = m - 1
```
Next, we check if the target element is larger than the middle element.
If so, this means that the target element is somewhere in the range to the right of the middle element, hence we reduce the search space by setting the start pointer to the index right after the middle index.
```py
  elif target > curr:
    l = m + 1
```
If we have arrived at this block we know that we have located the target element, since the middle element is neither larger than nor smaller than the target element.
We can hence return the middle index immediately.
```py
  else:
    return m
```
Finally, the question specifies that if the target element cannot be found, we should return `-1`.
By the time the loop has terminated, we would have exhausted the search space of the entire array due to the algorithm's converging nature.

We can then hence be confident that if the loop had completed, the array does not contain the target element and we can return a negative result immediately.
```py
return -1
```

### Complexity Analysis

As discussed above, since the algorithm repeatedly cuts the search space in half, our time complexity is logarithmic.

Since we are not memoising any part of the array in our solution, our space complexity is constant.

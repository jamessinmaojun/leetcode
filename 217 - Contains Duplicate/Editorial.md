# 217. Contains Duplicate - Editorial

### Intuition

This problem teaches us how to use a specific data structure - the *Set*.

We know that we have to use a set because of a core requirement of the problem - to return `true` if we encounter an element that we have **already seen before**.
This means that ideally, we would want a data structure that can store only **unique instances** of each element, and that is a Set!

### Solution

The general idea is simple:


First, we initialise a set.
```py
s = set()
```
Then, we systematically go through every element in the array.
```py
for n in nums:
```
If the set already contains that element, we simply return `true`, as we have identified a duplicate element!
```py
  if n in s:
    return True
```
Else we add the element into the set, and move on to the next element.
```py
  s.add(n)
```
Finally, if the loop completes and we still have not returned, we know that we were able to add every element into the set.
This means that the given array did not contain any duplicates, and that we are safe to return `false`.
```py
return False
```

### Complexity Analysis

Since the solution involves looping through the given array, our time complexity is linear.
Since we are storing all elements of the given array in a set in the worst case, our space complexity is also linear.

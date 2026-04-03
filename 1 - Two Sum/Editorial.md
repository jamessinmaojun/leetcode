# 1. Two Sums - Editorial

### Intuition

This problem teaches us how to use a specific data structure - the *Hashmap*.


Let us first analyse the problem and think of how to approach it trivially.


Intuitively, we know that if we perform a brute force search, we will be able to compare all possible combinations and hence derive the answer.


However, since we are comparing two numbers in this question, an exhaustive search in this case will require a doubly-nested loop.
This is inefficient as the amortised time complexity of a nested loop would be quadratic.


Are we able to solve this question in one pass?


To solve this question with a single loop, we need to find some way to compare the currently encountered number with the other numbers of the array, **as we loop through the array**.
Note at any point in time, we will only be able to compare the current number with the numbers that we have **already encountered** (since we have not seen the rest of the numbers yet).


So how can we compare the numbers we have already seen as we go through the array?


The solution is to **keep track of all the numbers we have previously encountered** in some data structure. This way, as we are looping through the array, we can simply compare the current number with our data structure.


How then do know that we have to use a hashmap?


To get there, we need to identify a key condition of the question: The question is asking for two numbers that **add up to `target`**.


What this means is that when we are comparing our current number with the data structure, we are actually performing a lookup to check if *something* in relation to our current number exists in the data structure.


This "something" in this question would be the **difference** between the current number and the target.
Since we are performing lookups, the most efficient data structure for performing fast lookups would be one that allows for key-value pairs.


That would be the hashmap.


In this case, the keys would be the differences between each of the numbers in the array and the target, and the values would be the respective indices of the numbers ih the array.

### Solution

The general idea is simple. We first construct a hashmap, then perform a single loop through the input array, checking at each iteration if the current number encountered exists in the hashmap as the target difference to another number that has already been encountered.


First, we initialise our hashmap.
```py
mp = {}
```
Then, we systematically go through every number in the array. Do note that we have to extract the indices as well due to the question requirement of returning indices and not the actual elements in the answer.
```py
for i, n in enumerate(nums):
```
In each iteration, we check if the current number exists as a key in the hashmap. If the hashmap contains the current number, we simply return the value of the key in the hashmap corresponding to the current number, as well the current index.
```py
  if n in mp:
    return [mp[n], i]
```
Else we compute the difference between the target and the current number, and add the difference into the hashmap with the current index as the key.
```py
  diff = target - n
  mp[diff] = i
```
Given that there is guaranteed to be a solution, our solution ends here as the `return` statement within the `for` loop will definitely execute.

### Complexity Analysis

Since the solution involves looping through the given array, our time complexity is linear.
Since we are storing all elements of the given array in a hashmap in the worst case, our space complexity is also linear.

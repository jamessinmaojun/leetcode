# 125. Valid Palindrome - Editorial

### Intuition

This problem requires us to check if a given string is a palindrome, **after stripping all non-alphanumeric characters and ignoring case sensitivity**.

To key to solving this question is in the definition of a palindrome.
A palindrome reads the same forwards and backwards.

Now imagine "folding" a palindromic string into half onto itself, such that the last letter is now perfectly stacked on top of the first letter.
What do we notice?

If we go through the stacked letters one by one, we realise that letters that are vertically aligned are the same!

This leads us to the invariant of our solution: as long as the given string is a palindrome, "vertically aligned" letters will always be the same.

### Solution 1

How can we translate this "vertical stacking" idea into code? Let us introduce the *Two Pointer* technique!

Recall that the question instructs us to ignore case-sensitivity and all non-alphanumeric characters. We hence need to first clean the input string to meet this requirement.
```py
s = "".join(c for c in s.lower() if c.isalnum())
```
Next, we initialise two pointers. The left pointer should point to the start of the string (position `0`), while the right pointer should point to the end of the string (position `len(s) - 1`).
```py
l, r = 0, len(s) - 1
```
Next, we need to find some way to move the left and right pointers towards each other, while simultaneously ensuring that they **do not cross**. We can achieve this with a while loop.
```py
while l < r: # ensure that the pointers do not cross each other
```
Inside the loop, we first check if the two letters corresponding to the left and right pointers are equal. According to our invariant, if "stacked" letters are not the same, we can conclude that the string is not a valid palindrome.
```py
  if s[l] != s[r]:
    return False
```
For every valid pair of "stacked" letters, we need to move the left and right pointers towards each other.
```py
  l += 1
  r -= 1
```
Finally, the loop manages to complete, we are certain that the string is palindromic, and we can return a positive result.
```py
return True
```

### Solution 1 Complexity Analysis

Since we are processing every letter of the input string exactly once, our time complexity is linear.

Since we are constructing a new filtered string at the start of our solution, our space complexity is also linear.

Can we do better?

### Improvement - Reducing Space Complexity

Notice how we are constructing another string just to ensure that our input string meets the filtering criteria.

Instead of creating a whole new filtered string, we can simply convert individual characters to lowercase, and check for non-alphanumeric characters in-place for each iteration of the while loop!

With this improvement, we no longer need to construct a filtered string at the start of our solution. We can immediately initialise the two pointers and begin our loop.
```py
l, r = 0, len(s) - 1
while l < r:
```
However, since we no longer have a filtered string, we have to check for non-alphanumeric characters in-place, and progress the pointers accordingly until we encounter an alphanumeric character.
```py
  while l < r and not s[l].isalnum():
    l += 1
  while l < r and not s[r].isalnum():
    r -= 1
```
Note that we also have to check that the pointers do not cross within the inner while loops to avoid accidental crossing of pointers.

Next, we also need to make a slight modification to the pairwise equality check for characters. The question requires us to be case-insensitive, so we have to convert characters to lowercase individually.
```py
  if s[l].lower() != s[r].lower():
    return False
```
Just like before, we shift the pointers towards each other at the end of every iteration of the outer while loop.
```py
  l += 1
  r -= 1
```
Finally, just like the first solution, if our loops manage to complete, then our string is palindromic and we can return a positive result.
```
return True
```

### Solution 2 Complexity Analysis

Since we still have to process each character of the input string, our time complexity remains linear. Although there is a slight improvement as constructing the filtered string in the first solution is also linear.


However, in this solution we are no longer constructing an additional filtered string. Hence our space complexity is now constant.

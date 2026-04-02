# 242. Valid Anagram - Editorial

### Intuition

This problem involves comparing two strings `a` and `t` and checking if they are permutations of each other (an anagram).

Intuitively, we can do this by keeping track of the frequencies of the characters that appear in each of the strings by constructing *frequency tables* and checking if the frequency tables for each of the strings are identical.

### Solution 1

The general idea is simple:


First, we check for the edge case where the two strings are not of the same length. In this case, we can return `false` immediately as trivially, strings of different lengths are not anagrams of each other.
```py
if len(s) != len(t):
  return False
```
Then, we initialise two dictionaries, one for each of the input strings.
```py
mp_s, mp_t = {}, {}
```
Next, we construct the frequency tables for each of the input strings by looping through them one at a time and counting the number of occurrences of each character.
```py
for c in s:
  mp_s[c] = mp_s.get(c, 0) + 1

for c in t:
  mp_t[c] = mp_t.get(c, 0) + 1
```
Finally, we compare both frequency tables for equality. If the frequency tables are identical, then the two input strings are valid anagrams of each other.
```py
return mp_s == mp_t
```

### Solution 1 Complexity Analysis

Since the solution involves looping through the given strings, our time complexity is linear.
Since the number of elements in our frequency tables depend on the lengths of the input strings, our space complexity is also linear.


However, do note that since we are initialising two hashmaps, and looping through each string individually, the actual time and space complexities are `O(2n)`.


Can we do better?

### Improvement 1 - Reducing Space Complexity

Notice how we are constructing two frequency tables, one for each string.
Also notice how at the end of the solution, we are checking for equality of the two frequency tables.


This leads to a subtle but interesting observation: if we 'subtract' one frequency table from the other, what do we get?


Instead of checking for equality of two frequency tables, we can simply check if the **difference** between the two frequency tables is an empty table. If the resulting table is empty, then the two strings are anagrams of each other!


From this observation, we can reduce the number of frequency tables to just one by making a slight modification:
```py
for c in t:
  mp_t[c] = mp_t.get(c, 0) - 1
```
By **decrementing** the frequency count when looping through the second string `t`, we are achieving the same effect as *subtracting* the second frequency table from the first!

### Solution 2 - Single Hashmap

We need to introduce some other modifications for this solution to work. The first step for checking string length equality remains the same.
```py
if len(s) != len(t):
  return False
```
As discussed, we will only initialise one dictionary this time.
```py
mp = {}
```
As before, we loop through both strings one at a time. However this time we apply the modification where we **decrement** the character count when looping through `t`.
```py
for c in s:
  mp[c] = mp.get(c, 0) + 1

for c in t:
  mp[c] = mp.get(c, 0) - 1
```
Next, since we will be checking for an empty dictionary at the end of the solution, we need to delete keys that have zero counts from the dictionary.
```py
  if mp[t] == 0:
    del mp[t]
```
Finally, we check if the resulting dictionary is empty.
```py
return not mp
```

### Solution 2 Complexity Analysis

Since we are still looping through each of the strings indivually, there is no change to the time complexity.


However, for this solution we are only using one hashmap, hence our space complexity is reduced by the constant factor of 2. Note that amortally, we still reduce the constant factor anyway, so this is just a small improvement.


That being said, we are still looping through the two strings indivually, can we reduce that to a single loop?

### Improvement 2 - Reducing Time Complexity

Notice how our previous solution is still performing operations on the hashmap one string at a time. We know that the two strings are of the same length, so can we perform all operations on the hashmap within the same loop?

### Solution 3 - Single Hashmap, One Pass

Recall that in order to perform the hashmap operations within a single loop, the two strings must first be of the same length. As such the initial check for length equality remains.
```py
if len(s) != len(t):
  return False
```
From the previous improvement, we retain the single dictionary initialisation.
```py
mp = {}
```
However, now we only perform one loop. Note that we have to use index looping now instead of a `for ... in` loop. We perform both the incrementing and decrementing of frequency counts within this loop.
```py
for i in range(len(s)):
  c_s, c_t = s[i], t[i]

  mp[c_s] = mp.get(c_s, 0) + 1
  mp[c_t] = mp.get(c_t, 0) - 1
```
As before, we need to make sure that all keys with zero counts are removed from the dictionary.
However this time we need to check for both keys `c_s` and `c_t`.
Also note that since there is a possibility that `c_s` and `c_t` are equal at a particular index, we need to additionally check that `c_t` still exists as a key in our dictionary, as it would have already been deleted if `c_s` and `c_t` were the same character.
```py
  if mp[c_s] == 0:
    del mp[c_s]

  if c_t in mp and mp[c_t] == 0: # Check if c_t is still in mp
    del mp[c_t]
```
Finally, we check if the resulting dictionary is empty.
```py
return not mp
```

### Solution 3 Complexity Analysis

In this solution, we only used one loop and one hashmap. As such, the time and space complexities are both `O(n)`.

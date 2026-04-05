# 20. Valid Parantheses - Editorial

### Intuition

This problem teaches us how to use a specific data structure - the *stack*.

How do we know that we need to use a stack?

From the second requirement of the definition of a valid arrangement of parantheses,

> *"Open brackets must be closed in the **correct order**."*

we know that the **most recently opened** bracket needs to be closed first.

This is exactly what a stack does! The stack is a LIFO data structure, which is exactly what we need—the last opening bracket to appear should be closed first.
  
### Solution

We will use a stack to keep track of all the opening brackets. That is, every time we encounter an opening bracket, we simply push it onto the stack.

Whenever we encounter a closing bracket, we check if the most recently opened bracket corresponds to it. If so, we pop the opening bracket from the stack. This keeps track of matching brackets and ensures correct ordering.

What if we encounter a closing bracket, but the stack is empty?

This means that we have encountered a string (or substring) that starts with an opening bracket!
This is an invalid arrangement of parantheses and hence a key invariant of a valid input string is that we will never encounter a situation where our stack starts with a closing bracket.
That is, for a valid input string, we will never encounter a closing bracket if the stack is empty.

First, we initialise our stack.
```py
stack = []
```
Then, we loop through the string and first check if the current character is an opening bracket. If it is then we simply push the current character onto the stack and move on to the next character.
```py
for c in s:
  if c == '(' or c == '[' or c == '{':
    stack.append(c)
    continue
```
If we made it past our opening bracket guard clause, we can be confident that the current character `c` is a closing bracket, since the question constraints indicate that the input string `s` only contains the six parantheses characters.
Per our key invariant as discussed earlier, we will never end up with a situation where our stack starts with a closing bracket for any valid string.
Therefore, should we encounter an empty stack with an incoming closing bracket character, we can conclude that the input string is not a valid arrangement of parantheses and return immediately.
```py
  if not stack:
    return False
```
Next, we pop the top element from our stack and check if the top character bracket matches that of the incoming character. If it is not a match, we have found an invalid arrangement of brackets and hence can return immediately.
```py
  top = stack.pop()

  if (c == ')' and top != '(') or (c == ']' and top != '[') or (c == '}' and top != '{'):
    return False
```
Finally, even if the loop manages to complete, we still need to check if our stack is empty. This is to catch edge cases with double brackets such as `'(()'`, which will complete the loop but end up with a single `'('` character in the stack at the end of the loop execution.
```py
return not stack
```

### Complexity Analysis

Since the solution involves looping through the given array, our time complexity is linear.

Since we are storing all elements of the given array in a stack in the worst case, our space complexity is also linear.

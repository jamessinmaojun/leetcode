 # 226. Invert Binary Tree - Editorial

### Intuition

This problem introduces us to the *Binary Tree* data structure, which is defined as follows:
```py
class BinaryTreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
```

Before we think about how to solve this problem, we first need to understand what *inverting* a binary tree means.

Put simply, inverting a binary tree basically means swapping all the left and right children.
This means that for every node in the tree, its left child will become its right child, and vice versa.

Since we have to perform this swapping operation for every single node in the tree at every level, we need to find some way to traverse the tree nodes.

### Solution

In general, there are two fundamental algorithms for exploring trees, [Breadth First Search](https://en.wikipedia.org/wiki/Breadth-first_search) and [Depth First Search](https://en.wikipedia.org/wiki/Depth-first_search).
BFS is implemented iteratively with a queue, while DFS can either be implemented iteratively with a stack or recursively.
For the purposes of this solution, we will be using **recursive DFS**.

We first implement our terminating condition.
The algorithm should terminate when we have reached a leaf node.
In other words, we check if the current node is `null`.
```py
if not root:
  return None
```
If we have cleared the terminating conditional guard clause, we know that the we are at a valid tree node.
We can now perform the swapping operation by assigning the left subtree as the right child of the current node, and vice versa.
Note that as with all recursive algorithms, we will apply *wishful thinking* here.
That is, we assume that subsequent recursive calls to our function will return correctly inverted subtress.
```py
  left, right = root.left, root.right # Create temporary variables to store original left and right subtrees
  root.left = self.invertTree(right)
  root.right = self.invertTree(left)
```
Also note how we initialise two temporary variables to store the current node's original left and right subtrees.
We need to do this since we are reassigning the left subtree in the next line, which will implicate the following line since without temporary variables, we would be using the mutated left subtree instead of the original left subtree.

Finally, we return the current tree node, which would either be returned to a preceding recursive call as an intermediary result, or as the root node of our new inverted tree if this is the first function call.
```py
  return root
```

### Complexity Analysis

Since we are traversing every node of the binary tree, our time complexity is linear.

Since we are making `n` recursive calls, where `n` is the number of elements in the binary tree, our call stack would contain `n` function calls and hence our space complexity is also linear.

# Advanced Data Structures

This repository contains implementations of three advanced data structures in Python:

## Red-Black Tree

A self-balancing binary search tree that maintains balance through node coloring:

- Every node is either red or black
- Root is black
- No two adjacent red nodes
- Every path from root to leaf has same number of black nodes

Operations:

- `insert(data)`: Insert new data
- `read(data)`: Check if data exists
- `delete(data)`: Remove data

## XOR Linked List

A memory-efficient doubly linked list that uses XOR of addresses to store both previous and next pointers in a single field:

- Uses single pointer field to store both next and previous node addresses
- Requires careful memory management
- Saves memory by storing two pointers in space of one

Operations:

- `insert(data, position=None)`: Insert at end, beginning, or specific position
- `read(position)`: Read data at position
- `delete(position)`: Delete node at position

## B-tree

A self-balancing tree data structure that maintains sorted data and is optimized for systems that read and write large blocks of data:

- Every node has at most m children
- Non-leaf nodes (except root) have at least ⌈m/2⌉ children
- All leaves appear at same level
- Optimized for disk operations

Operations:

- `insert(key)`: Insert new key
- `read(key)`: Search for key
- `delete(key)`: Remove key

## Usage

```python
from data_structures import RedBlackTree, XORLinkedList, BTree

# Red-Black Tree
rbt = RedBlackTree()
rbt.insert(5)
rbt.read(5)  # Returns True
rbt.delete(5)

# XOR Linked List
xll = XORLinkedList()
xll.insert(1)  # Insert at end
xll.insert(2, 0)  # Insert at beginning
xll.read(0)  # Returns 2
xll.delete(0)  # Removes and returns 2

# B-tree (t is minimum degree)
bt = BTree(t=3)
bt.insert(5)
bt.read(5)  # Returns True
bt.delete(5)
```

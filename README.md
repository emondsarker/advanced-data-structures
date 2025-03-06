# Advanced Data Structures

This repository contains implementations of three advanced data structures in Python.

## Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/advanced-data-structures.git
cd advanced-data-structures
```

2. Create and activate a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # On Unix/macOS
# or
.\venv\Scripts\activate  # On Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

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

## Performance Analysis

The repository includes tools to analyze and compare the performance characteristics of these data structures. You can generate graphs showing time and memory performance for operations on different input sizes.

### Running Analysis

1. Time Performance Analysis:

```bash
python3 performance_analysis.py
```

This will generate `graphs/insertion_performance.png` showing insertion time comparison across data structures.

2. Memory Usage Analysis:

```bash
python3 memory_analysis.py
```

This will generate `graphs/memory_usage.png` showing memory consumption comparison.

Both analyses test the data structures with increasing input sizes (1,000 to 1,000,000 elements) and use logarithmic scales to visualize performance differences. The graphs will be saved in the `graphs` directory.

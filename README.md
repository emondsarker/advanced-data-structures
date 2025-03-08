# Advanced Data Structures

This repository contains implementations of three advanced data structures in Python, along with comprehensive benchmarking and analysis tools.

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

## Project Structure

```
advanced-data-structures/
├── data_structures/           # Core data structure implementations
│   ├── __init__.py
│   ├── b_tree.py             # B-tree implementation
│   ├── dataset_generator.py   # Dataset generation utilities
│   ├── red_black_tree.py     # Red-Black tree implementation
│   └── xor_linked_list.py    # XOR Linked List implementation
├── datasets/                  # Generated test datasets
│   ├── dataset_100000.json
│   ├── large_500000.json
│   ├── large_1000000.json
│   ├── medium_50000.json
│   ├── medium_100000.json
│   ├── small_1000.json
│   ├── small_5000.json
│   └── small_10000.json
├── graphs/                    # Performance visualization graphs
│   ├── deletion_performance.png
│   ├── insertion_performance.png
│   └── search_performance.png
├── tests/                     # Unit tests
│   ├── test_b_tree.py
│   ├── test_red_black_tree.py
│   └── test_xor_linked_list.py
├── benchmark_data_structures.py  # Performance benchmarking script
├── generate_datasets.py          # Dataset generation script
├── performance_results.csv       # Benchmark results
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```

## Dependencies

The project requires the following Python packages:

```
contourpy==1.3.1      # Contour calculations for matplotlib
cycler==0.12.1        # Composable style cycles
fonttools==4.56.0     # Font file manipulation
kiwisolver==1.4.8     # Efficient constraint solving
matplotlib==3.10.1    # Plotting and visualization
numpy==2.2.3          # Numerical computations
packaging==24.2       # Core packaging utilities
pillow==11.1.0        # Image processing
pyparsing==3.2.1      # Parsing utilities
python-dateutil==2.9.0.post0  # Date utilities
six==1.17.0           # Python 2/3 compatibility
```

## Data Structures

### Red-Black Tree

Operations:

- `insert(data)`: Insert new data
- `read(data)`: Check if data exists
- `delete(data)`: Remove data

### XOR Linked List

Operations:

- `insert(data, position=None)`: Insert at end, beginning, or specific position
- `read(position)`: Read data at position
- `delete(position)`: Delete node at position

### B-tree

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

The repository includes comprehensive tools for analyzing and comparing the performance characteristics of these data structures.

### Dataset Generation

First, generate test datasets of various sizes:

```bash
python generate_datasets.py
```

This creates standardized datasets in the `datasets` directory:

- Small datasets: 1,000, 5,000, and 10,000 elements (for quick tests)
- Medium datasets: 50,000 and 100,000 elements (for thorough testing)
- Large datasets: 500,000 and 1,000,000 elements (for stress testing)

### Running Performance Analysis

Run the comprehensive benchmark suite:

```bash
python benchmark_data_structures.py
```

This will:

1. Test each data structure with increasing dataset sizes
2. Measure performance for insertion, search, and deletion operations
3. Generate performance graphs in the `graphs` directory:
   - `insertion_performance.png`: Comparison of insertion times
   - `search_performance.png`: Comparison of search times
   - `deletion_performance.png`: Comparison of deletion times
4. Save detailed results to `performance_results.csv` for further analysis

## Test Coverage

The repository includes comprehensive unit tests for each data structure:

```bash
python -m pytest tests/
```

Tests cover:

- Basic operations (insert, read, delete)
- Edge cases and error handling
- Structure-specific properties (e.g., Red-Black Tree balancing, B-tree degree constraints)

## Performance Results

The benchmarking process tests each data structure with datasets ranging from 100,000 to 1,000,000 elements. Results are saved in both visual (graphs) and tabular (CSV) formats for detailed analysis.

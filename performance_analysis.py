import time
import random
import matplotlib.pyplot as plt
from data_structures.b_tree import BTree
from data_structures.red_black_tree import RedBlackTree
from data_structures.xor_linked_list import XORLinkedList

def generate_random_data(size):
    """Generate a list of random integers."""
    return [random.randint(1, 1000000) for _ in range(size)]

def measure_insertion_time(data_structure, data):
    """Measure time taken to insert data into a data structure."""
    start_time = time.time()
    
    for value in data:
        if isinstance(data_structure, BTree):
            data_structure.insert(value)
        elif isinstance(data_structure, RedBlackTree):
            data_structure.insert(value)
        elif isinstance(data_structure, XORLinkedList):
            data_structure.insert(value)
    
    end_time = time.time()
    return end_time - start_time

def run_performance_analysis():
    """Run performance analysis on all data structures."""
    sizes = [1000, 10000, 100000, 1000000]
    
    results = {
        'B-Tree': [],
        'Red-Black Tree': [],
        'XOR Linked List': []
    }
    
    for size in sizes:
        print(f"Testing with {size} elements...")
        data = generate_random_data(size)
        
        btree = BTree(3) 
        results['B-Tree'].append(measure_insertion_time(btree, data))
        
        rbtree = RedBlackTree()
        results['Red-Black Tree'].append(measure_insertion_time(rbtree, data))
        
        xor_list = XORLinkedList()
        results['XOR Linked List'].append(measure_insertion_time(xor_list, data))
    
    # Plot results
    plt.figure(figsize=(10, 6))
    for structure, times in results.items():
        plt.plot(sizes, times, marker='o', label=structure)
    
    plt.xlabel('Number of Elements')
    plt.ylabel('Time (seconds)')
    plt.title('Data Structure Insertion Performance')
    plt.legend()
    plt.grid(True)
    plt.xscale('log')
    plt.yscale('log')
    
    # Save the plot
    plt.savefig('graphs/insertion_performance.png')
    print("Performance analysis complete. Graph saved as 'graphs/insertion_performance.png'")

if __name__ == '__main__':
    run_performance_analysis()

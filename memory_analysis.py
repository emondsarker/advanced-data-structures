import random
import psutil
import matplotlib.pyplot as plt
from data_structures.b_tree import BTree
from data_structures.red_black_tree import RedBlackTree
from data_structures.xor_linked_list import XORLinkedList

def generate_random_data(size):
    """Generate a list of random integers."""
    return [random.randint(1, 1000000) for _ in range(size)]

def measure_memory_usage(data_structure, data):
    """Measure memory usage while inserting data into a data structure."""
    process = psutil.Process()
    memory_usage = []
    initial_memory = process.memory_info().rss / 1024 / 1024  # Convert to MB
    
    # Measure memory at different intervals
    intervals = len(data) // 10 
    if intervals == 0:
        intervals = 1
    
    for i, value in enumerate(data):
        if isinstance(data_structure, BTree):
            data_structure.insert(value)
        elif isinstance(data_structure, RedBlackTree):
            data_structure.insert(value)
        elif isinstance(data_structure, XORLinkedList):
            data_structure.insert(value)
            
        if i % intervals == 0:
            current_memory = process.memory_info().rss / 1024 / 1024  # Convert to MB
            memory_usage.append(current_memory - initial_memory)
    
    final_memory = process.memory_info().rss / 1024 / 1024
    memory_usage.append(final_memory - initial_memory)
    
    return memory_usage

def run_memory_analysis():
    """Run memory analysis on all data structures."""
    sizes = [1000, 10000, 100000, 1000000]
    
    results = {
        'B-Tree': [],
        'Red-Black Tree': [],
        'XOR Linked List': []
    }
    
    # Run tests for each size
    for size in sizes:
        print(f"Testing with {size} elements...")
        data = generate_random_data(size)
        
        btree = BTree(3)
        memory_usage = measure_memory_usage(btree, data)
        results['B-Tree'].append(memory_usage[-1])  
        
        rbtree = RedBlackTree()
        memory_usage = measure_memory_usage(rbtree, data)
        results['Red-Black Tree'].append(memory_usage[-1])
        
        xor_list = XORLinkedList()
        memory_usage = measure_memory_usage(xor_list, data)
        results['XOR Linked List'].append(memory_usage[-1])
    
    # Plot results
    plt.figure(figsize=(10, 6))
    for structure, memory in results.items():
        plt.plot(sizes, memory, marker='o', label=structure)
    
    plt.xlabel('Number of Elements')
    plt.ylabel('Memory Usage (MB)')
    plt.title('Data Structure Memory Usage')
    plt.legend()
    plt.grid(True)
    plt.xscale('log')
    plt.yscale('log')
    
    # Save the plot
    plt.savefig('graphs/memory_usage.png')
    print("Memory analysis complete. Graph saved as 'graphs/memory_usage.png'")

if __name__ == '__main__':
    run_memory_analysis()

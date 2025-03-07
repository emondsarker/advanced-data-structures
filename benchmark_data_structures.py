import time
import matplotlib.pyplot as plt
import csv
from data_structures.b_tree import BTree
from data_structures.red_black_tree import RedBlackTree
from data_structures.xor_linked_list import XORLinkedList
from data_structures.dataset_generator import DatasetGenerator

def benchmark_data_structures(data_structure, dataset):
    """Test insertion, search, and deletion operations in sequence."""
    results = {'insertion': 0, 'search': 0, 'deletion': 0}
    
    # Convert dataset to list to avoid any iterator issues
    dataset = list(dataset)
    
    # Test insertion
    print("  Testing insertion...")
    start_time = time.time()
    for value in dataset:
        if isinstance(data_structure, XORLinkedList):
            data_structure.insert(value, position=0)  # Insert at beginning for XOR list
        else:
            data_structure.insert(value)
    results['insertion'] = time.time() - start_time
    print(f"  Insertion: {results['insertion']:.2f} seconds")
    
    # Test search (now that values are in the structure)
    print("  Testing search...")
    start_time = time.time()
    for value in dataset:
        try:
            if isinstance(data_structure, XORLinkedList):
                data_structure.read(0)  # Read from beginning for XOR list
            else:
                data_structure.read(value)  # Search by value for trees
        except (ValueError, IndexError):
            continue  # Skip if value not found
    results['search'] = time.time() - start_time
    print(f"  Search: {results['search']:.2f} seconds")
    
    # Test deletion (values are still in the structure)
    print("  Testing deletion...")
    start_time = time.time()
    dataset_copy = dataset.copy()  # Make a copy for deletion
    if not isinstance(data_structure, XORLinkedList):
        # For trees, delete in sorted order to maintain balance
        dataset_copy.sort()
    
    for value in dataset_copy:
        try:
            if isinstance(data_structure, XORLinkedList):
                data_structure.delete(0)  # Delete from beginning for XOR list
            else:
                data_structure.delete(value)  # Delete by value for trees
        except (ValueError, IndexError):
            continue  # Skip if value not found
    results['deletion'] = time.time() - start_time
    print(f"  Deletion: {results['deletion']:.2f} seconds")
    
    return results

def save_results_to_csv(results, sizes):
    """Save performance results to a CSV file."""
    with open('performance_results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write header
        writer.writerow(['Dataset Size', 'Data Structure', 'Operation', 'Time (seconds)'])
        
        # Write data
        for size_idx, size in enumerate(sizes):
            for structure in results:
                for operation in ['insertion', 'search', 'deletion']:
                    writer.writerow([
                        size,
                        structure,
                        operation,
                        results[structure][operation][size_idx]
                    ])
    print("\nResults saved to performance_results.csv")

def run_performance_analysis():
    """Run performance analysis for all operations on increasing dataset sizes."""
    structures = {
        'B-Tree': lambda: BTree(3),
        'Red-Black Tree': lambda: RedBlackTree(),
        'XOR Linked List': lambda: XORLinkedList()
    }
    
    results = {name: {'insertion': [], 'search': [], 'deletion': []} for name in structures}
    sizes = []
    
    generator = DatasetGenerator()
    
    # Test each size from 100k to 1M
    for size in range(100000, 1100000, 100000):
        print(f"\nTesting dataset size: {size:,}")
        dataset = generator.generate_dataset(size, seed=42)
        sizes.append(size)
        
        # Test each data structure
        for name, create_structure in structures.items():
            print(f"\nTesting {name}...")
            structure = create_structure()
            operation_times = benchmark_data_structures(structure, dataset)
            
            # Store results
            for operation, time_taken in operation_times.items():
                results[name][operation].append(time_taken)
    
    # Save results to CSV
    save_results_to_csv(results, sizes)
    
    # Plot results for each operation
    operations = ['insertion', 'search', 'deletion']
    for operation in operations:
        plt.figure(figsize=(12, 6))
        for name in structures:
            plt.plot(sizes, results[name][operation], marker='o', label=name)
        
        plt.xlabel('Dataset Size')
        plt.ylabel('Time (seconds)')
        plt.title(f'{operation.capitalize()} Performance Comparison')
        plt.legend()
        plt.grid(True)
        plt.savefig(f'graphs/{operation}_performance.png')
        print(f"\nSaved {operation} performance graph")

if __name__ == '__main__':
    run_performance_analysis()

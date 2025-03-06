import time
import random
import matplotlib.pyplot as plt
from data_structures.b_tree import BTree
from data_structures.red_black_tree import RedBlackTree
from data_structures.xor_linked_list import XORLinkedList

def generate_random_data(size):
    """Generate a list of random integers."""
    return [random.randint(1, 1000000) for _ in range(size)]

def calculate_moving_average(data, window_size=5):
    """Calculate moving average of the data."""
    result = []
    for i in range(len(data)):
        start_idx = max(0, i - window_size + 1)
        result.append(sum(data[start_idx:i + 1]) / (i - start_idx + 1))
    return result

def measure_individual_insertion_times(data_structure, max_size=1000000):
    """Measure time taken for each individual insertion."""
    times = []
    data_points = []
    current_size = 0
    
    # Measure every 10000 insertions
    measure_interval = 10000
    # Number of measurements to average for each interval
    measurements_per_interval = 100
    
    while current_size < max_size:
        if current_size % measure_interval == 0:
            # Take multiple measurements and average them
            interval_times = []
            for _ in range(measurements_per_interval):
                value = random.randint(1, 1000000)
                start_time = time.time()
                
                if isinstance(data_structure, BTree):
                    data_structure.insert(value)
                elif isinstance(data_structure, RedBlackTree):
                    data_structure.insert(value)
                elif isinstance(data_structure, XORLinkedList):
                    data_structure.insert(value, position=0)
                    
                end_time = time.time()
                interval_times.append(end_time - start_time)
            
            # Store average time for this interval
            times.append(sum(interval_times) / len(interval_times))
            data_points.append(current_size)
        else:
            # Insert without measuring time
            value = random.randint(1, 1000000)
            if isinstance(data_structure, BTree):
                data_structure.insert(value)
            elif isinstance(data_structure, RedBlackTree):
                data_structure.insert(value)
            elif isinstance(data_structure, XORLinkedList):
                data_structure.insert(value, position=0)
        
        current_size += 1
        
        if current_size % 1000 == 0:
            print(f"Processed {current_size:,} elements...")
    
    # Apply moving average to smooth out the data
    smoothed_times = calculate_moving_average(times)
    
    return data_points, smoothed_times

def run_performance_analysis():
    """Run performance analysis on all data structures."""
    results = {
        'B-Tree': {'points': [], 'times': []},
        'Red-Black Tree': {'points': [], 'times': []},
        'XOR Linked List': {'points': [], 'times': []}
    }
    
    print("Testing B-Tree...")
    btree = BTree(3)
    points, times = measure_individual_insertion_times(btree)
    results['B-Tree']['points'] = points
    results['B-Tree']['times'] = times
    
    print("\nTesting Red-Black Tree...")
    rbtree = RedBlackTree()
    points, times = measure_individual_insertion_times(rbtree)
    results['Red-Black Tree']['points'] = points
    results['Red-Black Tree']['times'] = times
    
    print("\nTesting XOR Linked List...")
    xor_list = XORLinkedList()
    points, times = measure_individual_insertion_times(xor_list)
    results['XOR Linked List']['points'] = points
    results['XOR Linked List']['times'] = times
    
    # Plot results
    plt.figure(figsize=(15, 8))
    for structure, data in results.items():
        plt.plot(data['points'], data['times'], label=structure, alpha=0.7)
    
    plt.xlabel('Number of Elements in Structure', fontsize=12)
    plt.ylabel('Average Time per Insertion (seconds)', fontsize=12)
    plt.title('Individual Insertion Time vs Structure Size\n(Moving Average)', fontsize=14)
    plt.legend()
    plt.grid(True)
    plt.xscale('log')
    plt.yscale('log')
    
    # Save the plot
    plt.savefig('graphs/insertion_performance.png')
    print("Performance analysis complete. Graph saved as 'graphs/insertion_performance.png'")

if __name__ == '__main__':
    run_performance_analysis()

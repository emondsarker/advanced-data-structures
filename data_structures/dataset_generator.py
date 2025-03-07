import random
import json
import os
from pathlib import Path

class DatasetGenerator:
    """Generator for creating and managing datasets for performance testing."""
    
    def __init__(self, min_value=1, max_value=1000000):
        """
        Initialize the dataset generator.
        
        Args:
            min_value (int): Minimum value for random numbers
            max_value (int): Maximum value for random numbers
        """
        self.min_value = min_value
        self.max_value = max_value
        self.datasets_dir = Path('datasets')
        self.datasets_dir.mkdir(exist_ok=True)
    
    def generate_dataset(self, size, seed=None):
        """
        Generate a dataset of specified size.
        
        Args:
            size (int): Number of elements in the dataset
            seed (int, optional): Random seed for reproducibility
            
        Returns:
            list: Generated dataset
        """
        if seed is not None:
            random.seed(seed)
            
        return [random.randint(self.min_value, self.max_value) for _ in range(size)]
    
    def save_dataset(self, dataset, name):
        """
        Save a dataset to a file.
        
        Args:
            dataset (list): The dataset to save
            name (str): Name of the dataset file (without extension)
        """
        file_path = self.datasets_dir / f"{name}.json"
        with open(file_path, 'w') as f:
            json.dump(dataset, f)
    
    def load_dataset(self, name):
        """
        Load a dataset from a file.
        
        Args:
            name (str): Name of the dataset file (without extension)
            
        Returns:
            list: The loaded dataset
        """
        file_path = self.datasets_dir / f"{name}.json"
        with open(file_path, 'r') as f:
            return json.load(f)
    
    def generate_and_save(self, sizes, prefix="dataset", seed=None):
        """
        Generate and save multiple datasets of different sizes.
        
        Args:
            sizes (list): List of sizes for the datasets
            prefix (str): Prefix for the dataset filenames
            seed (int, optional): Random seed for reproducibility
        """
        for size in sizes:
            dataset = self.generate_dataset(size, seed)
            name = f"{prefix}_{size}"
            self.save_dataset(dataset, name)
            print(f"Generated and saved dataset with {size} elements as {name}.json")
    
    def list_datasets(self):
        """
        List all available datasets.
        
        Returns:
            list: Names of available datasets (without extension)
        """
        return [f.stem for f in self.datasets_dir.glob("*.json")]

def generate_standard_datasets(seed=42):
    """
    Generate standard datasets for all performance tests.
    """
    generator = DatasetGenerator()
    
    # Generate datasets for different test cases
    sizes = {
        'small': [1000, 5000, 10000],  # For quick tests
        'medium': [50000, 100000],     # For more thorough testing
        'large': [500000, 1000000]     # For stress testing
    }
    
    for category, category_sizes in sizes.items():
        generator.generate_and_save(category_sizes, prefix=category, seed=seed)
    
    print("\nAvailable datasets:")
    for dataset in generator.list_datasets():
        print(f"- {dataset}")

if __name__ == '__main__':
    generate_standard_datasets()

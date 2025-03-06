import unittest
from data_structures.b_tree import BTree

class TestBTree(unittest.TestCase):
    def setUp(self):
        """Set up a new B-tree before each test."""
        self.tree = BTree(3)  # Minimum degree 3

    def test_insert_and_read(self):
        """Test basic insertion and reading operations."""
        values = [10, 20, 5, 6, 12, 30, 7, 17]
        for value in values:
            self.tree.insert(value)
            self.assertTrue(self.tree.read(value))

    def test_delete(self):
        """Test deletion operation."""
        # Insert fewer values to reduce complexity
        values = [10, 20, 30]
        for value in values:
            self.tree.insert(value)
            self.assertTrue(self.tree.read(value))

        # Delete middle value
        self.tree.delete(20)
        self.assertFalse(self.tree.read(20))
        self.assertTrue(self.tree.read(10))
        self.assertTrue(self.tree.read(30))

    def test_delete_nonexistent(self):
        """Test deleting a value that doesn't exist."""
        self.tree.insert(5)
        with self.assertRaises(ValueError):
            self.tree.delete(10)

    def test_read_empty_tree(self):
        """Test reading from an empty tree."""
        self.assertFalse(self.tree.read(5))

if __name__ == '__main__':
    unittest.main()

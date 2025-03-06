import unittest
from data_structures.red_black_tree import RedBlackTree

class TestRedBlackTree(unittest.TestCase):
    def setUp(self):
        """Set up a new tree before each test."""
        self.tree = RedBlackTree()

    def test_insert_and_read(self):
        """Test basic insertion and reading operations."""
        values = [7, 3, 18, 10, 22, 8, 11, 26, 2, 6]
        for value in values:
            self.tree.insert(value)
            self.assertTrue(self.tree.read(value))

    def test_delete(self):
        """Test deletion operation."""
        values = [7, 3, 18, 10, 22]
        for value in values:
            self.tree.insert(value)

        self.tree.delete(18)
        self.assertFalse(self.tree.read(18))
        self.assertTrue(self.tree.read(7))
        self.assertTrue(self.tree.read(22))

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

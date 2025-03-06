import unittest
from data_structures.xor_linked_list import XORLinkedList

class TestXORLinkedList(unittest.TestCase):
    def setUp(self):
        """Set up a new list before each test."""
        self.list = XORLinkedList()

    def test_insert_and_read(self):
        """Test insertion at different positions and reading."""

        with self.assertRaises(IndexError):
            self.list.read(0)

        self.list.insert(1)
        self.assertEqual(self.list.read(0), 1)
        
        # Insert at beginning
        self.list.insert(2, 0)
        self.assertEqual(self.list.read(0), 2)
        self.assertEqual(self.list.read(1), 1)

    def test_delete(self):
        """Test deletion from different positions."""
        values = [1, 2, 3, 4]
        for value in values:
            self.list.insert(value)

        deleted = self.list.delete(1)
        self.assertEqual(deleted, 2)
        self.assertEqual(self.list.read(1), 3)

        deleted = self.list.delete(0)
        self.assertEqual(deleted, 1)
        self.assertEqual(self.list.read(0), 3)

    def test_empty_list_operations(self):
        """Test operations on empty list."""
        with self.assertRaises(IndexError):
            self.list.read(0)

        with self.assertRaises(IndexError):
            self.list.delete(0)

    def test_invalid_position(self):
        """Test operations with invalid positions."""
        self.list.insert(1)
        
        with self.assertRaises(IndexError):
            self.list.read(1)

        with self.assertRaises(IndexError):
            self.list.delete(1)

        with self.assertRaises(IndexError):
            self.list.insert(2, 2)

if __name__ == '__main__':
    unittest.main()

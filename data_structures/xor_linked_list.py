"""
Implementation of a Memory-Efficient Doubly Linked List using XOR.

This implementation uses XOR of memory addresses to store both previous and next pointers
in a single field, effectively halving the memory requirement compared to a traditional
doubly linked list.

Note: This implementation requires careful memory management and pointer manipulation.
"""

import ctypes

class Node:
    """A node in the XOR Linked List.
    
    Attributes:
        data: The data stored in the node
        npx (int): XOR of addresses of previous and next nodes
    """
    
    def __init__(self, data):
        """Initialize a new node with the given data.
        
        Args:
            data: The data to be stored in the node
        """
        self.data = data
        self.npx = 0  # XOR of previous and next node addresses

class XORLinkedList:
    """Memory-efficient doubly linked list using XOR of addresses."""
    
    def __init__(self):
        """Initialize an empty XOR linked list."""
        self.head = None
        self.tail = None
        self._nodes = []  # Keep references to prevent garbage collection
    
    def _get_ptr(self, node):
        """Get the memory address of a node.
        
        Args:
            node: The node whose address is needed
            
        Returns:
            int: Memory address of the node
        """
        return id(node) if node else 0
    
    def _get_node(self, ptr):
        """Get the node from its memory address.
        
        Args:
            ptr (int): Memory address of the node
            
        Returns:
            Node: The node at the given address
        """
        return ctypes.cast(ptr, ctypes.py_object).value if ptr else None
    
    def insert(self, data, position=None):
        """Insert a new node with the given data.
        
        If position is None, insert at the end.
        If position is 0, insert at the beginning.
        
        Args:
            data: The data to be stored
            position (int, optional): Position to insert at. Defaults to None.
            
        Raises:
            IndexError: If position is out of range
        """
        new_node = Node(data)
        self._nodes.append(new_node)  # Prevent garbage collection
        
        if not self.head:  # Empty list
            self.head = new_node
            self.tail = new_node
            return
            
        if position == 0:  # Insert at beginning
            new_ptr = self._get_ptr(new_node)
            head_ptr = self._get_ptr(self.head)
            new_node.npx = head_ptr
            self.head.npx = self.head.npx ^ new_ptr
            self.head = new_node
            return
            
        if position is None:  # Insert at end
            new_ptr = self._get_ptr(new_node)
            tail_ptr = self._get_ptr(self.tail)
            new_node.npx = tail_ptr
            self.tail.npx = self.tail.npx ^ new_ptr
            self.tail = new_node
            return
            
        # Insert at specific position
        current = self.head
        prev_ptr = 0
        count = 0
        
        while current and count < position:
            next_ptr = prev_ptr ^ current.npx
            if not next_ptr:
                raise IndexError("Position out of range")
            prev_ptr = self._get_ptr(current)
            current = self._get_node(next_ptr)
            count += 1
            
        if not current:
            raise IndexError("Position out of range")
            
        new_ptr = self._get_ptr(new_node)
        next_ptr = prev_ptr ^ current.npx
        
        # Update pointers
        new_node.npx = prev_ptr ^ next_ptr
        if prev_ptr:
            prev_node = self._get_node(prev_ptr)
            prev_node.npx = prev_node.npx ^ self._get_ptr(current) ^ new_ptr
        current.npx = new_ptr ^ next_ptr
    
    def read(self, position):
        """Read data at the specified position.
        
        Args:
            position (int): Position to read from (0-based)
            
        Returns:
            The data at the specified position
            
        Raises:
            IndexError: If position is out of range
        """
        if not self.head:
            raise IndexError("List is empty")
            
        current = self.head
        prev_ptr = 0
        count = 0
        
        while current and count < position:
            next_ptr = prev_ptr ^ current.npx
            if not next_ptr:
                raise IndexError("Position out of range")
            prev_ptr = self._get_ptr(current)
            current = self._get_node(next_ptr)
            count += 1
            
        if not current:
            raise IndexError("Position out of range")
            
        return current.data
    
    def delete(self, position):
        """Delete node at the specified position.
        
        Args:
            position (int): Position to delete from (0-based)
            
        Returns:
            The data from the deleted node
            
        Raises:
            IndexError: If position is out of range
        """
        if not self.head:
            raise IndexError("List is empty")
            
        if position == 0:  # Delete head
            data = self.head.data
            next_ptr = self.head.npx
            if next_ptr:  # More than one node
                next_node = self._get_node(next_ptr)
                next_node.npx = next_node.npx ^ self._get_ptr(self.head)
                self.head = next_node
            else:  # Only one node
                self.head = None
                self.tail = None
            return data
            
        # Find node to delete
        current = self.head
        prev_ptr = 0
        count = 0
        
        while current and count < position:
            next_ptr = prev_ptr ^ current.npx
            if not next_ptr:
                raise IndexError("Position out of range")
            prev_ptr = self._get_ptr(current)
            current = self._get_node(next_ptr)
            count += 1
            
        if not current:
            raise IndexError("Position out of range")
            
        # Get next node pointer
        next_ptr = prev_ptr ^ current.npx
        
        # Update adjacent nodes
        if prev_ptr:
            prev_node = self._get_node(prev_ptr)
            prev_node.npx = prev_node.npx ^ self._get_ptr(current)
            if next_ptr:
                prev_node.npx = prev_node.npx ^ next_ptr
                
        if next_ptr:
            next_node = self._get_node(next_ptr)
            next_node.npx = next_node.npx ^ self._get_ptr(current)
            if prev_ptr:
                next_node.npx = next_node.npx ^ prev_ptr
                
        # Update tail if necessary
        if current == self.tail:
            self.tail = self._get_node(prev_ptr)
            
        # Remove from reference list to allow garbage collection
        self._nodes.remove(current)
        return current.data

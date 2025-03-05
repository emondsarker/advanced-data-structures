"""
Implementation of a Red-Black Tree data structure.

A Red-Black Tree is a self-balancing binary search tree where each node has an extra bit for denoting the color
of the node, either red or black. The tree maintains the following properties:
1. Every node is either red or black
2. The root is black
3. Every leaf (NIL) is black
4. If a node is red, then both its children are black
5. For each node, all simple paths from the node to descendant leaves contain the same number of black nodes
"""

class Node:
    """A node in the Red-Black Tree.
    
    Attributes:
        data: The data stored in the node
        color (bool): True for Red, False for Black
        left (Node): Left child
        right (Node): Right child
        parent (Node): Parent node
    """
    
    def __init__(self, data):
        self.data = data
        self.color = True  # New nodes are red by default
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    """Red-Black Tree implementation with standard operations.
    
    The tree maintains balance through color properties and rotations.
    """
    
    def __init__(self):
        """Initialize an empty Red-Black Tree."""
        self.NIL = Node(None)  # Sentinel node
        self.NIL.color = False  # NIL nodes are black
        self.root = self.NIL
    
    def insert(self, data):
        """Insert a new node with the given data.
        
        Args:
            data: The data to be inserted
        """
        node = Node(data)
        node.left = self.NIL
        node.right = self.NIL
        
        y = None
        x = self.root
        
        # Find the position to insert
        while x != self.NIL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right
        
        node.parent = y
        if y is None:
            self.root = node  # Tree was empty
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node
            
        self._fix_insert(node)
    
    def read(self, data):
        """Search for a node with the given data.
        
        Args:
            data: The data to search for
            
        Returns:
            bool: True if data exists in tree, False otherwise
        """
        node = self.root
        while node != self.NIL:
            if data == node.data:
                return True
            elif data < node.data:
                node = node.left
            else:
                node = node.right
        return False
    
    def delete(self, data):
        """Delete the node with the given data.
        
        Args:
            data: The data to be deleted
            
        Raises:
            ValueError: If data not found in tree
        """
        z = self._find_node(data)
        if z:
            self._delete_node(z)
        else:
            raise ValueError("Data not found in tree")
    
    # Private methods
    
    def _fix_insert(self, k):
        """Fix the Red-Black Tree properties after insertion."""
        while k.parent and k.parent.color:  # While parent is red
            if k.parent == k.parent.parent.right:  # Parent is right child
                u = k.parent.parent.left  # Uncle
                if u.color:  # Uncle is red
                    u.color = False
                    k.parent.color = False
                    k.parent.parent.color = True
                    k = k.parent.parent
                else:  # Uncle is black
                    if k == k.parent.left:  # k is left child
                        k = k.parent
                        self._right_rotate(k)
                    k.parent.color = False
                    k.parent.parent.color = True
                    self._left_rotate(k.parent.parent)
            else:  # Parent is left child
                u = k.parent.parent.right  # Uncle
                if u.color:  # Uncle is red
                    u.color = False
                    k.parent.color = False
                    k.parent.parent.color = True
                    k = k.parent.parent
                else:  # Uncle is black
                    if k == k.parent.right:  # k is right child
                        k = k.parent
                        self._left_rotate(k)
                    k.parent.color = False
                    k.parent.parent.color = True
                    self._right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = False  # Root must be black
    
    def _left_rotate(self, x):
        """Perform left rotation on the given node."""
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
    
    def _right_rotate(self, x):
        """Perform right rotation on the given node."""
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
    
    def _find_node(self, data):
        """Find and return the node with the given data."""
        node = self.root
        while node != self.NIL:
            if data == node.data:
                return node
            elif data < node.data:
                node = node.left
            else:
                node = node.right
        return None
    
    def _delete_node(self, z):
        """Delete the given node and fix the tree properties."""
        y = z
        y_original_color = y.color
        
        if z.left == self.NIL:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
            
        if y_original_color == False:
            self._fix_delete(x)
    
    def _fix_delete(self, x):
        """Fix the Red-Black Tree properties after deletion."""
        while x != self.root and x.color == False:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == True:
                    w.color = False
                    x.parent.color = True
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == False and w.right.color == False:
                    w.color = True
                    x = x.parent
                else:
                    if w.right.color == False:
                        w.left.color = False
                        w.color = True
                        self._right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = False
                    w.right.color = False
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == True:
                    w.color = False
                    x.parent.color = True
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == False and w.left.color == False:
                    w.color = True
                    x = x.parent
                else:
                    if w.left.color == False:
                        w.right.color = False
                        w.color = True
                        self._left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = False
                    w.left.color = False
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = False
    
    def _transplant(self, u, v):
        """Replace subtree rooted at u with subtree rooted at v."""
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
    
    def _minimum(self, node):
        """Find the minimum value in the subtree rooted at node."""
        while node.left != self.NIL:
            node = node.left
        return node

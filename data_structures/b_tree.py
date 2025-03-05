"""
Implementation of a B-tree data structure.

A B-tree is a self-balancing tree data structure that maintains sorted data and allows
searches, sequential access, insertions, and deletions in logarithmic time. It is
optimized for systems that read and write large blocks of data.

Properties:
1. Every node has at most m children (m is the order of the tree)
2. Every non-leaf node (except root) has at least ⌈m/2⌉ children
3. The root has at least two children if it is not a leaf
4. All leaves appear in the same level
5. A non-leaf node with k children contains k-1 keys
"""

class Node:
    """A node in the B-tree.
    
    Attributes:
        keys (list): List of keys stored in the node
        children (list): List of child nodes
        leaf (bool): True if this is a leaf node
    """
    
    def __init__(self, leaf=True):
        """Initialize a new node.
        
        Args:
            leaf (bool): True if this is a leaf node
        """
        self.keys = []
        self.children = []
        self.leaf = leaf

class BTree:
    """B-tree implementation with standard operations.
    
    The tree maintains balance and sorted order through node splitting
    and merging operations.
    
    Attributes:
        root (Node): Root node of the tree
        t (int): Minimum degree (minimum number of keys = t-1)
    """
    
    def __init__(self, t):
        """Initialize an empty B-tree with the given minimum degree.
        
        Args:
            t (int): Minimum degree of the tree (minimum number of keys = t-1)
        """
        self.root = Node()
        self.t = t  # Minimum degree
    
    def insert(self, k):
        """Insert a key into the B-tree.
        
        Args:
            k: Key to be inserted
        """
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            # If root is full, create new root
            new_root = Node(leaf=False)
            self.root = new_root
            new_root.children.append(root)
            self._split_child(new_root, 0)
            self._insert_non_full(new_root, k)
        else:
            self._insert_non_full(root, k)
    
    def read(self, k):
        """Search for a key in the B-tree.
        
        Args:
            k: Key to search for
            
        Returns:
            bool: True if key exists in tree, False otherwise
        """
        return self._search(self.root, k) is not None
    
    def delete(self, k):
        """Delete a key from the B-tree.
        
        Args:
            k: Key to be deleted
            
        Raises:
            ValueError: If key not found in tree
        """
        self._delete_key(self.root, k)
        
   
    # Private Methods
    
    def _split_child(self, x, i):
        """Split the i-th child of node x.
        
        Args:
            x (Node): Parent node
            i (int): Index of child to split
        """
        t = self.t
        y = x.children[i]
        z = Node(leaf=y.leaf)
        
        # Move keys and children from y to z
        z.keys = y.keys[t:]
        y.keys = y.keys[:t-1]
        
        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]
        
        # Insert middle key into parent
        x.keys.insert(i, y.keys.pop())
        x.children.insert(i + 1, z)
    
    def _insert_non_full(self, x, k):
        """Insert key k into non-full node x.
        
        Args:
            x (Node): Node to insert into
            k: Key to insert
        """
        i = len(x.keys) - 1
        
        if x.leaf:
            # Insert key into leaf node
            while i >= 0 and k < x.keys[i]:
                i -= 1
            x.keys.insert(i + 1, k)
        else:
            # Find child to recurse on
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            
            if len(x.children[i].keys) == (2 * self.t) - 1:
                self._split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self._insert_non_full(x.children[i], k)
    
    def _search(self, x, k):
        """Search for key k in subtree rooted at x.
        
        Args:
            x (Node): Root of subtree to search
            k: Key to search for
            
        Returns:
            tuple: (node, index) if key found, None otherwise
        """
        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i += 1
            
        if i < len(x.keys) and k == x.keys[i]:
            return (x, i)
            
        if x.leaf:
            return None
            
        return self._search(x.children[i], k)
    
    def _delete_key(self, x, k):
        """Delete key k from subtree rooted at x.
        
        Args:
            x (Node): Root of subtree
            k: Key to delete
            
        Raises:
            ValueError: If key not found
        """
        t = self.t
        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i += 1
            
        if x.leaf:
            if i < len(x.keys) and x.keys[i] == k:
                x.keys.pop(i)
            else:
                raise ValueError("Key not found in tree")
        else:
            if i < len(x.keys) and x.keys[i] == k:
                self._delete_from_internal_node(x, k, i)
            else:
                if i == len(x.keys):
                    i -= 1
                child = x.children[i]
                
                if len(child.keys) < t:
                    self._fill_child(x, i)
                    
                if i > len(x.keys):
                    self._delete_key(x.children[i-1], k)
                else:
                    self._delete_key(x.children[i], k)
    
    def _delete_from_internal_node(self, x, k, i):
        """Delete key k from internal node x.
        
        Args:
            x (Node): Internal node
            k: Key to delete
            i (int): Index of key in node
        """
        if x.children[i].keys:
            pred = self._get_predecessor(x, i)
            x.keys[i] = pred
            self._delete_key(x.children[i], pred)
        elif x.children[i+1].keys:
            successor = self._get_successor(x, i)
            x.keys[i] = successor
            self._delete_key(x.children[i+1], successor)
        else:
            self._merge_children(x, i)
            self._delete_key(x.children[i], k)
    
    def _get_predecessor(self, x, i):
        """Get predecessor of keys[i] in node x.
        
        Args:
            x (Node): Node containing key
            i (int): Index of key
            
        Returns:
            Predecessor key
        """
        curr = x.children[i]
        while not curr.leaf:
            curr = curr.children[-1]
        return curr.keys[-1]
    
    def _get_successor(self, x, i):
        """Get successor of keys[i] in node x.
        
        Args:
            x (Node): Node containing key
            i (int): Index of key
            
        Returns:
            Successor key
        """
        curr = x.children[i+1]
        while not curr.leaf:
            curr = curr.children[0]
        return curr.keys[0]
    
    def _fill_child(self, x, i):
        """Fill child i of x with a key from sibling.
        
        Args:
            x (Node): Parent node
            i (int): Index of child to fill
        """
        if i != 0 and len(x.children[i-1].keys) >= self.t:
            self._borrow_from_prev(x, i)
        elif i != len(x.children)-1 and len(x.children[i+1].keys) >= self.t:
            self._borrow_from_next(x, i)
        else:
            if i != len(x.children)-1:
                self._merge_children(x, i)
            else:
                self._merge_children(x, i-1)
    
    def _borrow_from_prev(self, x, i):
        """Borrow a key from previous sibling.
        
        Args:
            x (Node): Parent node
            i (int): Index of child borrowing key
        """
        child = x.children[i]
        sibling = x.children[i-1]
        
        child.keys.insert(0, x.keys[i-1])
        if not child.leaf:
            child.children.insert(0, sibling.children.pop())
            
        x.keys[i-1] = sibling.keys.pop()
    
    def _borrow_from_next(self, x, i):
        """Borrow a key from next sibling.
        
        Args:
            x (Node): Parent node
            i (int): Index of child borrowing key
        """
        child = x.children[i]
        sibling = x.children[i+1]
        
        child.keys.append(x.keys[i])
        if not child.leaf:
            child.children.append(sibling.children.pop(0))
            
        x.keys[i] = sibling.keys.pop(0)
    
    def _merge_children(self, x, i):
        """Merge children i and i+1 of x.
        
        Args:
            x (Node): Parent node
            i (int): Index of first child to merge
        """
        child = x.children[i]
        sibling = x.children[i+1]
        
        child.keys.append(x.keys.pop(i))
        child.keys.extend(sibling.keys)
        
        if not child.leaf:
            child.children.extend(sibling.children)
            
        x.children.pop(i+1)
        
        if x == self.root and not x.keys:
            self.root = child

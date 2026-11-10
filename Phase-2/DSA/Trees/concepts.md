# Trees & Binary Search Trees (BST) in C — Core Concepts

## 1. What is a Tree?
A **Tree** is a non-linear, hierarchical data structure consisting of nodes connected by directed or undirected edges. Unlike arrays and linked lists, trees represent hierarchical relationships such as file directories or family lineages.

### Tree Terminology
- **Root:** The topmost node with no parent.
- **Parent & Child:** A node directly connected above/below another.
- **Leaf (External Node):** A node having zero children.
- **Depth:** Number of edges from root to the node.
- **Height:** Number of edges on the longest path from node to a leaf.
- **Subtree:** A tree consisting of a node and all its descendants.

---

## 2. Binary Tree & Binary Search Tree (BST)

### Binary Tree
A tree where each node has at most two children, referred to as **left child** and **right child**.

### Binary Search Tree (BST) Property
A specialized binary tree maintaining an ordering invariant for all nodes:
$$	ext{Keys in Left Subtree} < 	ext{Root Key} < 	ext{Keys in Right Subtree}$$
This property enables binary-search-like efficiency ($O(\log n)$ average time) for search, insert, and delete operations.

```
         (50)
        /    \
      (30)    (70)
      /  \   /   \
    (20)(40)(60) (80)
```

---

## 3. Tree Traversal Algorithms
Tree traversal is the process of visiting every node in the tree exactly once.

| Traversal | Order of Visiting | Primary Application |
| :--- | :--- | :--- |
| **Inorder** | `Left -> Root -> Right` | Produces sorted values in a BST |
| **Preorder** | `Root -> Left -> Right` | Used to serialize/clone tree structure |
| **Postorder** | `Left -> Right -> Root` | Used in bottom-up cleanup (deleting trees) & postfix evaluation |
| **Level-Order** | Breadth-First (BFS) level-by-level | Printing tree level-wise using a FIFO queue |

---

## 4. Time & Space Complexity
| Operation | Average Case (Balanced BST) | Worst Case (Degenerate/Skewed Tree) | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Search** | $O(\log n)$ | $O(n)$ | $O(h)$ call stack space |
| **Insert** | $O(\log n)$ | $O(n)$ | $O(h)$ |
| **Delete** | $O(\log n)$ | $O(n)$ | $O(h)$ |
| **Traversals** | $O(n)$ | $O(n)$ | $O(h)$ (where $h = \log n$ to $n$) |

---

## 5. Practical Applications
1. **Database Indexing:** B-Trees and B+ Trees used in PostgreSQL, MySQL, and SQLite.
2. **File Systems:** Hierarchical folder structures in Windows (NTFS) and Linux (ext4).
3. **Compiler Syntax Trees:** Abstract Syntax Trees (AST) parse arithmetic expressions.
4. **Auto-complete & Routing:** Trie structures and routing tables.

---

## 6. Practice Problems
- **Easy:** Maximum depth / height of binary tree; Count total leaf nodes.
- **Medium:** Validate if a binary tree is a valid BST; Lowest Common Ancestor (LCA) in BST.
- **Hard:** Serialize and deserialize binary tree; Delete a node with two children in a BST.

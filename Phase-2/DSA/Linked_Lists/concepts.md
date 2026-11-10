# Linked Lists in C — Core Concepts

## 1. What is a Linked List?
A **Linked List** is a linear, dynamic data structure where elements (called **nodes**) are not stored at contiguous memory locations. Instead, each node contains two components:
1. **Data:** The value or payload stored in the node.
2. **Next Pointer:** A pointer holding the memory address of the next node in the sequence.

```
[ Head ] -> [ Data | Next ] -> [ Data | Next ] -> [ Data | NULL ]
```

---

## 2. Types of Linked Lists

### A. Singly Linked List (SLL)
Each node points only to the next node. Traversal is strictly unidirectional (forward).
- **Structure in C:**
```c
struct Node {
    int data;
    struct Node* next;
};
```

### B. Doubly Linked List (DLL)
Each node contains two pointers: `prev` pointing to the previous node and `next` pointing to the next node. Allows bidirectional traversal (forward and backward).
```
NULL <- [ Prev | Data | Next ] <-> [ Prev | Data | Next ] -> NULL
```

### C. Circular Linked List (CLL)
The `next` pointer of the last node points back to the `head` node rather than `NULL`. Can be singly circular or doubly circular.

---

## 3. Core Operations & Algorithms
- **Insertion at Beginning:** Allocate new node, set `new_node->next = head`, set `head = new_node`. Time: $O(1)$.
- **Insertion at End:** Traverse to node where `curr->next == NULL`, link `curr->next = new_node`. Time: $O(n)$.
- **Deletion by Value:** Traverse finding target node while tracking `prev` pointer. Link `prev->next = target->next` and `free(target)`. Time: $O(n)$.
- **List Reversal:** Use three pointers (`prev = NULL`, `curr = head`, `next = NULL`) to reverse link directions in one pass. Time: $O(n)$, Space: $O(1)$.

---

## 4. Time & Space Complexity
| Operation | Singly Linked List | Doubly Linked List | Array Comparison |
| :--- | :--- | :--- | :--- |
| **Insert at Head** | $O(1)$ | $O(1)$ | $O(n)$ (requires shifting) |
| **Insert at Tail** | $O(n)$ ($O(1)$ with tail ptr) | $O(1)$ (with tail ptr) | $O(1)$ (if capacity remains) |
| **Delete Head** | $O(1)$ | $O(1)$ | $O(n)$ |
| **Access / Search by Index** | $O(n)$ | $O(n)$ | $O(1)$ (random access) |
| **Memory Overhead** | 1 pointer per node | 2 pointers per node | 0 pointer overhead |

---

## 5. Practical Applications
1. **Dynamic Memory Allocation:** Used by operating system heap managers (free list tracking).
2. **Undo Functionality:** Browser history (Back/Forward using Doubly Linked List).
3. **Music Playlists:** Circular playlists repeating songs infinitely.
4. **Implementation of Other Structures:** Used to implement dynamic Stacks, Queues, Hash Tables (Separate Chaining), and Graph Adjacency Lists.

---

## 6. Practice Problems
- **Easy:** Print elements of a linked list; Count number of nodes.
- **Medium:** Reverse a singly linked list; Detect a cycle using Floyd's Tortoise and Hare algorithm.
- **Hard:** Merge $k$ sorted linked lists; Flatten a multilevel doubly linked list.

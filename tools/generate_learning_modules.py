"""
Generator script to populate all Phase III learning modules for DSA (C) and OOP (C++).
Creates concepts.md, notes.md, resources.json updates, and Phase-3 standalone source files.
"""

import os
import json
from pathlib import Path

BASE_DIR = Path(r"C:\Users\sudeep\OneDrive\Documents\SkillArc-PBL")
DSA_DIR = BASE_DIR / "Phase-2" / "DSA"
OOPS_DIR = BASE_DIR / "Phase-2" / "OOPS"
PHASE3_DIR = BASE_DIR / "Phase-3"
PHASE3_DSA = PHASE3_DIR / "DSA"
PHASE3_OOPS = PHASE3_DIR / "OOPS"

PHASE3_DSA.mkdir(parents=True, exist_ok=True)
PHASE3_OOPS.mkdir(parents=True, exist_ok=True)

# -----------------------------------------------------------------------------
# DSA MODULES CONTENT
# -----------------------------------------------------------------------------
MODULES_DSA = {
    "Linked_Lists": {
        "concepts": """# Linked Lists in C — Core Concepts

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
""",
        "notes": """/**
 * SkillArc Phase III — Data Structures in C
 * Module: Singly Linked List Implementation
 * Author: Team Apex (Samiksha Gurung, Vaibhavi Thapliyal, Tanisha Rai)
 * Features:
 *  - Dynamic node creation using malloc()
 *  - Insertion at beginning and end
 *  - Linear traversal and searching
 *  - In-place iterative list reversal
 *  - Safe memory cleanup with free()
 */

#include <stdio.h>
#include <stdlib.h>

// Definition of a Singly Linked List Node
typedef struct Node {
    int data;
    struct Node* next;
} Node;

// Function to allocate a new node dynamically on the heap
Node* createNode(int value) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (newNode == NULL) {
        printf("Error: Memory allocation failed!\\n");
        exit(1);
    }
    newNode->data = value;
    newNode->next = NULL;
    return newNode;
}

// Insert a new element at the beginning (Head) of the list: O(1) time
void insertAtHead(Node** headRef, int value) {
    Node* newNode = createNode(value);
    newNode->next = *headRef;
    *headRef = newNode;
    printf("Inserted %d at head.\\n", value);
}

// Insert a new element at the end (Tail) of the list: O(n) time
void insertAtTail(Node** headRef, int value) {
    Node* newNode = createNode(value);
    if (*headRef == NULL) {
        *headRef = newNode;
        return;
    }
    Node* temp = *headRef;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = newNode;
    printf("Inserted %d at tail.\\n", value);
}

// Traverse and print the list: O(n) time
void displayList(Node* head) {
    printf("List: [Head] -> ");
    Node* temp = head;
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\\n");
}

// Reverse the linked list in-place: O(n) time, O(1) space
void reverseList(Node** headRef) {
    Node* prev = NULL;
    Node* curr = *headRef;
    Node* next = NULL;
    
    while (curr != NULL) {
        next = curr->next;  // Store next node
        curr->next = prev;  // Reverse current node's pointer
        prev = curr;        // Move prev forward
        curr = next;        // Move curr forward
    }
    *headRef = prev;
    printf("Linked List reversed successfully!\\n");
}

// Deallocate all nodes to prevent memory leaks
void freeList(Node* head) {
    Node* temp;
    while (head != NULL) {
        temp = head;
        head = head->next;
        free(temp);
    }
    printf("Memory freed successfully.\\n");
}

int main() {
    printf("========================================\\n");
    printf(" SkillArc — Singly Linked List in C     \\n");
    printf("========================================\\n\\n");

    Node* head = NULL;

    insertAtHead(&head, 30);
    insertAtHead(&head, 20);
    insertAtHead(&head, 10);
    insertAtTail(&head, 40);
    insertAtTail(&head, 50);

    printf("\\nInitial ");
    displayList(head);

    printf("\\nReversing list...\\n");
    reverseList(&head);

    printf("Reversed ");
    displayList(head);

    printf("\\nCleaning up heap memory...\\n");
    freeList(head);

    return 0;
}
"""
    },
    "Trees": {
        "concepts": """# Trees & Binary Search Trees (BST) in C — Core Concepts

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
$$\text{Keys in Left Subtree} < \text{Root Key} < \text{Keys in Right Subtree}$$
This property enables binary-search-like efficiency ($O(\log n)$ average time) for search, insert, and delete operations.

```
         (50)
        /    \\
      (30)    (70)
      /  \\   /   \\
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
""",
        "notes": """/**
 * SkillArc Phase III — Data Structures in C
 * Module: Binary Search Tree (BST) Implementation
 * Author: Team Apex (Samiksha Gurung, Vaibhavi Thapliyal, Tanisha Rai)
 * Features:
 *  - Dynamic BST node creation
 *  - Recursive BST insertion preserving invariant
 *  - Recursive searching: O(log n) average time
 *  - Inorder traversal (outputs sorted keys)
 *  - Leaf node counter function
 */

#include <stdio.h>
#include <stdlib.h>

// Definition of a Binary Search Tree Node
typedef struct BSTNode {
    int data;
    struct BSTNode* left;
    struct BSTNode* right;
} BSTNode;

// Function to create a new tree node
BSTNode* createTreeNode(int value) {
    BSTNode* newNode = (BSTNode*)malloc(sizeof(BSTNode));
    if (!newNode) {
        printf("Memory allocation error.\\n");
        exit(1);
    }
    newNode->data = value;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// Insert into BST recursively: O(log n) avg, O(n) worst
BSTNode* insertBST(BSTNode* root, int value) {
    if (root == NULL) {
        return createTreeNode(value);
    }
    if (value < root->data) {
        root->left = insertBST(root->left, value);
    } else if (value > root->data) {
        root->right = insertBST(root->right, value);
    }
    return root;
}

// Search for a key in BST: O(log n) avg
BSTNode* searchBST(BSTNode* root, int target) {
    if (root == NULL || root->data == target) {
        return root;
    }
    if (target < root->data) {
        return searchBST(root->left, target);
    }
    return searchBST(root->right, target);
}

// Inorder traversal (Left, Root, Right) -> Yields ascending sorted order
void inorderTraversal(BSTNode* root) {
    if (root != NULL) {
        inorderTraversal(root->left);
        printf("%d ", root->data);
        inorderTraversal(root->right);
    }
}

// Preorder traversal (Root, Left, Right)
void preorderTraversal(BSTNode* root) {
    if (root != NULL) {
        printf("%d ", root->data);
        preorderTraversal(root->left);
        preorderTraversal(root->right);
    }
}

// Count total leaf nodes (nodes with 0 children)
int countLeafNodes(BSTNode* root) {
    if (root == NULL) return 0;
    if (root->left == NULL && root->right == NULL) return 1;
    return countLeafNodes(root->left) + countLeafNodes(root->right);
}

// Postorder deallocation of tree nodes
void freeTree(BSTNode* root) {
    if (root != NULL) {
        freeTree(root->left);
        freeTree(root->right);
        free(root);
    }
}

int main() {
    printf("========================================\\n");
    printf(" SkillArc — Binary Search Tree (BST) in C\\n");
    printf("========================================\\n\\n");

    BSTNode* root = NULL;
    int keys[] = {50, 30, 70, 20, 40, 60, 80};
    int n = sizeof(keys) / sizeof(keys[0]);

    printf("Inserting keys: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", keys[i]);
        root = insertBST(root, keys[i]);
    }
    printf("\\n\\n");

    printf("Inorder Traversal (Sorted): ");
    inorderTraversal(root);
    printf("\\n");

    printf("Preorder Traversal: ");
    preorderTraversal(root);
    printf("\\n\\n");

    printf("Total Leaf Nodes: %d\\n", countLeafNodes(root));

    // Test Search
    int query = 40;
    BSTNode* found = searchBST(root, query);
    if (found) {
        printf("Search Key %d: FOUND in BST!\\n", query);
    } else {
        printf("Search Key %d: NOT found.\\n", query);
    }

    freeTree(root);
    printf("Tree memory deallocated successfully.\\n");

    return 0;
}
"""
    },
    "Graphs": {
        "concepts": """# Graphs & Graph Traversals in C — Core Concepts

## 1. What is a Graph?
A **Graph** $G = (V, E)$ is a non-linear data structure consisting of:
- **Vertices (Nodes, $V$):** The entities or data points.
- **Edges (Arcs, $E$):** The connections or relationships between pairs of vertices.

### Graph Classifications
1. **Undirected vs Directed (Digraph):** In an undirected graph, edges have no orientation ($A - B$). In a directed graph, edges point from source to destination ($A \\to B$).
2. **Weighted vs Unweighted:** Weighted edges carry a cost, distance, or capacity.
3. **Cyclic vs Acyclic:** A cyclic graph contains at least one path that starts and ends at the same vertex. A Directed Acyclic Graph is called a **DAG**.

---

## 2. Graph Representations

### A. Adjacency Matrix
A 2D array of size $|V| \\times |V|$ where `matrix[u][v] = 1` (or weight) if an edge exists between $u$ and $v$.
- **Space:** $O(V^2)$
- **Edge Lookup:** $O(1)$
- **Best for:** Dense graphs where $|E| \\approx |V|^2$.

### B. Adjacency List
An array of linked lists where index $u$ stores all neighbor vertices connected to $u$.
- **Space:** $O(V + E)$
- **Edge Lookup:** $O(\\text{degree}(u))$
- **Best for:** Sparse graphs (most real-world networks).

---

## 3. Graph Traversal Algorithms

### Breadth-First Search (BFS)
Explores all neighbor vertices at the current depth level before proceeding to vertices at the next depth level.
- **Underlying Data Structure:** **FIFO Queue**.
- **Time Complexity:** $O(V + E)$
- **Primary Use:** Shortest path in unweighted graphs.

### Depth-First Search (DFS)
Explores as deep as possible along each branch before backtracking.
- **Underlying Data Structure:** **LIFO Call Stack** (Recursion).
- **Time Complexity:** $O(V + E)$
- **Primary Use:** Topological sorting, cycle detection, connected components.

---

## 4. Complexity Comparison
| Representation | Space Complexity | Add Vertex | Add Edge | Check Edge $(u, v)$ | BFS / DFS Traversal |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Adjacency Matrix** | $O(V^2)$ | $O(V^2)$ | $O(1)$ | $O(1)$ | $O(V^2)$ |
| **Adjacency List** | $O(V + E)$ | $O(1)$ | $O(1)$ | $O(V)$ | $O(V + E)$ |

---

## 5. Practical Applications
1. **GPS Navigation:** Shortest route calculation (Google Maps using Dijkstra/A* on road graphs).
2. **Social Networks:** Mutual friends recommendations and network connectivity (LinkedIn, Instagram).
3. **Web Crawlers:** Search engine indexers traversing hyperlinks as directed graphs.
4. **Dependency Resolution:** Build systems (Makefiles, npm, pip) resolving DAG package dependencies.

---

## 6. Practice Problems
- **Easy:** Number of connected components; Find path between source and target.
- **Medium:** BFS shortest path in unweighted grid; Detect cycle in directed graph.
- **Hard:** Topological sort of course prerequisites; Dijkstra's algorithm for weighted shortest paths.
""",
        "notes": """/**
 * SkillArc Phase III — Data Structures in C
 * Module: Graph Representation and Traversals (BFS & DFS)
 * Author: Team Apex (Samiksha Gurung, Vaibhavi Thapliyal, Tanisha Rai)
 * Features:
 *  - Adjacency Matrix representation
 *  - Breadth-First Search (BFS) using circular FIFO queue
 *  - Depth-First Search (DFS) using recursion
 *  - Undirected edge insertion
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_VERTICES 10

// Graph structure using Adjacency Matrix
typedef struct {
    int numVertices;
    int adjMatrix[MAX_VERTICES][MAX_VERTICES];
} Graph;

// Initialize graph
void initGraph(Graph* g, int vertices) {
    g->numVertices = vertices;
    for (int i = 0; i < vertices; i++) {
        for (int j = 0; j < vertices; j++) {
            g->adjMatrix[i][j] = 0;
        }
    }
}

// Add undirected edge between u and v
void addEdge(Graph* g, int u, int v) {
    if (u >= 0 && u < g->numVertices && v >= 0 && v < g->numVertices) {
        g->adjMatrix[u][v] = 1;
        g->adjMatrix[v][u] = 1;
    }
}

// Simple Circular Queue for BFS
typedef struct {
    int items[MAX_VERTICES];
    int front;
    int rear;
} Queue;

void initQueue(Queue* q) { q->front = -1; q->rear = -1; }
bool isQueueEmpty(Queue* q) { return q->front == -1; }
void enqueue(Queue* q, int value) {
    if (q->front == -1) q->front = 0;
    q->rear = (q->rear + 1) % MAX_VERTICES;
    q->items[q->rear] = value;
}
int dequeue(Queue* q) {
    int item = q->items[q->front];
    if (q->front == q->rear) {
        q->front = -1;
        q->rear = -1;
    } else {
        q->front = (q->front + 1) % MAX_VERTICES;
    }
    return item;
}

// Breadth-First Search (BFS) from startVertex: O(V^2) for matrix
void BFS(Graph* g, int startVertex) {
    bool visited[MAX_VERTICES] = {false};
    Queue q;
    initQueue(&q);

    visited[startVertex] = true;
    enqueue(&q, startVertex);

    printf("BFS Traversal starting from vertex %d: ", startVertex);

    while (!isQueueEmpty(&q)) {
        int curr = dequeue(&q);
        printf("%d ", curr);

        for (int neighbor = 0; neighbor < g->numVertices; neighbor++) {
            if (g->adjMatrix[curr][neighbor] == 1 && !visited[neighbor]) {
                visited[neighbor] = true;
                enqueue(&q, neighbor);
            }
        }
    }
    printf("\\n");
}

// Recursive Helper for DFS
void DFSRecursive(Graph* g, int curr, bool visited[]) {
    visited[curr] = true;
    printf("%d ", curr);

    for (int neighbor = 0; neighbor < g->numVertices; neighbor++) {
        if (g->adjMatrix[curr][neighbor] == 1 && !visited[neighbor]) {
            DFSRecursive(g, neighbor, visited);
        }
    }
}

// Depth-First Search (DFS) from startVertex: O(V^2) for matrix
void DFS(Graph* g, int startVertex) {
    bool visited[MAX_VERTICES] = {false};
    printf("DFS Traversal starting from vertex %d: ", startVertex);
    DFSRecursive(g, startVertex, visited);
    printf("\\n");
}

int main() {
    printf("========================================\\n");
    printf(" SkillArc — Graph Traversals in C       \\n");
    printf("========================================\\n\\n");

    Graph g;
    initGraph(&g, 6);

    // Creating sample connected graph:
    // 0 - 1, 0 - 2, 1 - 3, 1 - 4, 2 - 4, 3 - 5, 4 - 5
    addEdge(&g, 0, 1);
    addEdge(&g, 0, 2);
    addEdge(&g, 1, 3);
    addEdge(&g, 1, 4);
    addEdge(&g, 2, 4);
    addEdge(&g, 3, 5);
    addEdge(&g, 4, 5);

    printf("Graph successfully constructed with 6 vertices (0 to 5) and 7 edges.\\n\\n");

    BFS(&g, 0);
    DFS(&g, 0);

    return 0;
}
"""
    },
    "Searching": {
        "concepts": """# Searching Algorithms in C — Core Concepts

## 1. What is Searching?
**Searching** is the algorithmic process of locating a specific target key within a collection of data items, returning either its index location or an indicator that the item does not exist.

---

## 2. Linear Search vs Binary Search

### A. Linear Search (Sequential Search)
Scans elements one by one from beginning to end until the match is found or the end of the array is reached.
- **Requirement:** Works on both **unsorted** and **sorted** arrays.
- **Time Complexity:** Best: $O(1)$ (first element), Worst: $O(n)$ (last element or absent).
- **Space Complexity:** $O(1)$

### B. Binary Search (Divide and Conquer)
Repeatedly divides the search interval in half. Compares target with middle element:
1. If `arr[mid] == target`: Found.
2. If `target < arr[mid]`: Search left half (`high = mid - 1`).
3. If `target > arr[mid]`: Search right half (`low = mid + 1`).
- **Prerequisite:** The array **MUST be sorted** in advance.
- **Time Complexity:** Best: $O(1)$, Worst: $O(\log n)$.
- **Space Complexity:** Iterative: $O(1)$, Recursive: $O(\log n)$ call stack frames.

---

## 3. Time & Space Complexity Comparison Table
| Algorithm | Best Case | Average Case | Worst Case | Space Complexity | Array Prerequisite |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Linear Search** | $O(1)$ | $O(n)$ | $O(n)$ | $O(1)$ | None (unsorted ok) |
| **Binary Search (Iterative)** | $O(1)$ | $O(\log n)$ | $O(\log n)$ | $O(1)$ | Must be sorted |
| **Binary Search (Recursive)** | $O(1)$ | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | Must be sorted |

---

## 4. Practical Applications
1. **Symbol Tables:** Compilers searching identifiers and reserved keywords.
2. **Database Queries:** B-Tree index lookups use binary search principles.
3. **Debugging Tools:** `git bisect` uses binary search over commit history to pinpoint regressions.
4. **Dictionary Lookups:** Finding words in alphabetical dictionaries.

---

## 5. Practice Problems
- **Easy:** Linear search element; Binary search on sorted array.
- **Medium:** Find first and last position of element in sorted array; Search in rotated sorted array.
- **Hard:** Median of two sorted arrays ($O(\log(m+n))$); Capacity to ship packages within D days.
""",
        "notes": """/**
 * SkillArc Phase III — Data Structures in C
 * Module: Linear Search and Binary Search (Iterative & Recursive)
 * Author: Team Apex (Samiksha Gurung, Vaibhavi Thapliyal, Tanisha Rai)
 */

#include <stdio.h>

// Linear Search: O(n)
int linearSearch(int arr[], int n, int target) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == target) return i; // Return 0-based index
    }
    return -1; // Not found
}

// Binary Search (Iterative): O(log n)
int binarySearchIterative(int arr[], int n, int target) {
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2; // Prevents integer overflow
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}

// Binary Search (Recursive): O(log n)
int binarySearchRecursive(int arr[], int low, int high, int target) {
    if (low > high) return -1;
    int mid = low + (high - low) / 2;
    if (arr[mid] == target) return mid;
    else if (arr[mid] < target) return binarySearchRecursive(arr, mid + 1, high, target);
    else return binarySearchRecursive(arr, low, mid - 1, target);
}

int main() {
    printf("========================================\\n");
    printf(" SkillArc — Searching Algorithms in C   \\n");
    printf("========================================\\n\\n");

    int sortedArr[] = {12, 24, 35, 47, 53, 68, 79, 88, 95};
    int n = sizeof(sortedArr) / sizeof(sortedArr[0]);
    int target = 68;

    printf("Array: ");
    for (int i = 0; i < n; i++) printf("%d ", sortedArr[i]);
    printf("\\nTarget to search: %d\\n\\n", target);

    // 1. Linear Search
    int linIdx = linearSearch(sortedArr, n, target);
    printf("Linear Search Result: Found at index %d\\n", linIdx);

    // 2. Binary Search (Iterative)
    int binIterIdx = binarySearchIterative(sortedArr, n, target);
    printf("Binary Search (Iterative) Result: Found at index %d\\n", binIterIdx);

    // 3. Binary Search (Recursive)
    int binRecIdx = binarySearchRecursive(sortedArr, 0, n - 1, target);
    printf("Binary Search (Recursive) Result: Found at index %d\\n", binRecIdx);

    return 0;
}
"""
    },
    "Sorting": {
        "concepts": """# Sorting Algorithms in C — Core Concepts

## 1. What is Sorting?
**Sorting** is the algorithmic arrangement of elements in a specific order (ascending or descending). It is a foundational building block for binary search, database indexing, and data presentation.

---

## 2. Core Sorting Algorithms

### A. Bubble Sort
Repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
- **Time:** Best: $O(n)$ (with sorted flag), Worst: $O(n^2)$. Space: $O(1)$. Stable.

### B. Selection Sort
Finds the minimum element from the unsorted segment and puts it at the beginning.
- **Time:** Always $O(n^2)$. Space: $O(1)$. Unstable.

### C. Insertion Sort
Builds the final sorted array one item at a time, inserting each element into its proper position among previously sorted elements.
- **Time:** Best: $O(n)$, Worst: $O(n^2)$. Space: $O(1)$. Stable. Ideal for small or nearly sorted arrays.

### D. Merge Sort (Divide and Conquer)
Divides the array into two halves, recursively sorts them, and merges the two sorted halves back together.
- **Time:** Guaranteed $O(n \log n)$ in all cases. Space: $O(n)$ auxiliary array. Stable.

### E. Quick Sort (Divide and Conquer)
Selects a 'pivot' element and partitions array such that elements smaller than pivot go left, and elements greater go right. Recursively sorts subarrays.
- **Time:** Average: $O(n \log n)$, Worst: $O(n^2)$ (when pivot is poor). Space: $O(\log n)$ call stack. Unstable.

---

## 3. Comprehensive Time & Space Complexity Comparison Table
| Algorithm | Best Case | Average Case | Worst Case | Space Complexity | Stability |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Bubble Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Yes |
| **Selection Sort** | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | No |
| **Insertion Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Yes |
| **Merge Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | Yes |
| **Quick Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(\log n)$ | No |

---

## 4. Practice Problems
- **Easy:** Sort an array using Bubble Sort and count swaps; Insertion sort implementation.
- **Medium:** Merge Sort implementation on arrays and linked lists; Dutch National Flag problem (sort 0s, 1s, 2s).
- **Hard:** Quickselect algorithm ($O(n)$ find $k$-th smallest element); Count inversions in an array.
""",
        "notes": """/**
 * SkillArc Phase III — Data Structures in C
 * Module: Comparison Sorting Algorithms (Bubble, Insertion, Merge, Quick)
 * Author: Team Apex (Samiksha Gurung, Vaibhavi Thapliyal, Tanisha Rai)
 */

#include <stdio.h>
#include <stdlib.h>

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) printf("%d ", arr[i]);
    printf("\\n");
}

// 1. Bubble Sort with early termination flag: O(n) best, O(n^2) worst
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int swapped = 0;
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = 1;
            }
        }
        if (!swapped) break;
    }
}

// 2. Merge Sort: O(n log n) in all cases, O(n) space
void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    int* L = (int*)malloc(n1 * sizeof(int));
    int* R = (int*)malloc(n2 * sizeof(int));

    for (int i = 0; i < n1; i++) L[i] = arr[left + i];
    for (int j = 0; j < n2; j++) R[j] = arr[mid + 1 + j];

    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];

    free(L);
    free(R);
}

void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

// 3. Quick Sort: O(n log n) average, in-place O(log n) stack
int partition(int arr[], int low, int high) {
    int pivot = arr[high]; // Choosing last element as pivot
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;
    return i + 1;
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int main() {
    printf("========================================\\n");
    printf(" SkillArc — Sorting Algorithms in C     \\n");
    printf("========================================\\n\\n");

    int testArr1[] = {64, 34, 25, 12, 22, 11, 90};
    int n1 = sizeof(testArr1) / sizeof(testArr1[0]);
    printf("Original Array: ");
    printArray(testArr1, n1);

    bubbleSort(testArr1, n1);
    printf("After Bubble Sort: ");
    printArray(testArr1, n1);

    int testArr2[] = {38, 27, 43, 3, 9, 82, 10};
    int n2 = sizeof(testArr2) / sizeof(testArr2[0]);
    mergeSort(testArr2, 0, n2 - 1);
    printf("After Merge Sort : ");
    printArray(testArr2, n2);

    int testArr3[] = {10, 80, 30, 90, 40, 50, 70};
    int n3 = sizeof(testArr3) / sizeof(testArr3[0]);
    quickSort(testArr3, 0, n3 - 1);
    printf("After Quick Sort : ");
    printArray(testArr3, n3);

    return 0;
}
"""
    },
    "Hashing": {
        "concepts": """# Hashing & Collision Handling in C — Core Concepts

## 1. What is Hashing?
**Hashing** is a technique used to map a large range of data keys into a fixed-size table (called a **Hash Table**) using a mathematical transformation called a **Hash Function**.
$$\\text{Index} = \\text{HashFunction}(\\text{Key}) \\pmod{\\text{TableSize}}$$
This technique provides average constant time **$O(1)$** for search, insert, and delete operations.

---

## 2. Hash Collisions & Resolution Strategies
A **collision** occurs when two distinct keys produce the exact same index:
$$h(k_1) = h(k_2) \\quad \\text{where } k_1 \\neq k_2$$

### Strategy 1: Open Addressing (Closed Hashing)
All elements are stored directly inside the hash table array itself. When a collision occurs, we probe for the next available empty slot.
- **Linear Probing:** $h(k, i) = (h'(k) + i) \\pmod m$. Subject to *primary clustering*.
- **Quadratic Probing:** $h(k, i) = (h'(k) + c_1 i + c_2 i^2) \\pmod m$. Solves primary clustering.
- **Double Hashing:** Uses a secondary hash function $h(k, i) = (h_1(k) + i \\cdot h_2(k)) \\pmod m$.

### Strategy 2: Separate Chaining (Open Hashing)
Each slot of the hash table points to a linked list of entries that hashed to that same bucket index.
- Clean and simple; table never becomes "full".
- Memory overhead for pointers.

---

## 3. Time Complexity
| Operation | Average Case | Worst Case (All keys collide) | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Search** | $O(1)$ | $O(n)$ | $O(m + n)$ |
| **Insert** | $O(1)$ | $O(n)$ | $O(m + n)$ |
| **Delete** | $O(1)$ | $O(n)$ | $O(m + n)$ |

---

## 4. Practice Problems
- **Easy:** Implement a direct-address table; Count frequency of elements using hashing.
- **Medium:** Implement Hash Table with Linear Probing; Longest consecutive sequence ($O(n)$).
- **Hard:** Design an LRU (Least Recently Used) cache combining Hash Map + Doubly Linked List.
""",
        "notes": """/**
 * SkillArc Phase III — Data Structures in C
 * Module: Hash Table with Linear Probing Collision Resolution
 * Author: Team Apex (Samiksha Gurung, Vaibhavi Thapliyal, Tanisha Rai)
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define TABLE_SIZE 10
#define EMPTY -1
#define DELETED -2

typedef struct {
    int key;
    int value;
} HashEntry;

typedef struct {
    HashEntry table[TABLE_SIZE];
    int size;
} HashTable;

void initHashTable(HashTable* ht) {
    ht->size = 0;
    for (int i = 0; i < TABLE_SIZE; i++) {
        ht->table[i].key = EMPTY;
        ht->table[i].value = 0;
    }
}

int hashFunction(int key) {
    return (key % TABLE_SIZE + TABLE_SIZE) % TABLE_SIZE;
}

// Insert key-value pair using linear probing: O(1) avg
bool insert(HashTable* ht, int key, int value) {
    if (ht->size == TABLE_SIZE) {
        printf("Hash table overflow!\\n");
        return false;
    }
    int index = hashFunction(key);
    while (ht->table[index].key != EMPTY && ht->table[index].key != DELETED && ht->table[index].key != key) {
        index = (index + 1) % TABLE_SIZE; // Linear probe
    }
    ht->table[index].key = key;
    ht->table[index].value = value;
    ht->size++;
    return true;
}

// Search key in hash table: O(1) avg
int search(HashTable* ht, int key) {
    int index = hashFunction(key);
    int start = index;
    while (ht->table[index].key != EMPTY) {
        if (ht->table[index].key == key) {
            return ht->table[index].value;
        }
        index = (index + 1) % TABLE_SIZE;
        if (index == start) break;
    }
    return -1; // Not found
}

void printTable(HashTable* ht) {
    printf("Slot | Key    | Value\\n");
    printf("---------------------\\n");
    for (int i = 0; i < TABLE_SIZE; i++) {
        if (ht->table[i].key == EMPTY) printf("[%2d] | EMPTY  | -\\n", i);
        else if (ht->table[i].key == DELETED) printf("[%2d] | DELETED| -\\n", i);
        else printf("[%2d] | %-6d | %d\\n", i, ht->table[i].key, ht->table[i].value);
    }
}

int main() {
    printf("========================================\\n");
    printf(" SkillArc — Hash Table (Linear Probing) \\n");
    printf("========================================\\n\\n");

    HashTable ht;
    initHashTable(&ht);

    insert(&ht, 15, 100);
    insert(&ht, 25, 200); // Collides with 15 (both 15%10 and 25%10 are 5) -> probes to 6
    insert(&ht, 35, 300); // Collides with 15 & 25 -> probes to 7
    insert(&ht, 12, 400);

    printTable(&ht);

    printf("\\nSearching for key 25: Value = %d\\n", search(&ht, 25));
    printf("Searching for key 99: Value = %d (not found)\\n", search(&ht, 99));

    return 0;
}
"""
    },
    "Advanced_DSA": {
        "concepts": """# Advanced DSA Concepts in C — Pointers, DMA, Recursion & Applications

## 1. Dynamic Memory Allocation (DMA) in C
In C, variables declared in functions are stored on the **Call Stack** and deallocated when the function returns. Dynamic memory is allocated at runtime from the **Heap** using standard library functions (`<stdlib.h>`):
- `malloc(size_t size)`: Allocates uninitialized memory. Returns `void*` or `NULL`.
- `calloc(size_t num, size_t size)`: Allocates memory and initializes all bytes to zero.
- `realloc(void* ptr, size_t new_size)`: Resizes previously allocated block.
- `free(void* ptr)`: Releases allocated memory back to the heap. Avoids **Memory Leaks**.

---

## 2. Pointers & Memory Management
- **Pointer:** A variable storing the memory address of another variable (`int* ptr = &val;`).
- **Dangling Pointer:** A pointer pointing to memory that has already been deallocated by `free()`.
- **Memory Leak:** Allocating memory with `malloc()` without ever calling `free()`.

---

## 3. Recursion & The Call Stack
A recursive function calls itself to solve smaller subproblems until a **base case** is reached. Every recursive call pushes an activation record onto the process Call Stack.

---

## 4. Sparse Matrices
A **Sparse Matrix** is a matrix in which the majority of elements are zero. Storing all zeros wastes significant memory.
- **3-Tuple Representation:** Each non-zero element is stored as `(Row, Column, Value)`.
- Reduces space from $O(R \times C)$ down to $O(\text{NonZeroCount})$.

---

## 5. Expression Conversion (Infix, Prefix, Postfix)
Using Stacks for compiler arithmetic parsing:
- **Infix:** `A + B * C` (Human readable)
- **Postfix (RPN):** `A B C * +` (No parentheses required, evaluated linearly with stack)
""",
        "notes": """/**
 * SkillArc Phase III — Data Structures in C
 * Module: Dynamic Memory Allocation and Infix-to-Postfix Stack Conversion
 * Author: Team Apex (Samiksha Gurung, Vaibhavi Thapliyal, Tanisha Rai)
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Stack for operator conversion
typedef struct {
    char* items;
    int top;
    int capacity;
} CharStack;

CharStack* createStack(int cap) {
    CharStack* s = (CharStack*)malloc(sizeof(CharStack));
    s->capacity = cap;
    s->top = -1;
    s->items = (char*)malloc(cap * sizeof(char));
    return s;
}

void push(CharStack* s, char c) { s->items[++s->top] = c; }
char pop(CharStack* s) { return s->items[s->top--]; }
char peek(CharStack* s) { return s->items[s->top]; }
int isEmpty(CharStack* s) { return s->top == -1; }

int precedence(char op) {
    if (op == '+' || op == '-') return 1;
    if (op == '*' || op == '/') return 2;
    if (op == '^') return 3;
    return 0;
}

// Convert Infix to Postfix expression
void infixToPostfix(const char* infix, char* postfix) {
    int len = strlen(infix);
    CharStack* s = createStack(len + 1);
    int k = 0;

    for (int i = 0; i < len; i++) {
        char ch = infix[i];
        if (isalnum(ch)) {
            postfix[k++] = ch;
        } else if (ch == '(') {
            push(s, ch);
        } else if (ch == ')') {
            while (!isEmpty(s) && peek(s) != '(') {
                postfix[k++] = pop(s);
            }
            if (!isEmpty(s)) pop(s); // Remove '('
        } else {
            // Operator
            while (!isEmpty(s) && precedence(peek(s)) >= precedence(ch)) {
                postfix[k++] = pop(s);
            }
            push(s, ch);
        }
    }
    while (!isEmpty(s)) {
        postfix[k++] = pop(s);
    }
    postfix[k] = '\\0';
    free(s->items);
    free(s);
}

int main() {
    printf("========================================\\n");
    printf(" SkillArc — Infix to Postfix Conversion \\n");
    printf("========================================\\n\\n");

    const char* infix = "A+(B*C-(D/E^F)*G)*H";
    char postfix[100];

    infixToPostfix(infix, postfix);

    printf("Infix Expression   : %s\\n", infix);
    printf("Postfix Expression : %s\\n", postfix);

    return 0;
}
"""
    }
}

# -----------------------------------------------------------------------------
# OOPS MODULES CONTENT
# -----------------------------------------------------------------------------
MODULES_OOPS = {
    "CPP_Fundamentals": {
        "concepts": """# C++ Fundamentals & Functions — Core Concepts

## 1. Evolution from C to C++
C++ was developed by Bjarne Stroustrup at Bell Labs as "C with Classes". It incorporates both procedural systems programming and the object-oriented paradigm.

---

## 2. Namespaces & Standard I/O
The `std` namespace prevents name collisions in large programs.
```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Standard output with cout" << endl;
    return 0;
}
```

---

## 3. Function Overloading & Default Arguments
- **Function Overloading:** Multiple functions can share the exact same name as long as their parameter lists (signatures) differ by count or type.
- **Default Arguments:** Default parameter values are specified in the function declaration.
- **Inline Functions:** The `inline` keyword suggests the compiler replace function calls with the actual function body to eliminate call overhead for small routines.
""",
        "notes": """/**
 * SkillArc Phase III — OOP in C++
 * Module: C++ Fundamentals, Namespaces, Overloading & Inline Functions
 * Author: Team Apex (Samiksha Gurung, Vaibhavi Thapliyal, Tanisha Rai)
 */

#include <iostream>
#include <string>

using namespace std;

// Inline function definition
inline int square(int x) {
    return x * x;
}

// Function Overloading: Same name 'calculateArea', different parameter signatures
double calculateArea(double radius) {
    return 3.14159 * radius * radius;
}

double calculateArea(double length, double width) {
    return length * width;
}

// Default Arguments: 'discount' defaults to 0.05 (5%)
double computeTotal(double price, int qty, double discount = 0.05) {
    double subtotal = price * qty;
    return subtotal * (1.0 - discount);
}

int main() {
    cout << "========================================" << endl;
    cout << " SkillArc — C++ Fundamentals Showcase   " << endl;
    cout << "========================================" << endl << endl;

    cout << "Inline Square of 9: " << square(9) << endl;

    cout << "Area of Circle (r=5.0)    : " << calculateArea(5.0) << endl;
    cout << "Area of Rectangle (4x6)   : " << calculateArea(4.0, 6.0) << endl;

    cout << "Order Total (default 5% disc): $" << computeTotal(100.0, 2) << endl;
    cout << "Order Total (custom 15% disc): $" << computeTotal(100.0, 2, 0.15) << endl;

    return 0;
}
"""
    },
    "Exception_FileIO": {
        "concepts": """# Exception Handling & File I/O in C++ — Core Concepts

## 1. Exception Handling (`try`, `catch`, `throw`)
C++ provides structured runtime error handling to prevent unexpected application crashes:
- `try`: Encloses code that might trigger an exceptional condition.
- `throw`: Signals an anomaly or error state.
- `catch`: Intercepts and resolves the thrown exception.

---

## 2. File Input/Output Streams
C++ uses stream classes declared in `<fstream>`:
- `ifstream`: Input file stream for reading data.
- `ofstream`: Output file stream for writing data.
- `fstream`: Bidirectional file stream for simultaneous reading and writing.
""",
        "notes": """/**
 * SkillArc Phase III — OOP in C++
 * Module: Exception Handling and File Streams (ifstream, ofstream)
 * Author: Team Apex (Samiksha Gurung, Vaibhavi Thapliyal, Tanisha Rai)
 */

#include <iostream>
#include <fstream>
#include <string>
#include <stdexcept>

using namespace std;

// Function demonstrating Exception Handling
double safeDivide(double numerator, double denominator) {
    if (denominator == 0.0) {
        throw runtime_error("Math Error: Division by zero is undefined!");
    }
    return numerator / denominator;
}

// Function demonstrating File Writing and Reading
void demonstrateFileIO() {
    string filename = "skillarc_log.txt";

    // 1. Writing to a file using ofstream
    ofstream outFile(filename);
    if (!outFile) {
        cerr << "Error opening file for write!" << endl;
        return;
    }
    outFile << "SKILLARC SYSTEM AUDIT LOG" << endl;
    outFile << "Student: Samiksha Gurung (2510370150) | Topic: Linked Lists | Score: 100%" << endl;
    outFile << "Student: Vaibhavi Thapliyal (2510370530) | Topic: Trees | Score: 100%" << endl;
    outFile << "Student: Tanisha Rai (2510370080) | Topic: STL | Score: 100%" << endl;
    outFile.close();
    cout << "[OK] File '" << filename << "' written successfully." << endl;

    // 2. Reading back using ifstream
    ifstream inFile(filename);
    if (!inFile) {
        cerr << "Error opening file for read!" << endl;
        return;
    }
    cout << "\\n--- Reading Contents of " << filename << " ---" << endl;
    string line;
    while (getline(inFile, line)) {
        cout << "  " << line << endl;
    }
    inFile.close();
}

int main() {
    cout << "========================================" << endl;
    cout << " SkillArc — Exception & File I/O Engine " << endl;
    cout << "========================================" << endl << endl;

    // Exception handling demo
    try {
        cout << "10 / 2 = " << safeDivide(10, 2) << endl;
        cout << "Attempting 10 / 0..." << endl;
        cout << safeDivide(10, 0) << endl;
    } catch (const exception& e) {
        cout << "[CAUGHT EXCEPTION] " << e.what() << endl;
    }

    cout << endl;
    demonstrateFileIO();

    return 0;
}
"""
    },
    "Templates_STL": {
        "concepts": """# Templates & Standard Template Library (STL) in C++ — Core Concepts

## 1. What are Templates?
**Templates** enable generic programming in C++, allowing functions and classes to operate with generic types without duplicating code for `int`, `double`, `string`, etc.
- **Function Templates:** `template <typename T> T findMax(T a, T b)`
- **Class Templates:** `template <class T> class Stack { ... }`

---

## 2. Standard Template Library (STL) Architecture
The STL consists of four foundational pillars:
1. **Containers:** Data structures storing objects (`vector`, `list`, `deque`, `set`, `map`, `unordered_map`, `stack`, `queue`, `priority_queue`).
2. **Iterators:** Pointer-like abstractions that traverse container elements (`begin()`, `end()`).
3. **Algorithms:** Pre-optimized algorithms for searching, sorting, counting (`std::sort`, `std::binary_search`).
4. **Functors:** Function objects acting as callbacks.
""",
        "notes": """/**
 * SkillArc Phase III — OOP in C++
 * Module: Templates and STL (vector, map, priority_queue, algorithms)
 * Author: Team Apex (Samiksha Gurung, Vaibhavi Thapliyal, Tanisha Rai)
 */

#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>

using namespace std;

// 1. Generic Function Template
template <typename T>
T findMax(T a, T b) {
    return (a > b) ? a : b;
}

int main() {
    cout << "========================================" << endl;
    cout << " SkillArc — Templates & STL Engine      " << endl;
    cout << "========================================" << endl << endl;

    // Test Function Template
    cout << "findMax(15, 29)          : " << findMax(15, 29) << endl;
    cout << "findMax(3.1415, 2.7182)   : " << findMax(3.1415, 2.7182) << endl;
    cout << "findMax(string(\"Alpha\"), string(\"Omega\")): " << findMax(string("Alpha"), string("Omega")) << endl << endl;

    // STL Vector & Algorithm (std::sort)
    vector<int> scores = {95, 40, 85, 100, 60, 75};
    cout << "Original Scores : ";
    for (int s : scores) cout << s << " ";
    cout << endl;

    sort(scores.begin(), scores.end());
    cout << "Sorted Scores   : ";
    for (int s : scores) cout << s << " ";
    cout << endl << endl;

    // STL Map: Key-Value association
    map<string, int> studentCredits;
    studentCredits["Samiksha Gurung"] = 140;
    studentCredits["Vaibhavi Thapliyal"] = 160;
    studentCredits["Tanisha Rai"] = 165;

    cout << "Student Credits Directory (STL Map):" << endl;
    for (const auto& pair : studentCredits) {
        cout << "  • " << pair.first << " : " << pair.second << " pts" << endl;
    }

    return 0;
}
"""
    }
}

# Write DSA files
for topic_id, data in MODULES_DSA.items():
    topic_dir = DSA_DIR / topic_id
    topic_dir.mkdir(parents=True, exist_ok=True)
    with open(topic_dir / "concepts.md", "w", encoding="utf-8") as f:
        f.write(data["concepts"])
    with open(topic_dir / "notes.md", "w", encoding="utf-8") as f:
        f.write(data["notes"])
    # Also write standalone C file to Phase-3/DSA/
    with open(PHASE3_DSA / f"{topic_id.lower()}.c", "w", encoding="utf-8") as f:
        f.write(data["notes"])
    print(f"Created DSA module: {topic_id}")

# Write OOPS files
for topic_id, data in MODULES_OOPS.items():
    topic_dir = OOPS_DIR / topic_id
    topic_dir.mkdir(parents=True, exist_ok=True)
    with open(topic_dir / "concepts.md", "w", encoding="utf-8") as f:
        f.write(data["concepts"])
    with open(topic_dir / "notes.md", "w", encoding="utf-8") as f:
        f.write(data["notes"])
    # Also write standalone C++ file to Phase-3/OOPS/
    with open(PHASE3_OOPS / f"{topic_id.lower()}.cpp", "w", encoding="utf-8") as f:
        f.write(data["notes"])
    print(f"Created OOP module: {topic_id}")

print("All learning module files generated successfully!")

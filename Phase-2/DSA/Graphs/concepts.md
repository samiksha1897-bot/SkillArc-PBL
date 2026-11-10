# Graphs & Graph Traversals in C — Core Concepts

## 1. What is a Graph?
A **Graph** $G = (V, E)$ is a non-linear data structure consisting of:
- **Vertices (Nodes, $V$):** The entities or data points.
- **Edges (Arcs, $E$):** The connections or relationships between pairs of vertices.

### Graph Classifications
1. **Undirected vs Directed (Digraph):** In an undirected graph, edges have no orientation ($A - B$). In a directed graph, edges point from source to destination ($A \to B$).
2. **Weighted vs Unweighted:** Weighted edges carry a cost, distance, or capacity.
3. **Cyclic vs Acyclic:** A cyclic graph contains at least one path that starts and ends at the same vertex. A Directed Acyclic Graph is called a **DAG**.

---

## 2. Graph Representations

### A. Adjacency Matrix
A 2D array of size $|V| \times |V|$ where `matrix[u][v] = 1` (or weight) if an edge exists between $u$ and $v$.
- **Space:** $O(V^2)$
- **Edge Lookup:** $O(1)$
- **Best for:** Dense graphs where $|E| \approx |V|^2$.

### B. Adjacency List
An array of linked lists where index $u$ stores all neighbor vertices connected to $u$.
- **Space:** $O(V + E)$
- **Edge Lookup:** $O(\text{degree}(u))$
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

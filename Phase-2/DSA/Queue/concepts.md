# Queue Data Structure in C — Core Concepts

## 1. What is a Queue?
A **Queue** is a linear data structure that adheres to the **FIFO (First In, First Out)** principle. The element inserted first is the first one to be removed.

Analogy: A line of students waiting at a college ticket counter — the person who arrives first gets served first.

---

## 2. Core Queue Terminology & Operations
A queue uses two separate indices or pointers:
- **`front`:** Points to the position of the first (oldest) element.
- **`rear`:** Points to the position of the last (newest) element.

### Primary Operations:
1. **`enqueue(element)`:** Inserts an element at the `rear` end.
2. **`dequeue()`:** Removes and returns the element at the `front` end.
3. **`peek()` / `frontElement()`:** Retrieves the front element without deleting it.
4. **`isEmpty()`:** Checks if `front == -1` or `front > rear`.
5. **`isFull()`:** Checks if `rear == MAX - 1` (in linear queues).

---

## 3. The False Overflow Problem & Circular Queues
In a standard **Linear Queue**, as elements are enqueued and dequeued, the `front` pointer moves forward. Eventually, `rear` reaches `MAX - 1`, triggering an "Overflow" error even if free memory slots exist at the beginning!

### Solution: Circular Queue
A **Circular Queue** connects the last position back to the first position in a ring-like structure using the modulo operator:
$$\text{Next Position} = (\text{Current Position} + 1) \pmod{\text{MAX}}$$

---

## 4. Complexity Analysis
| Operation | Linear Queue | Circular Queue | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Enqueue** | $O(1)$ | $O(1)$ | $O(1)$ |
| **Dequeue** | $O(1)$ | $O(1)$ | $O(1)$ |
| **Peek / Front** | $O(1)$ | $O(1)$ | $O(1)$ |
| **isEmpty / isFull** | $O(1)$ | $O(1)$ | $O(1)$ |

---

## 5. Applications of Queues
1. **CPU Process Scheduling:** Round Robin and First-Come-First-Served (FCFS) process queues in Operating Systems.
2. **Print Spooling:** Print jobs sent to a shared college printer are queued in FIFO order.
3. **Graph Algorithms:** Breadth-First Search (BFS) graph traversal uses a queue.
4. **Network Buffering:** Routers and packet switches queue data packets during traffic bursts.
5. **Keyboard Buffer:** Keystrokes typed by a user are held in an asynchronous queue buffer until processed.
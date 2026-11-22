# Stack Data Structure in C — Core Concepts

## 1. What is a Stack?
A **Stack** is a linear data structure that follows the **LIFO (Last In, First Out)** principle. The element that is inserted last is the first one to be removed.

Imagine a stack of cafeteria plates: you can only place a new plate on top, and you can only take a plate from the top.

---

## 2. Core Operations
All operations in a stack are performed at one designated end called the **Top**:

1. **`push(element)`:** Adds an element to the top of the stack.
2. **`pop()`:** Removes and returns the top element of the stack.
3. **`peek()` / `top()`:** Returns the top element without removing it.
4. **`isEmpty()`:** Checks if the stack contains no elements.
5. **`isFull()`:** Checks if the stack has reached its maximum allocated capacity (in array implementations).

---

## 3. Boundary Conditions
- **Stack Overflow:** Occurs when an attempt is made to `push` an item onto an already full stack (`top == MAX - 1`).
- **Stack Underflow:** Occurs when an attempt is made to `pop` or `peek` an item from an empty stack (`top == -1`).

---

## 4. Complexity Analysis
| Operation | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **Push** | $O(1)$ | $O(1)$ |
| **Pop** | $O(1)$ | $O(1)$ |
| **Peek / Top** | $O(1)$ | $O(1)$ |
| **isEmpty / isFull** | $O(1)$ | $O(1)$ |

Every primary stack operation executes in constant time $O(1)$ because no shifting of elements is required.

---

## 5. Real-World & Computer Science Applications
1. **Function Call Stack:** The CPU uses a runtime stack to store return addresses and local variables during nested or recursive function calls.
2. **Expression Evaluation & Conversion:** Infix to Postfix/Prefix conversion and expression evaluation (using Dijkstra's Shunting-yard algorithm).
3. **Backtracking Algorithms:** Depth-First Search (DFS), maze solving, and game move undo systems.
4. **Parentheses Matching:** Validating syntactically balanced brackets in source code compilers (`{ [ ( ) ] }`).
5. **Undo / Redo Operations:** Text editors maintain undo and redo stacks.
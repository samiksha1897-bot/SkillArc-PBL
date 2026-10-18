# Arrays in C — Core Concepts

## 1. What is an Array?
An **array** is a linear data structure that stores a collection of elements of the same data type in contiguous memory locations. Each element can be directly accessed using its numerical index.

```c
// Declaration of an integer array of size 5
int arr[5] = {10, 20, 30, 40, 50};
```

---

## 2. Memory Representation
Arrays are stored sequentially in RAM:
- If `arr[0]` is at memory address `1000`, and `sizeof(int) == 4` bytes:
  - `arr[0]` -> Address `1000`
  - `arr[1]` -> Address `1004`
  - `arr[2]` -> Address `1008`
  - `arr[3]` -> Address `1012`
  - `arr[4]` -> Address `1016`

**Address Formula:**
$$\text{Address of } arr[i] = \text{Base Address} + (i \times \text{Size of Data Type})$$

---

## 3. Time & Space Complexity
| Operation | Average Case | Worst Case | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Access by Index** | $O(1)$ | $O(1)$ | $O(1)$ |
| **Search (Linear)** | $O(n)$ | $O(n)$ | $O(1)$ |
| **Search (Binary - Sorted)** | $O(\log n)$ | $O(\log n)$ | $O(1)$ |
| **Insertion at End** | $O(1)$ | $O(1)$ | $O(1)$ |
| **Insertion at Position** | $O(n)$ | $O(n)$ | $O(1)$ |
| **Deletion at Position** | $O(n)$ | $O(n)$ | $O(1)$ |

---

## 4. Key Advantages & Limitations
### Advantages:
1. **Random Access:** Any element can be accessed in constant time $O(1)$ using its index.
2. **Memory Efficiency:** Minimal memory overhead since no pointers are stored between elements.
3. **Cache Friendliness:** Contiguous memory layout benefits from CPU spatial cache locality.

### Limitations:
1. **Fixed Size:** Size must be known at compile-time or dynamic allocation time; cannot easily grow or shrink.
2. **Expensive Insertions/Deletions:** Inserting or deleting an element requires shifting subsequent elements ($O(n)$ time).
3. **Contiguous Allocation Requirement:** Large arrays require a contiguous block of free memory, which may cause fragmentation issues.

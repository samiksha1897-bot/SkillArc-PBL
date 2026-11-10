# Hashing & Collision Handling in C — Core Concepts

## 1. What is Hashing?
**Hashing** is a technique used to map a large range of data keys into a fixed-size table (called a **Hash Table**) using a mathematical transformation called a **Hash Function**.
$$\text{Index} = \text{HashFunction}(\text{Key}) \pmod{\text{TableSize}}$$
This technique provides average constant time **$O(1)$** for search, insert, and delete operations.

---

## 2. Hash Collisions & Resolution Strategies
A **collision** occurs when two distinct keys produce the exact same index:
$$h(k_1) = h(k_2) \quad \text{where } k_1 \neq k_2$$

### Strategy 1: Open Addressing (Closed Hashing)
All elements are stored directly inside the hash table array itself. When a collision occurs, we probe for the next available empty slot.
- **Linear Probing:** $h(k, i) = (h'(k) + i) \pmod m$. Subject to *primary clustering*.
- **Quadratic Probing:** $h(k, i) = (h'(k) + c_1 i + c_2 i^2) \pmod m$. Solves primary clustering.
- **Double Hashing:** Uses a secondary hash function $h(k, i) = (h_1(k) + i \cdot h_2(k)) \pmod m$.

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

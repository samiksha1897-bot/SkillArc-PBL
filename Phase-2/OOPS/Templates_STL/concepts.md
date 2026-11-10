# Templates & Standard Template Library (STL) in C++ — Core Concepts

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

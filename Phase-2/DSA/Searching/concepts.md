# Searching Algorithms in C — Core Concepts

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

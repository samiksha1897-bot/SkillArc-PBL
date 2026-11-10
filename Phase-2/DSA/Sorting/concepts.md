# Sorting Algorithms in C — Core Concepts

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

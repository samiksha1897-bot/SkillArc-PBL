# Advanced DSA Concepts in C — Pointers, DMA, Recursion & Applications

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
- Reduces space from $O(R 	imes C)$ down to $O(	ext{NonZeroCount})$.

---

## 5. Expression Conversion (Infix, Prefix, Postfix)
Using Stacks for compiler arithmetic parsing:
- **Infix:** `A + B * C` (Human readable)
- **Postfix (RPN):** `A B C * +` (No parentheses required, evaluated linearly with stack)

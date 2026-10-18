# Arrays in C — Quick Notes & Code Examples

## Quick Revision Notes
1. **0-indexed:** In C, array indexing starts from `0` and ends at `n - 1`.
2. **Bounds Checking:** C does **not** perform boundary checking on array indices. Accessing `arr[10]` on a 5-element array leads to undefined behavior.
3. **Array Decays to Pointer:** When passed into a function, an array decays to a pointer to its first element:
   ```c
   void printArray(int arr[], int size); // Equivalent to: void printArray(int *arr, int size)
   ```

---

## C Implementation: Traversal, Insertion & Deletion

```c
#include <stdio.h>

#define MAX_SIZE 100

// Function to traverse and display elements
void display(int arr[], int size) {
    printf("Array elements: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// Function to insert an element at a specified position (1-based index)
int insertAt(int arr[], int *size, int element, int pos) {
    if (*size >= MAX_SIZE) {
        printf("Error: Array Overflow!\n");
        return 0;
    }
    if (pos < 1 || pos > *size + 1) {
        printf("Error: Invalid position!\n");
        return 0;
    }

    // Shift elements to the right
    for (int i = *size; i >= pos; i--) {
        arr[i] = arr[i - 1];
    }
    arr[pos - 1] = element;
    (*size)++;
    return 1;
}

// Function to delete an element from a specified position
int deleteAt(int arr[], int *size, int pos) {
    if (*size <= 0) {
        printf("Error: Array Underflow!\n");
        return 0;
    }
    if (pos < 1 || pos > *size) {
        printf("Error: Invalid position!\n");
        return 0;
    }

    // Shift elements to the left
    for (int i = pos - 1; i < *size - 1; i++) {
        arr[i] = arr[i + 1];
    }
    (*size)--;
    return 1;
}

int main() {
    int arr[MAX_SIZE] = {12, 24, 36, 48};
    int size = 4;

    display(arr, size);
    
    // Insert 99 at position 3
    insertAt(arr, &size, 99, 3);
    printf("After inserting 99 at pos 3:\n");
    display(arr, size);

    // Delete element at position 2
    deleteAt(arr, &size, 2);
    printf("After deleting element at pos 2:\n");
    display(arr, size);

    return 0;
}
```

---

## Practical Applications of Arrays
- Implementing other data structures: Stacks, Queues, Hash Tables, Heaps.
- Lookup tables and coefficient matrices in scientific computation.
- Buffer storage in I/O operations and audio/video streaming.

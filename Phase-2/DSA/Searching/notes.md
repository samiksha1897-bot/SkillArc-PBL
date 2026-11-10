/**
 * SkillArc Phase III — Data Structures in C
 * Module: Linear Search and Binary Search (Iterative & Recursive)
 * Author: Team Apex (Samiksha Gurung, Vaibhavi Thapliyal, Tanisha Rai)
 */

#include <stdio.h>

// Linear Search: O(n)
int linearSearch(int arr[], int n, int target) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == target) return i; // Return 0-based index
    }
    return -1; // Not found
}

// Binary Search (Iterative): O(log n)
int binarySearchIterative(int arr[], int n, int target) {
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2; // Prevents integer overflow
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}

// Binary Search (Recursive): O(log n)
int binarySearchRecursive(int arr[], int low, int high, int target) {
    if (low > high) return -1;
    int mid = low + (high - low) / 2;
    if (arr[mid] == target) return mid;
    else if (arr[mid] < target) return binarySearchRecursive(arr, mid + 1, high, target);
    else return binarySearchRecursive(arr, low, mid - 1, target);
}

int main() {
    printf("========================================\n");
    printf(" SkillArc — Searching Algorithms in C   \n");
    printf("========================================\n\n");

    int sortedArr[] = {12, 24, 35, 47, 53, 68, 79, 88, 95};
    int n = sizeof(sortedArr) / sizeof(sortedArr[0]);
    int target = 68;

    printf("Array: ");
    for (int i = 0; i < n; i++) printf("%d ", sortedArr[i]);
    printf("\nTarget to search: %d\n\n", target);

    // 1. Linear Search
    int linIdx = linearSearch(sortedArr, n, target);
    printf("Linear Search Result: Found at index %d\n", linIdx);

    // 2. Binary Search (Iterative)
    int binIterIdx = binarySearchIterative(sortedArr, n, target);
    printf("Binary Search (Iterative) Result: Found at index %d\n", binIterIdx);

    // 3. Binary Search (Recursive)
    int binRecIdx = binarySearchRecursive(sortedArr, 0, n - 1, target);
    printf("Binary Search (Recursive) Result: Found at index %d\n", binRecIdx);

    return 0;
}

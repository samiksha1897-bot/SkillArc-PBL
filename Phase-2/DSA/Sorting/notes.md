/**
 * SkillArc Phase III — Data Structures in C
 * Module: Comparison Sorting Algorithms (Bubble, Insertion, Merge, Quick)
 * Author: Team Apex (Samiksha Gurung, Vaibhavi Thapliyal, Tanisha Rai)
 */

#include <stdio.h>
#include <stdlib.h>

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) printf("%d ", arr[i]);
    printf("\n");
}

// 1. Bubble Sort with early termination flag: O(n) best, O(n^2) worst
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int swapped = 0;
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = 1;
            }
        }
        if (!swapped) break;
    }
}

// 2. Merge Sort: O(n log n) in all cases, O(n) space
void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    int* L = (int*)malloc(n1 * sizeof(int));
    int* R = (int*)malloc(n2 * sizeof(int));

    for (int i = 0; i < n1; i++) L[i] = arr[left + i];
    for (int j = 0; j < n2; j++) R[j] = arr[mid + 1 + j];

    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];

    free(L);
    free(R);
}

void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

// 3. Quick Sort: O(n log n) average, in-place O(log n) stack
int partition(int arr[], int low, int high) {
    int pivot = arr[high]; // Choosing last element as pivot
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;
    return i + 1;
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int main() {
    printf("========================================\n");
    printf(" SkillArc — Sorting Algorithms in C     \n");
    printf("========================================\n\n");

    int testArr1[] = {64, 34, 25, 12, 22, 11, 90};
    int n1 = sizeof(testArr1) / sizeof(testArr1[0]);
    printf("Original Array: ");
    printArray(testArr1, n1);

    bubbleSort(testArr1, n1);
    printf("After Bubble Sort: ");
    printArray(testArr1, n1);

    int testArr2[] = {38, 27, 43, 3, 9, 82, 10};
    int n2 = sizeof(testArr2) / sizeof(testArr2[0]);
    mergeSort(testArr2, 0, n2 - 1);
    printf("After Merge Sort : ");
    printArray(testArr2, n2);

    int testArr3[] = {10, 80, 30, 90, 40, 50, 70};
    int n3 = sizeof(testArr3) / sizeof(testArr3[0]);
    quickSort(testArr3, 0, n3 - 1);
    printf("After Quick Sort : ");
    printArray(testArr3, n3);

    return 0;
}

/**
 * SkillArc Phase III — Data Structures in C
 * Module: Singly Linked List Implementation
 * Author: Team Apex (Samiksha Gurung, Vaibhavi Thapliyal, Tanisha Rai)
 * Features:
 *  - Dynamic node creation using malloc()
 *  - Insertion at beginning and end
 *  - Linear traversal and searching
 *  - In-place iterative list reversal
 *  - Safe memory cleanup with free()
 */

#include <stdio.h>
#include <stdlib.h>

// Definition of a Singly Linked List Node
typedef struct Node {
    int data;
    struct Node* next;
} Node;

// Function to allocate a new node dynamically on the heap
Node* createNode(int value) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (newNode == NULL) {
        printf("Error: Memory allocation failed!\n");
        exit(1);
    }
    newNode->data = value;
    newNode->next = NULL;
    return newNode;
}

// Insert a new element at the beginning (Head) of the list: O(1) time
void insertAtHead(Node** headRef, int value) {
    Node* newNode = createNode(value);
    newNode->next = *headRef;
    *headRef = newNode;
    printf("Inserted %d at head.\n", value);
}

// Insert a new element at the end (Tail) of the list: O(n) time
void insertAtTail(Node** headRef, int value) {
    Node* newNode = createNode(value);
    if (*headRef == NULL) {
        *headRef = newNode;
        return;
    }
    Node* temp = *headRef;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = newNode;
    printf("Inserted %d at tail.\n", value);
}

// Traverse and print the list: O(n) time
void displayList(Node* head) {
    printf("List: [Head] -> ");
    Node* temp = head;
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}

// Reverse the linked list in-place: O(n) time, O(1) space
void reverseList(Node** headRef) {
    Node* prev = NULL;
    Node* curr = *headRef;
    Node* next = NULL;
    
    while (curr != NULL) {
        next = curr->next;  // Store next node
        curr->next = prev;  // Reverse current node's pointer
        prev = curr;        // Move prev forward
        curr = next;        // Move curr forward
    }
    *headRef = prev;
    printf("Linked List reversed successfully!\n");
}

// Deallocate all nodes to prevent memory leaks
void freeList(Node* head) {
    Node* temp;
    while (head != NULL) {
        temp = head;
        head = head->next;
        free(temp);
    }
    printf("Memory freed successfully.\n");
}

int main() {
    printf("========================================\n");
    printf(" SkillArc — Singly Linked List in C     \n");
    printf("========================================\n\n");

    Node* head = NULL;

    insertAtHead(&head, 30);
    insertAtHead(&head, 20);
    insertAtHead(&head, 10);
    insertAtTail(&head, 40);
    insertAtTail(&head, 50);

    printf("\nInitial ");
    displayList(head);

    printf("\nReversing list...\n");
    reverseList(&head);

    printf("Reversed ");
    displayList(head);

    printf("\nCleaning up heap memory...\n");
    freeList(head);

    return 0;
}

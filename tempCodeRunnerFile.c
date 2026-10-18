
#include <stdio.h>
#include <stdlib.h>

struct node {
    int info;
    struct node *next;
};

/* Create a node and insert at the end */
struct node *create(struct node *head) {
    struct node *temp, *ptr;
    int data;

    temp = (struct node *)malloc(sizeof(struct node));

    if (temp == NULL) {
        printf("Memory allocation failed!\n");
        return head;
    }

    printf("Enter data: ");
    scanf("%d", &data);

    temp->info = data;
    temp->next = NULL;

    if (head == NULL) {
        head = temp;
    } else {
        ptr = head;
        while (ptr->next != NULL) {
            ptr = ptr->next;
        }
        ptr->next = temp;
    }

    return head;
}

/* Display the linked list */
void display(struct node *head) {
    struct node *ptr = head;

    if (head == NULL) {
        printf("List is empty!\n");
        return;
    }

    printf("Linked List: ");
    while (ptr != NULL) {
        printf("%d -> ", ptr->info);
        ptr = ptr->next;
    }
    printf("NULL\n");
}

/* Insert at the beginning */
struct node *insertstart(struct node *head) {
    struct node *temp;
    int data;

    temp = (struct node *)malloc(sizeof(struct node));

    if (temp == NULL) {
        printf("Memory allocation failed!\n");
        return head;
    }

    printf("Enter data: ");
    scanf("%d", &data);

    temp->info = data;
    temp->next = head;
    head = temp;

    printf("Node inserted at beginning.\n");
    return head;
}

/* Insert at the end */
struct node *insertend(struct node *head) {
    struct node *temp, *ptr;
    int data;

    temp = (struct node *)malloc(sizeof(struct node));

    if (temp == NULL) {
        printf("Memory allocation failed!\n");
        return head;
    }

    printf("Enter data: ");
    scanf("%d", &data);

    temp->info = data;
    temp->next = NULL;

    if (head == NULL) {
        head = temp;
    } else {
        ptr = head;
        while (ptr->next != NULL) {
            ptr = ptr->next;
        }
        ptr->next = temp;
    }

    printf("Node inserted at end.\n");
    return head;
}

/* Insert at a given position (positions start at 1) */
struct node *insertatpos(struct node *head) {
    struct node *temp, *ptr;
    int data, pos, i;

    printf("Enter position: ");
    scanf("%d", &pos);

    if (pos < 1) {
        printf("Invalid position!\n");
        return head;
    }

    if (pos == 1) {
        return insertstart(head);
    }

    ptr = head;
    for (i = 1; i < pos - 1 && ptr != NULL; i++) {
        ptr = ptr->next;
    }

    if (ptr == NULL) {
        printf("Invalid position!\n");
        return head;
    }

    temp = (struct node *)malloc(sizeof(struct node));

    if (temp == NULL) {
        printf("Memory allocation failed!\n");
        return head;
    }

    printf("Enter data: ");
    scanf("%d", &data);

    temp->info = data;
    temp->next = ptr->next;
    ptr->next = temp;

    printf("Node inserted at position %d.\n", pos);
    return head;
}

/* Delete from the beginning */
struct node *deletestart(struct node *head) {
    struct node *ptr;

    if (head == NULL) {
        printf("List is empty!\n");
        return head;
    }

    ptr = head;
    head = head->next;
    free(ptr);

    printf("Node deleted from beginning.\n");
    return head;
}

/* Delete from the end */
struct node *deleteend(struct node *head) {
    struct node *ptr, *preptr;

    if (head == NULL) {
        printf("List is empty!\n");
        return head;
    }

    if (head->next == NULL) {
        free(head);
        printf("Node deleted from end.\n");
        return NULL;
    }

    ptr = head;

    while (ptr->next != NULL) {
        preptr = ptr;
        ptr = ptr->next;
    }

    preptr->next = NULL;
    free(ptr);

    printf("Node deleted from end.\n");
    return head;
}

/* Delete from a given position */
struct node *deleteatpos(struct node *head) {
    struct node *ptr, *preptr;
    int pos, i;

    if (head == NULL) {
        printf("List is empty!\n");
        return head;
    }

    printf("Enter position: ");
    scanf("%d", &pos);

    if (pos < 1) {
        printf("Invalid position!\n");
        return head;
    }

    if (pos == 1) {
        return deletestart(head);
    }

    ptr = head;

    for (i = 1; i < pos && ptr != NULL; i++) {
        preptr = ptr;
        ptr = ptr->next;
    }

    if (ptr == NULL) {
        printf("Invalid position!\n");
        return head;
    }

    preptr->next = ptr->next;
    free(ptr);

    printf("Node deleted from position %d.\n", pos);
    return head;
}

/* Main function */
int main() {
    struct node *head = NULL;
    int choice;

    do {
        printf("\n--- SINGLY LINKED LIST MENU ---\n");
        printf("1. Create node\n");
        printf("2. Insert at beginning\n");
        printf("3. Insert at end\n");
        printf("4. Insert at position\n");
        printf("5. Delete from beginning\n");
        printf("6. Delete from end\n");
        printf("7. Delete from position\n");
        printf("8. Display\n");
        printf("9. Exit\n");

        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                head = create(head);
                break;

            case 2:
                head = insertstart(head);
                break;

            case 3:
                head = insertend(head);
                break;

            case 4:
                head = insertatpos(head);
                break;

            case 5:
                head = deletestart(head);
                break;

            case 6:
                head = deleteend(head);
                break;

            case 7:
                head = deleteatpos(head);
                break;

            case 8:
                display(head);
                break;

            case 9:
                printf("Program exited.\n");
                break;

            default:
                printf("Invalid choice! Try again.\n");
        }

    } while (choice != 9);

    return 0;
}

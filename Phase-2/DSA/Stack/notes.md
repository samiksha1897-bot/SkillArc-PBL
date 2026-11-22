# Stack in C — Quick Notes & Code Implementation

## Quick Revision Notes
1. The variable `top` tracks the index of the uppermost element.
2. Initialize `top = -1` to represent an empty stack.
3. Before pushing, always check `if (top == MAX - 1)` to prevent **Stack Overflow**.
4. Before popping, always check `if (top == -1)` to prevent **Stack Underflow**.

---

## C Implementation: Array-based Stack

```c
#include <stdio.h>
#include <stdbool.h>

#define MAX 5

// Stack Structure definition
typedef struct {
    int items[MAX];
    int top;
} Stack;

// Initialize stack
void initStack(Stack *s) {
    s->top = -1;
}

// Check if stack is empty
bool isEmpty(Stack *s) {
    return s->top == -1;
}

// Check if stack is full
bool isFull(Stack *s) {
    return s->top == MAX - 1;
}

// Push an item onto stack
bool push(Stack *s, int val) {
    if (isFull(s)) {
        printf("Error: Stack Overflow! Cannot push %d\n", val);
        return false;
    }
    s->items[++(s->top)] = val;
    printf("Pushed: %d\n", val);
    return true;
}

// Pop an item from stack
int pop(Stack *s) {
    if (isEmpty(s)) {
        printf("Error: Stack Underflow! Stack is empty\n");
        return -1;
    }
    int popped = s->items[(s->top)--];
    printf("Popped: %d\n", popped);
    return popped;
}

// Peek top item
int peek(Stack *s) {
    if (isEmpty(s)) {
        printf("Stack is empty!\n");
        return -1;
    }
    return s->items[s->top];
}

// Display all elements from top to bottom
void display(Stack *s) {
    if (isEmpty(s)) {
        printf("Stack is currently empty.\n");
        return;
    }
    printf("Current Stack (top to bottom):\n");
    for (int i = s->top; i >= 0; i--) {
        printf(" | %4d |\n", s->items[i]);
    }
    printf(" +------+\n");
}

int main() {
    Stack myStack;
    initStack(&myStack);

    push(&myStack, 10);
    push(&myStack, 20);
    push(&myStack, 30);
    display(&myStack);

    printf("Top element is: %d\n", peek(&myStack));

    pop(&myStack);
    display(&myStack);

    return 0;
}
```
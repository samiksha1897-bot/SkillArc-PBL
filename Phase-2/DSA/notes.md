# Queue in C — Quick Notes & Circular Queue Implementation

## Quick Revision Notes
1. Linear queue condition for full: `rear == MAX - 1`.
2. Circular queue condition for full: `(rear + 1) % MAX == front`.
3. Circular queue condition for empty: `front == -1`.
4. When deleting the last remaining element, reset both `front = -1` and `rear = -1`.

---

## C Implementation: Circular Queue

```c
#include <stdio.h>
#include <stdbool.h>

#define SIZE 5

typedef struct {
    int items[SIZE];
    int front;
    int rear;
} CircularQueue;

// Initialize circular queue
void initQueue(CircularQueue *q) {
    q->front = -1;
    q->rear = -1;
}

// Check if queue is full
bool isFull(CircularQueue *q) {
    return (q->front == 0 && q->rear == SIZE - 1) || 
           (q->front == (q->rear + 1) % SIZE);
}

// Check if queue is empty
bool isEmpty(CircularQueue *q) {
    return q->front == -1;
}

// Enqueue element
bool enqueue(CircularQueue *q, int val) {
    if (isFull(q)) {
        printf("Error: Queue is full! Cannot enqueue %d\n", val);
        return false;
    }
    if (isEmpty(q)) {
        q->front = 0;
        q->rear = 0;
    } else {
        q->rear = (q->rear + 1) % SIZE;
    }
    q->items[q->rear] = val;
    printf("Enqueued: %d (rear at index %d)\n", val, q->rear);
    return true;
}

// Dequeue element
int dequeue(CircularQueue *q) {
    if (isEmpty(q)) {
        printf("Error: Queue is empty!\n");
        return -1;
    }
    int removed = q->items[q->front];
    if (q->front == q->rear) {
        // Last element dequeued, reset queue
        q->front = -1;
        q->rear = -1;
    } else {
        q->front = (q->front + 1) % SIZE;
    }
    printf("Dequeued: %d\n", removed);
    return removed;
}

// Display elements
void display(CircularQueue *q) {
    if (isEmpty(q)) {
        printf("Queue is empty.\n");
        return;
    }
    printf("Queue contents (Front to Rear): ");
    int i = q->front;
    while (true) {
        printf("%d ", q->items[i]);
        if (i == q->rear) break;
        i = (i + 1) % SIZE;
    }
    printf("\n");
}

int main() {
    CircularQueue q;
    initQueue(&q);

    enqueue(&q, 10);
    enqueue(&q, 20);
    enqueue(&q, 30);
    enqueue(&q, 40);
    display(&q);

    dequeue(&q);
    dequeue(&q);
    display(&q);

    enqueue(&q, 50);
    enqueue(&q, 60);
    display(&q);

    return 0;
}
```
/**
 * SkillArc Phase III — Data Structures in C
 * Module: Graph Representation and Traversals (BFS & DFS)
 * Author: Team Apex (Samiksha Gurung, Vaibhavi Thapliyal, Tanisha Rai)
 * Features:
 *  - Adjacency Matrix representation
 *  - Breadth-First Search (BFS) using circular FIFO queue
 *  - Depth-First Search (DFS) using recursion
 *  - Undirected edge insertion
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_VERTICES 10

// Graph structure using Adjacency Matrix
typedef struct {
    int numVertices;
    int adjMatrix[MAX_VERTICES][MAX_VERTICES];
} Graph;

// Initialize graph
void initGraph(Graph* g, int vertices) {
    g->numVertices = vertices;
    for (int i = 0; i < vertices; i++) {
        for (int j = 0; j < vertices; j++) {
            g->adjMatrix[i][j] = 0;
        }
    }
}

// Add undirected edge between u and v
void addEdge(Graph* g, int u, int v) {
    if (u >= 0 && u < g->numVertices && v >= 0 && v < g->numVertices) {
        g->adjMatrix[u][v] = 1;
        g->adjMatrix[v][u] = 1;
    }
}

// Simple Circular Queue for BFS
typedef struct {
    int items[MAX_VERTICES];
    int front;
    int rear;
} Queue;

void initQueue(Queue* q) { q->front = -1; q->rear = -1; }
bool isQueueEmpty(Queue* q) { return q->front == -1; }
void enqueue(Queue* q, int value) {
    if (q->front == -1) q->front = 0;
    q->rear = (q->rear + 1) % MAX_VERTICES;
    q->items[q->rear] = value;
}
int dequeue(Queue* q) {
    int item = q->items[q->front];
    if (q->front == q->rear) {
        q->front = -1;
        q->rear = -1;
    } else {
        q->front = (q->front + 1) % MAX_VERTICES;
    }
    return item;
}

// Breadth-First Search (BFS) from startVertex: O(V^2) for matrix
void BFS(Graph* g, int startVertex) {
    bool visited[MAX_VERTICES] = {false};
    Queue q;
    initQueue(&q);

    visited[startVertex] = true;
    enqueue(&q, startVertex);

    printf("BFS Traversal starting from vertex %d: ", startVertex);

    while (!isQueueEmpty(&q)) {
        int curr = dequeue(&q);
        printf("%d ", curr);

        for (int neighbor = 0; neighbor < g->numVertices; neighbor++) {
            if (g->adjMatrix[curr][neighbor] == 1 && !visited[neighbor]) {
                visited[neighbor] = true;
                enqueue(&q, neighbor);
            }
        }
    }
    printf("\n");
}

// Recursive Helper for DFS
void DFSRecursive(Graph* g, int curr, bool visited[]) {
    visited[curr] = true;
    printf("%d ", curr);

    for (int neighbor = 0; neighbor < g->numVertices; neighbor++) {
        if (g->adjMatrix[curr][neighbor] == 1 && !visited[neighbor]) {
            DFSRecursive(g, neighbor, visited);
        }
    }
}

// Depth-First Search (DFS) from startVertex: O(V^2) for matrix
void DFS(Graph* g, int startVertex) {
    bool visited[MAX_VERTICES] = {false};
    printf("DFS Traversal starting from vertex %d: ", startVertex);
    DFSRecursive(g, startVertex, visited);
    printf("\n");
}

int main() {
    printf("========================================\n");
    printf(" SkillArc — Graph Traversals in C       \n");
    printf("========================================\n\n");

    Graph g;
    initGraph(&g, 6);

    // Creating sample connected graph:
    // 0 - 1, 0 - 2, 1 - 3, 1 - 4, 2 - 4, 3 - 5, 4 - 5
    addEdge(&g, 0, 1);
    addEdge(&g, 0, 2);
    addEdge(&g, 1, 3);
    addEdge(&g, 1, 4);
    addEdge(&g, 2, 4);
    addEdge(&g, 3, 5);
    addEdge(&g, 4, 5);

    printf("Graph successfully constructed with 6 vertices (0 to 5) and 7 edges.\n\n");

    BFS(&g, 0);
    DFS(&g, 0);

    return 0;
}

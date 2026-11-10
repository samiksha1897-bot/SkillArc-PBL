/**
 * SkillArc Phase III — Data Structures in C
 * Module: Binary Search Tree (BST) Implementation
 * Author: Team Apex (Samiksha Gurung, Vaibhavi Thapliyal, Tanisha Rai)
 * Features:
 *  - Dynamic BST node creation
 *  - Recursive BST insertion preserving invariant
 *  - Recursive searching: O(log n) average time
 *  - Inorder traversal (outputs sorted keys)
 *  - Leaf node counter function
 */

#include <stdio.h>
#include <stdlib.h>

// Definition of a Binary Search Tree Node
typedef struct BSTNode {
    int data;
    struct BSTNode* left;
    struct BSTNode* right;
} BSTNode;

// Function to create a new tree node
BSTNode* createTreeNode(int value) {
    BSTNode* newNode = (BSTNode*)malloc(sizeof(BSTNode));
    if (!newNode) {
        printf("Memory allocation error.\n");
        exit(1);
    }
    newNode->data = value;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// Insert into BST recursively: O(log n) avg, O(n) worst
BSTNode* insertBST(BSTNode* root, int value) {
    if (root == NULL) {
        return createTreeNode(value);
    }
    if (value < root->data) {
        root->left = insertBST(root->left, value);
    } else if (value > root->data) {
        root->right = insertBST(root->right, value);
    }
    return root;
}

// Search for a key in BST: O(log n) avg
BSTNode* searchBST(BSTNode* root, int target) {
    if (root == NULL || root->data == target) {
        return root;
    }
    if (target < root->data) {
        return searchBST(root->left, target);
    }
    return searchBST(root->right, target);
}

// Inorder traversal (Left, Root, Right) -> Yields ascending sorted order
void inorderTraversal(BSTNode* root) {
    if (root != NULL) {
        inorderTraversal(root->left);
        printf("%d ", root->data);
        inorderTraversal(root->right);
    }
}

// Preorder traversal (Root, Left, Right)
void preorderTraversal(BSTNode* root) {
    if (root != NULL) {
        printf("%d ", root->data);
        preorderTraversal(root->left);
        preorderTraversal(root->right);
    }
}

// Count total leaf nodes (nodes with 0 children)
int countLeafNodes(BSTNode* root) {
    if (root == NULL) return 0;
    if (root->left == NULL && root->right == NULL) return 1;
    return countLeafNodes(root->left) + countLeafNodes(root->right);
}

// Postorder deallocation of tree nodes
void freeTree(BSTNode* root) {
    if (root != NULL) {
        freeTree(root->left);
        freeTree(root->right);
        free(root);
    }
}

int main() {
    printf("========================================\n");
    printf(" SkillArc — Binary Search Tree (BST) in C\n");
    printf("========================================\n\n");

    BSTNode* root = NULL;
    int keys[] = {50, 30, 70, 20, 40, 60, 80};
    int n = sizeof(keys) / sizeof(keys[0]);

    printf("Inserting keys: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", keys[i]);
        root = insertBST(root, keys[i]);
    }
    printf("\n\n");

    printf("Inorder Traversal (Sorted): ");
    inorderTraversal(root);
    printf("\n");

    printf("Preorder Traversal: ");
    preorderTraversal(root);
    printf("\n\n");

    printf("Total Leaf Nodes: %d\n", countLeafNodes(root));

    // Test Search
    int query = 40;
    BSTNode* found = searchBST(root, query);
    if (found) {
        printf("Search Key %d: FOUND in BST!\n", query);
    } else {
        printf("Search Key %d: NOT found.\n", query);
    }

    freeTree(root);
    printf("Tree memory deallocated successfully.\n");

    return 0;
}

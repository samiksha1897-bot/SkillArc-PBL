/**
 * SkillArc Phase III — Data Structures in C
 * Module: Hash Table with Linear Probing Collision Resolution
 * Author: Team Apex (Samiksha Gurung, Vaibhavi Thapliyal, Tanisha Rai)
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define TABLE_SIZE 10
#define EMPTY -1
#define DELETED -2

typedef struct {
    int key;
    int value;
} HashEntry;

typedef struct {
    HashEntry table[TABLE_SIZE];
    int size;
} HashTable;

void initHashTable(HashTable* ht) {
    ht->size = 0;
    for (int i = 0; i < TABLE_SIZE; i++) {
        ht->table[i].key = EMPTY;
        ht->table[i].value = 0;
    }
}

int hashFunction(int key) {
    return (key % TABLE_SIZE + TABLE_SIZE) % TABLE_SIZE;
}

// Insert key-value pair using linear probing: O(1) avg
bool insert(HashTable* ht, int key, int value) {
    if (ht->size == TABLE_SIZE) {
        printf("Hash table overflow!\n");
        return false;
    }
    int index = hashFunction(key);
    while (ht->table[index].key != EMPTY && ht->table[index].key != DELETED && ht->table[index].key != key) {
        index = (index + 1) % TABLE_SIZE; // Linear probe
    }
    ht->table[index].key = key;
    ht->table[index].value = value;
    ht->size++;
    return true;
}

// Search key in hash table: O(1) avg
int search(HashTable* ht, int key) {
    int index = hashFunction(key);
    int start = index;
    while (ht->table[index].key != EMPTY) {
        if (ht->table[index].key == key) {
            return ht->table[index].value;
        }
        index = (index + 1) % TABLE_SIZE;
        if (index == start) break;
    }
    return -1; // Not found
}

void printTable(HashTable* ht) {
    printf("Slot | Key    | Value\n");
    printf("---------------------\n");
    for (int i = 0; i < TABLE_SIZE; i++) {
        if (ht->table[i].key == EMPTY) printf("[%2d] | EMPTY  | -\n", i);
        else if (ht->table[i].key == DELETED) printf("[%2d] | DELETED| -\n", i);
        else printf("[%2d] | %-6d | %d\n", i, ht->table[i].key, ht->table[i].value);
    }
}

int main() {
    printf("========================================\n");
    printf(" SkillArc — Hash Table (Linear Probing) \n");
    printf("========================================\n\n");

    HashTable ht;
    initHashTable(&ht);

    insert(&ht, 15, 100);
    insert(&ht, 25, 200); // Collides with 15 (both 15%10 and 25%10 are 5) -> probes to 6
    insert(&ht, 35, 300); // Collides with 15 & 25 -> probes to 7
    insert(&ht, 12, 400);

    printTable(&ht);

    printf("\nSearching for key 25: Value = %d\n", search(&ht, 25));
    printf("Searching for key 99: Value = %d (not found)\n", search(&ht, 99));

    return 0;
}

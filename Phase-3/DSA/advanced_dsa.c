/**
 * SkillArc Phase III — Data Structures in C
 * Module: Dynamic Memory Allocation and Infix-to-Postfix Stack Conversion
 * Author: Team Apex (Samiksha Gurung, Vaibhavi Thapliyal, Tanisha Rai)
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Stack for operator conversion
typedef struct {
    char* items;
    int top;
    int capacity;
} CharStack;

CharStack* createStack(int cap) {
    CharStack* s = (CharStack*)malloc(sizeof(CharStack));
    s->capacity = cap;
    s->top = -1;
    s->items = (char*)malloc(cap * sizeof(char));
    return s;
}

void push(CharStack* s, char c) { s->items[++s->top] = c; }
char pop(CharStack* s) { return s->items[s->top--]; }
char peek(CharStack* s) { return s->items[s->top]; }
int isEmpty(CharStack* s) { return s->top == -1; }

int precedence(char op) {
    if (op == '+' || op == '-') return 1;
    if (op == '*' || op == '/') return 2;
    if (op == '^') return 3;
    return 0;
}

// Convert Infix to Postfix expression
void infixToPostfix(const char* infix, char* postfix) {
    int len = strlen(infix);
    CharStack* s = createStack(len + 1);
    int k = 0;

    for (int i = 0; i < len; i++) {
        char ch = infix[i];
        if (isalnum(ch)) {
            postfix[k++] = ch;
        } else if (ch == '(') {
            push(s, ch);
        } else if (ch == ')') {
            while (!isEmpty(s) && peek(s) != '(') {
                postfix[k++] = pop(s);
            }
            if (!isEmpty(s)) pop(s); // Remove '('
        } else {
            // Operator
            while (!isEmpty(s) && precedence(peek(s)) >= precedence(ch)) {
                postfix[k++] = pop(s);
            }
            push(s, ch);
        }
    }
    while (!isEmpty(s)) {
        postfix[k++] = pop(s);
    }
    postfix[k] = '\0';
    free(s->items);
    free(s);
}

int main() {
    printf("========================================\n");
    printf(" SkillArc — Infix to Postfix Conversion \n");
    printf("========================================\n\n");

    const char* infix = "A+(B*C-(D/E^F)*G)*H";
    char postfix[100];

    infixToPostfix(infix, postfix);

    printf("Infix Expression   : %s\n", infix);
    printf("Postfix Expression : %s\n", postfix);

    return 0;
}

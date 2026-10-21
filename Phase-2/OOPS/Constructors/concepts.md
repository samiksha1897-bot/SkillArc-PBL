# Constructors & Destructors in C++ — Core Concepts

## 1. What is a Constructor?
A **Constructor** is a special member function that has the same name as the class. It is automatically called when an object of the class is instantiated. It has no return type (not even `void`).

---

## 2. Types of Constructors
1. **Default Constructor:** Takes no arguments. If not defined, C++ compiler generates a default constructor automatically.
2. **Parameterized Constructor:** Takes arguments to initialize member variables with specific values.
3. **Copy Constructor:** Creates a new object as a copy of an existing object of the same class:
   ```cpp
   Student(const Student &other);
   ```

---

## 3. Destructor
A **Destructor** (`~ClassName()`) is called automatically when an object goes out of scope. It deallocates resources, closes files, or frees dynamically allocated heap memory.

---

## 4. C++ Code Example

```cpp
#include <iostream>
#include <string>
using namespace std;

class Question {
private:
    int id;
    string promptText;
    int pointValue;

public:
    // 1. Default Constructor
    Question() : id(0), promptText("Unassigned"), pointValue(0) {
        cout << "[Default Constructor Called]\n";
    }

    // 2. Parameterized Constructor
    Question(int qId, string text, int pts) : id(qId), promptText(text), pointValue(pts) {
        cout << "[Parameterized Constructor Called for Q" << id << "]\n";
    }

    // 3. Copy Constructor
    Question(const Question &other) {
        id = other.id;
        promptText = other.promptText + " (Copy)";
        pointValue = other.pointValue;
        cout << "[Copy Constructor Called]\n";
    }

    // Destructor
    ~Question() {
        // Clean up actions
    }

    void show() const {
        cout << "Q" << id << ": " << promptText << " [" << pointValue << " pts]\n";
    }
};

int main() {
    Question q1(101, "What is the time complexity of pushing onto a stack?", 10);
    Question q2 = q1; // Calls Copy Constructor

    q1.show();
    q2.show();

    return 0;
}
```
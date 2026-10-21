# Inheritance in C++ — Core Concepts

## 1. What is Inheritance?
**Inheritance** is a fundamental pillar of Object-Oriented Programming (OOP) where a new class (known as the **derived** or **child** class) inherits properties (data members) and behaviors (member functions) from an existing class (known as the **base** or **parent** class).

### Key Benefits:
- **Code Reusability:** Common attributes and logic are defined once in the base class and inherited across multiple child classes without rewriting code.
- **Extensibility:** Child classes can add specialized attributes and methods without modifying the base class.
- **Real-World Modeling:** Allows natural representation of "is-a" relationships (e.g., a `Student` *is a* `User`).

---

## 2. Modes of Inheritance & Access Specifiers
When a class is derived, the access mode (`public`, `protected`, or `private`) controls how base class members are inherited:

| Base Class Member Access | Inherited via `public` | Inherited via `protected` | Inherited via `private` |
| :--- | :--- | :--- | :--- |
| **`public`** | `public` | `protected` | `private` |
| **`protected`** | `protected` | `protected` | `private` |
| **`private`** | *Not Inherited* (Hidden) | *Not Inherited* (Hidden) | *Not Inherited* (Hidden) |

> **Important Rule:** `private` members of the base class are never directly accessible by derived classes. To allow derived classes access while keeping members hidden from the outside world, use the **`protected:`** specifier.

---

## 3. Types of Inheritance in C++

1. **Single Inheritance:** A derived class inherits from exactly one base class.
   ```
   [ Base Class A ] ───▶ [ Derived Class B ]
   ```
2. **Multiple Inheritance:** A single derived class inherits from two or more base classes.
   ```
   [ Base A ]   [ Base B ]
        \           /
         ▼         ▼
     [ Derived C ]
   ```
3. **Multilevel Inheritance:** A class inherits from a derived class, forming a chain.
   ```
   [ Base A ] ───▶ [ Intermediate B ] ───▶ [ Derived C ]
   ```
4. **Hierarchical Inheritance:** Multiple derived classes inherit from a single base class.
   ```
           [ Base Class A ]
             /          \
            ▼            ▼
     [ Derived B ]   [ Derived C ]
   ```
5. **Hybrid (Virtual) Inheritance:** A combination of two or more types (e.g., Diamond Problem), resolved using `virtual` base classes.

---

## 4. Complete C++ Code Example

```cpp
#include <iostream>
#include <string>
using namespace std;

// Base Class (Parent)
class User {
protected:
    string username;
    string email;

public:
    // Parameterized Constructor
    User(string u, string e) : username(u), email(e) {
        cout << "[User Base Class Constructor Called]\n";
    }

    // Base class member function
    void displayBasicInfo() const {
        cout << "Username : " << username << "\n";
        cout << "Email    : " << email << "\n";
    }
};

// Derived Class (Child inherits from User via Single Public Inheritance)
class StudentLearner : public User {
private:
    int streakDays;
    int creditPoints;

public:
    // Constructor initializes base class constructor via Member Initializer List
    StudentLearner(string u, string e, int streak, int points)
        : User(u, e), streakDays(streak), creditPoints(points) {
        cout << "[StudentLearner Derived Class Constructor Called]\n";
    }

    // Extended functionality in derived class
    void displayDashboard() const {
        cout << "\n--- Student Learner Profile ---\n";
        displayBasicInfo(); // Reusing inherited method from User class
        cout << "Streak   : " << streakDays << " Days 🔥\n";
        cout << "Credits  : " << creditPoints << " pts 💎\n";
        cout << "-------------------------------\n";
    }

    // Member function to update credits
    void earnBonusCredits(int bonus) {
        creditPoints += bonus;
        cout << ">> " << username << " earned +" << bonus << " bonus credits!\n";
    }
};

int main() {
    // Instantiating derived class object
    StudentLearner student("vaibhavi_t", "vaibhavithapliyal23@gmail.com", 5, 160);

    // Calling derived class methods
    student.displayDashboard();
    student.earnBonusCredits(25);
    student.displayDashboard();

    return 0;
}
```

---

## 5. Constructor Execution Order
1. When an object of a derived class is created:
   - The **Base Class Constructor** is called **first**.
   - The **Derived Class Constructor** is called **second**.
2. When the object is destroyed (goes out of scope):
   - The **Derived Class Destructor** is called **first**.
   - The **Base Class Destructor** is called **second** (reverse order).

---
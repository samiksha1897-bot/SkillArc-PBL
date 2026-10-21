# Classes and Objects in C++ — Core Concepts

## 1. What is a Class and an Object?
In Object-Oriented Programming (OOP):
- A **Class** is a user-defined blueprint or prototype from which objects are created. It encapsulates member data (attributes) and member functions (behaviors).
- An **Object** is an instance of a class. When a class is defined, no memory is allocated until an object of that class is instantiated.

---

## 2. Access Specifiers
C++ provides three primary access specifiers:
1. **`public`:** Members are accessible from anywhere outside the class.
2. **`private` (Default):** Members are accessible only from within member functions of the class (or friend functions).
3. **`protected`:** Members are accessible within the class and by derived (child) classes.

---

## 3. C++ Code Example

```cpp
#include <iostream>
#include <string>
using namespace std;

// Class Definition
class Student {
private:
    string studentId;
    string name;
    int creditPoints;

public:
    // Member function to initialize state
    void setData(string id, string n, int credits) {
        studentId = id;
        name = n;
        creditPoints = credits;
    }

    // Member function to display details
    void displayProfile() const {
        cout << "--------------------------------\n";
        cout << "Student ID : " << studentId << "\n";
        cout << "Name       : " << name << "\n";
        cout << "Credits    : " << creditPoints << " pts\n";
        cout << "--------------------------------\n";
    }

    // Getter for credits
    int getCredits() const {
        return creditPoints;
    }
};

int main() {
    // Instantiating objects of class Student
    Student s1;
    s1.setData("2510370150", "Samiksha Gurung", 120);

    Student s2;
    s2.setData("2510370080", "Tanisha Rai", 140);

    s1.displayProfile();
    s2.displayProfile();

    return 0;
}
```

---

## 4. Key Takeaways
- Encapsulation hides internal data members behind private access and exposes public interface methods.
- Good practice: keep member variables `private` and provide `public` getter and setter methods.
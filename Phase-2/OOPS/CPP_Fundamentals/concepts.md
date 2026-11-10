# C++ Fundamentals & Functions — Core Concepts

## 1. Evolution from C to C++
C++ was developed by Bjarne Stroustrup at Bell Labs as "C with Classes". It incorporates both procedural systems programming and the object-oriented paradigm.

---

## 2. Namespaces & Standard I/O
The `std` namespace prevents name collisions in large programs.
```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Standard output with cout" << endl;
    return 0;
}
```

---

## 3. Function Overloading & Default Arguments
- **Function Overloading:** Multiple functions can share the exact same name as long as their parameter lists (signatures) differ by count or type.
- **Default Arguments:** Default parameter values are specified in the function declaration.
- **Inline Functions:** The `inline` keyword suggests the compiler replace function calls with the actual function body to eliminate call overhead for small routines.

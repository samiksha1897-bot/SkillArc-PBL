# Polymorphism in C++ — Core Concepts

## 1. What is Polymorphism?
**Polymorphism** means "having many forms" (*poly* = many, *morph* = forms). It allows an entity such as a function, operator, or object to behave differently in different contexts.

---

## 2. Compile-Time vs Run-Time Polymorphism
### 1. Compile-Time (Static / Early Binding):
- **Function Overloading:** Functions with the same name but different signatures (number/types of parameters).
- **Operator Overloading:** Customizing standard operators (`+`, `<<`, `==`) for user-defined classes.

### 2. Run-Time (Dynamic / Late Binding):
- **Function Overriding:** A derived class provides a specific implementation of a function already defined in its base class.
- Achieved using the **`virtual`** keyword in the base class and base class pointers/references.

---

## 3. C++ Code Example: Virtual Functions

```cpp
#include <iostream>
#include <vector>
#include <memory>
using namespace std;

// Abstract Base Class
class LearningResource {
public:
    virtual void openResource() const = 0; // Pure Virtual Function
    virtual ~LearningResource() {}
};

// Derived Class 1
class VideoResource : public LearningResource {
private:
    string videoUrl;
public:
    VideoResource(string url) : videoUrl(url) {}
    void openResource() const override {
        cout << "[Streaming Video] Launching video player: " << videoUrl << "\n";
    }
};

// Derived Class 2
class QuizResource : public LearningResource {
private:
    int questionCount;
public:
    QuizResource(int count) : questionCount(count) {}
    void openResource() const override {
        cout << "[Interactive Quiz] Starting quiz session with " << questionCount << " questions.\n";
    }
};

int main() {
    // Polymorphic collection
    vector<LearningResource*> curriculum;
    curriculum.push_back(new VideoResource("https://youtube.com/watch?v=1uR4tL-UugM"));
    curriculum.push_back(new QuizResource(5));

    cout << "Loading Student Curriculum:\n";
    for (auto resource : curriculum) {
        resource->openResource(); // Polymorphic call resolved at runtime!
    }

    // Clean up
    for (auto resource : curriculum) delete resource;

    return 0;
}
```
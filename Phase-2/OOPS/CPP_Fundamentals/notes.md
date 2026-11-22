/**
 * SkillArc Phase III — OOP in C++
 * Module: C++ Fundamentals, Namespaces, Overloading & Inline Functions
 * Author: Team Apex (Samiksha Gurung, Vaibhavi Thapliyal, Tanisha Rai)
 */

#include <iostream>
#include <string>

using namespace std;

// Inline function definition
inline int square(int x) {
    return x * x;
}

// Function Overloading: Same name 'calculateArea', different parameter signatures
double calculateArea(double radius) {
    return 3.14159 * radius * radius;
}

double calculateArea(double length, double width) {
    return length * width;
}

// Default Arguments: 'discount' defaults to 0.05 (5%)
double computeTotal(double price, int qty, double discount = 0.05) {
    double subtotal = price * qty;
    return subtotal * (1.0 - discount);
}

int main() {
    cout << "========================================" << endl;
    cout << " SkillArc — C++ Fundamentals Showcase   " << endl;
    cout << "========================================" << endl << endl;

    cout << "Inline Square of 9: " << square(9) << endl;

    cout << "Area of Circle (r=5.0)    : " << calculateArea(5.0) << endl;
    cout << "Area of Rectangle (4x6)   : " << calculateArea(4.0, 6.0) << endl;

    cout << "Order Total (default 5% disc): $" << computeTotal(100.0, 2) << endl;
    cout << "Order Total (custom 15% disc): $" << computeTotal(100.0, 2, 0.15) << endl;

    return 0;
}

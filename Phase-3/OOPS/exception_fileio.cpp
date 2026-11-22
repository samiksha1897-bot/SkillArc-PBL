/**
 * SkillArc Phase III — OOP in C++
 * Module: Exception Handling and File Streams (ifstream, ofstream)
 * Author: Team Apex (Samiksha Gurung, Vaibhavi Thapliyal, Tanisha Rai)
 */

#include <iostream>
#include <fstream>
#include <string>
#include <stdexcept>

using namespace std;

// Function demonstrating Exception Handling
double safeDivide(double numerator, double denominator) {
    if (denominator == 0.0) {
        throw runtime_error("Math Error: Division by zero is undefined!");
    }
    return numerator / denominator;
}

// Function demonstrating File Writing and Reading
void demonstrateFileIO() {
    string filename = "skillarc_log.txt";

    // 1. Writing to a file using ofstream
    ofstream outFile(filename);
    if (!outFile) {
        cerr << "Error opening file for write!" << endl;
        return;
    }
    outFile << "SKILLARC SYSTEM AUDIT LOG" << endl;
    outFile << "Student: Samiksha Gurung (2510370150) | Topic: Linked Lists | Score: 100%" << endl;
    outFile << "Student: Vaibhavi Thapliyal (2510370530) | Topic: Trees | Score: 100%" << endl;
    outFile << "Student: Tanisha Rai (2510370080) | Topic: STL | Score: 100%" << endl;
    outFile.close();
    cout << "[OK] File '" << filename << "' written successfully." << endl;

    // 2. Reading back using ifstream
    ifstream inFile(filename);
    if (!inFile) {
        cerr << "Error opening file for read!" << endl;
        return;
    }
    cout << "\n--- Reading Contents of " << filename << " ---" << endl;
    string line;
    while (getline(inFile, line)) {
        cout << "  " << line << endl;
    }
    inFile.close();
}

int main() {
    cout << "========================================" << endl;
    cout << " SkillArc — Exception & File I/O Engine " << endl;
    cout << "========================================" << endl << endl;

    // Exception handling demo
    try {
        cout << "10 / 2 = " << safeDivide(10, 2) << endl;
        cout << "Attempting 10 / 0..." << endl;
        cout << safeDivide(10, 0) << endl;
    } catch (const exception& e) {
        cout << "[CAUGHT EXCEPTION] " << e.what() << endl;
    }

    cout << endl;
    demonstrateFileIO();

    return 0;
}

/**
 * SkillArc Phase III — OOP in C++
 * Module: Templates and STL (vector, map, priority_queue, algorithms)
 * Author: Team Apex (Samiksha Gurung, Vaibhavi Thapliyal, Tanisha Rai)
 */

#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>

using namespace std;

// 1. Generic Function Template
template <typename T>
T findMax(T a, T b) {
    return (a > b) ? a : b;
}

int main() {
    cout << "========================================" << endl;
    cout << " SkillArc — Templates & STL Engine      " << endl;
    cout << "========================================" << endl << endl;

    // Test Function Template
    cout << "findMax(15, 29)          : " << findMax(15, 29) << endl;
    cout << "findMax(3.1415, 2.7182)   : " << findMax(3.1415, 2.7182) << endl;
    cout << "findMax(string("Alpha"), string("Omega")): " << findMax(string("Alpha"), string("Omega")) << endl << endl;

    // STL Vector & Algorithm (std::sort)
    vector<int> scores = {95, 40, 85, 100, 60, 75};
    cout << "Original Scores : ";
    for (int s : scores) cout << s << " ";
    cout << endl;

    sort(scores.begin(), scores.end());
    cout << "Sorted Scores   : ";
    for (int s : scores) cout << s << " ";
    cout << endl << endl;

    // STL Map: Key-Value association
    map<string, int> studentCredits;
    studentCredits["Samiksha Gurung"] = 140;
    studentCredits["Vaibhavi Thapliyal"] = 160;
    studentCredits["Tanisha Rai"] = 165;

    cout << "Student Credits Directory (STL Map):" << endl;
    for (const auto& pair : studentCredits) {
        cout << "  • " << pair.first << " : " << pair.second << " pts" << endl;
    }

    return 0;
}

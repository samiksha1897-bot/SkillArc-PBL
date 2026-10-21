/**
 * ============================================================================
 * Project: SkillArc — Phase-II Prototype
 * Module : C++ OOP Quiz Engine
 * Author : Tanisha Rai (Team Apex — Student ID: 2510370080)
 * Description: Demonstrates Object-Oriented Programming (Encapsulation,
 *              Constructors, Member Methods) using Question and Student classes.
 * ============================================================================
 */

#include <iostream>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;

// ============================================================================
// Class: Question
// Represents an individual multiple-choice question in the SkillArc platform.
// ============================================================================
class Question {
private:
    int id;
    string topic;
    string prompt;
    vector<string> options;
    int correctIndex; // 0-based index (0, 1, 2, 3)
    int points;
    string explanation;

public:
    // Default Constructor
    Question() : id(0), topic("General"), prompt(""), correctIndex(0), points(10), explanation("") {}

    // Parameterized Constructor
    Question(int qId, string qTopic, string qPrompt, vector<string> qOptions, int qCorrect, int qPts, string qExp)
        : id(qId), topic(qTopic), prompt(qPrompt), options(qOptions), correctIndex(qCorrect), points(qPts), explanation(qExp) {}

    // Display the question and numbered options
    void display(int questionNumber) const {
        cout << "\n================================================================\n";
        cout << " Question " << questionNumber << " [" << topic << "] (" << points << " Credit Points)\n";
        cout << "================================================================\n";
        cout << prompt << "\n\n";
        for (size_t i = 0; i < options.size(); i++) {
            cout << "  [" << (i + 1) << "] " << options[i] << "\n";
        }
        cout << "----------------------------------------------------------------\n";
    }

    // Validate the student's chosen answer (1-based input converted to 0-based)
    bool validateAnswer(int chosenOption) const {
        return (chosenOption - 1) == correctIndex;
    }

    // Getters
    int getPoints() const { return points; }
    string getExplanation() const { return explanation; }
    string getCorrectAnswerText() const {
        if (correctIndex >= 0 && correctIndex < (int)options.size()) {
            return options[correctIndex];
        }
        return "Unknown";
    }
    int getCorrectOptionNumber() const { return correctIndex + 1; }
};

// ============================================================================
// Class: Student
// Encapsulates learner profile, earned credit points, and quiz statistics.
// ============================================================================
class Student {
private:
    string studentId;
    string fullName;
    string department;
    int creditPoints;
    int currentStreak;
    int totalQuizzesAttempted;

public:
    // Parameterized Constructor
    Student(string id, string name, string dept, int initialCredits = 100, int streak = 3)
        : studentId(id), fullName(name), department(dept), creditPoints(initialCredits),
          currentStreak(streak), totalQuizzesAttempted(0) {}

    // Award Credit Points for successful answers or milestones
    void addCredits(int points) {
        if (points > 0) {
            creditPoints += points;
            cout << "  >> [REWARD] +" << points << " Credit Points awarded to " << fullName << "!\n";
        }
    }

    // Increment completed quiz count
    void recordQuizAttempt() {
        totalQuizzesAttempted++;
    }

    // Display formatted student profile dashboard
    void displayDashboard() const {
        cout << "\n============================================================\n";
        cout << "               SKILLARC — STUDENT PROFILE                   \n";
        cout << "============================================================\n";
        cout << " Student ID        : " << studentId << "\n";
        cout << " Name              : " << fullName << "\n";
        cout << " Department        : " << department << "\n";
        cout << " Total Credits     : " << creditPoints << " pts\n";
        cout << " Current Streak    : " << currentStreak << " Days 🔥\n";
        cout << " Quizzes Completed : " << totalQuizzesAttempted << "\n";
        cout << "============================================================\n";
    }

    // Getters
    int getCredits() const { return creditPoints; }
    string getName() const { return fullName; }
};

// ============================================================================
// Main Application / Driver Function
// ============================================================================
int main() {
    cout << "============================================================\n";
    cout << "      SKILLARC — INTERACTIVE C++ OOP QUIZ MODULE            \n";
    cout << "      Developed by: Tanisha Rai (Team Apex)                 \n";
    cout << "============================================================\n";

    // Initialize Demonstration Student
    Student student("2510370080", "Tanisha Rai", "B.Tech CSE (Year 2)", 120, 4);
    student.displayDashboard();

    // Prepare Sample Questions (Arrays, Stack, Queue)
    vector<Question> quizQuestions;

    quizQuestions.push_back(Question(
        1, "Arrays",
        "What is the time complexity of accessing an element in an array using its index?",
        {"O(1)", "O(n)", "O(log n)", "O(n^2)"},
        0, 10,
        "Arrays allow random access via memory address offset calculation: Address = Base + i * Size."
    ));

    quizQuestions.push_back(Question(
        2, "Stack",
        "Which principle does the Stack data structure strictly follow?",
        {"FIFO (First In First Out)", "LIFO (Last In First Out)", "LILO (Last In Last Out)", "Random Access"},
        1, 10,
        "Stack follows Last-In First-Out: the last item pushed is the first item popped."
    ));

    quizQuestions.push_back(Question(
        3, "Queue",
        "In a Circular Queue of size N, what condition indicates that the queue is full?",
        {"front == rear", "(rear + 1) % N == front", "rear == N", "front == 0"},
        1, 10,
        "A circular queue wraps around using modulo; full condition is (rear + 1) % N == front."
    ));

    int score = 0;
    int pointsEarned = 0;

    cout << "\nStarting Quiz: DSA Fundamentals (3 Questions)...\n";

    // Simulation of quiz evaluation
    // Can accept real user input or demonstration answers
    for (size_t i = 0; i < quizQuestions.size(); i++) {
        quizQuestions[i].display(i + 1);
        
        int userChoice = 0;
        cout << "Enter your answer (1-4): ";
        
        // Safety check if running non-interactively
        if (!(cin >> userChoice)) {
            // Default demo answer
            userChoice = quizQuestions[i].getCorrectOptionNumber();
            cout << userChoice << " (Demo Auto-Selection)\n";
        }

        if (quizQuestions[i].validateAnswer(userChoice)) {
            cout << "  [CORRECT!] Well done!\n";
            cout << "  Explanation: " << quizQuestions[i].getExplanation() << "\n";
            score++;
            pointsEarned += quizQuestions[i].getPoints();
            student.addCredits(quizQuestions[i].getPoints());
        } else {
            cout << "  [INCORRECT] Correct answer was: Option [" 
                 << quizQuestions[i].getCorrectOptionNumber() << "] " 
                 << quizQuestions[i].getCorrectAnswerText() << "\n";
            cout << "  Explanation: " << quizQuestions[i].getExplanation() << "\n";
        }
    }

    student.recordQuizAttempt();

    // Final Results Summary
    cout << "\n============================================================\n";
    cout << "                    QUIZ SCORECARD                          \n";
    cout << "============================================================\n";
    cout << " Questions Attempted : " << quizQuestions.size() << "\n";
    cout << " Correct Answers     : " << score << "\n";
    cout << " Accuracy            : " << fixed << setprecision(1) 
         << ((double)score / quizQuestions.size() * 100.0) << "%\n";
    cout << " Credits Gained      : +" << pointsEarned << " pts\n";
    cout << " Updated Total Points: " << student.getCredits() << " pts\n";
    cout << "============================================================\n\n";

    return 0;
}
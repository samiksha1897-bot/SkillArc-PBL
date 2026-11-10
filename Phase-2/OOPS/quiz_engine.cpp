/**
 * ============================================================================
 * Project: SkillArc — Phase-II Prototype with Admin Extension
 * Module : C++ OOP Quiz Engine & Admin Audit System
 * Author : Tanisha Rai (Team Apex — Student ID: 2510370080)
 * Description: Demonstrates Object-Oriented Programming:
 *              - Classes & Encapsulation (Question, Student, Admin)
 *              - Constructors & Member Initializer Lists
 *              - Friend Class Concept (Admin accesses private Student data)
 *              - Cohort Progress Auditing & Reporting
 * ============================================================================
 */

#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
#include <fstream>
#include <map>
#include <stack>

using namespace std;

// Forward declaration of Admin class to declare it as a friend inside Student
class Admin;

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
    string getTopic() const { return topic; }
};

// ============================================================================
// Class: Student
// Encapsulates learner profile, earned credit points, and quiz statistics.
// Demonstrates Encapsulation by keeping sensitive progress and credit data private.
// Grants privileged audit access to class Admin via friend declaration.
// ============================================================================
class Student {
private:
    string studentId;
    string fullName;
    string department;
    int creditPoints;
    int currentStreak;
    int totalQuizzesAttempted;
    int totalQuestionsAttempted;
    int totalCorrectAnswers;
    vector<string> completedTopics;

    // ========================================================================
    // FRIEND CLASS DECLARATION
    // ========================================================================
    // By declaring 'friend class Admin;', the Student class permits the Admin
    // class to directly access private members (studentId, creditPoints, 
    // totalCorrectAnswers, completedTopics, etc.) for administrative reporting
    // and academic audits without compromising encapsulation to ordinary functions.
    friend class Admin;

public:
    // Parameterized Constructor
    Student(string id, string name, string dept, int initialCredits = 100, int streak = 3,
            int questionsAttempted = 0, int correctAnswers = 0, vector<string> topics = {})
        : studentId(id), fullName(name), department(dept), creditPoints(initialCredits),
          currentStreak(streak), totalQuizzesAttempted(0),
          totalQuestionsAttempted(questionsAttempted), totalCorrectAnswers(correctAnswers),
          completedTopics(topics) {}

    // Award Credit Points for successful answers or milestones
    void addCredits(int points) {
        if (points > 0) {
            creditPoints += points;
            cout << "  >> [REWARD] +" << points << " Credit Points awarded to " << fullName << "!\n";
        }
    }

    // Record quiz question attempt result
    void recordQuestionResult(bool isCorrect) {
        totalQuestionsAttempted++;
        if (isCorrect) {
            totalCorrectAnswers++;
        }
    }

    // Increment completed quiz count
    void recordQuizAttempt() {
        totalQuizzesAttempted++;
    }

    // Mark a learning topic completed
    void addCompletedTopic(const string& topicName) {
        for (const auto& t : completedTopics) {
            if (t == topicName) return;
        }
        completedTopics.push_back(topicName);
    }

    // Display formatted student profile dashboard (User-facing method)
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
        cout << " Questions Done    : " << totalQuestionsAttempted << " (" 
             << totalCorrectAnswers << " Correct)\n";
        cout << " Completed Topics  : " << completedTopics.size() << "\n";
        cout << "============================================================\n";
    }

    // Public Getters for ordinary non-privileged access
    int getCredits() const { return creditPoints; }
    string getName() const { return fullName; }
    string getId() const { return studentId; }
};

// ============================================================================
// Class: Admin
// Demonstrates the Friend Class concept in C++ Object-Oriented Programming.
// Because Admin is declared as a friend of Student, Admin member functions
// can directly access private student attributes (such as creditPoints,
// totalQuestionsAttempted, totalCorrectAnswers, and completedTopics) to generate
// administrative performance analytics and cohort-wide audit reports.
// ============================================================================
class Admin {
private:
    string adminId;
    string adminName;
    string department;

public:
    // Parameterized Constructor
    Admin(string id = "ADMIN01", string name = "Prof. Rajesh Sharma", 
          string dept = "Faculty of Computer Science & Engineering")
        : adminId(id), adminName(name), department(dept) {}

    // Function 1: Display an Individual Student Progress Report
    // Directly accesses private members of the Student object through friendship!
    void displayStudentReport(const Student& s) const {
        cout << "\n============================================================\n";
        cout << "        ADMINISTRATIVE AUDIT: INDIVIDUAL STUDENT REPORT     \n";
        cout << "        Inspector: " << adminName << " (" << adminId << ")\n";
        cout << "============================================================\n";
        // Accessing private members: s.studentId, s.fullName, s.department, s.creditPoints, etc.
        cout << " Student Roll ID     : " << s.studentId << "\n";
        cout << " Student Name        : " << s.fullName << "\n";
        cout << " Department          : " << s.department << "\n";
        cout << " Credit Wallet       : " << s.creditPoints << " pts\n";
        cout << " Learning Streak     : " << s.currentStreak << " Days 🔥\n";
        cout << " Quizzes Attempted   : " << s.totalQuizzesAttempted << "\n";
        cout << " Questions Attempted : " << s.totalQuestionsAttempted << "\n";
        cout << " Correct Answers     : " << s.totalCorrectAnswers << "\n";
        int incorrect = s.totalQuestionsAttempted - s.totalCorrectAnswers;
        cout << " Incorrect Answers   : " << (incorrect > 0 ? incorrect : 0) << "\n";

        double acc = (s.totalQuestionsAttempted > 0)
                     ? ((double)s.totalCorrectAnswers / s.totalQuestionsAttempted * 100.0)
                     : 0.0;
        cout << " Individual Accuracy : " << fixed << setprecision(1) << acc << "%\n";

        cout << " Completed Topics (" << s.completedTopics.size() << ") : ";
        if (s.completedTopics.empty()) {
            cout << "No topics completed yet.\n";
        } else {
            for (size_t i = 0; i < s.completedTopics.size(); i++) {
                cout << s.completedTopics[i] << (i + 1 < s.completedTopics.size() ? ", " : "\n");
            }
        }
        cout << "============================================================\n";
    }

    // Function 2: Display Cohort Overview for ALL Students
    // Operates across a collection (vector<Student>) to calculate macro statistics
    void displayAllStudentsOverview(const vector<Student>& cohort) const {
        cout << "\n================================================================================\n";
        cout << "              SKILLARC ADMIN DASHBOARD — COHORT OVERVIEW REPORT                \n";
        cout << "              Authorized Administrator: " << adminName << "                   \n";
        cout << "================================================================================\n";
        cout << left << setw(14) << "Roll ID"
             << setw(20) << "Student Name"
             << setw(10) << "Credits"
             << setw(9)  << "Streak"
             << setw(12) << "Questions"
             << setw(10) << "Correct"
             << setw(11) << "Accuracy"
             << setw(10) << "Topics"
             << "\n";
        cout << "--------------------------------------------------------------------------------\n";

        int totalQuestions = 0;
        int totalCorrect = 0;
        int totalCredits = 0;
        int totalTopicsCompleted = 0;

        for (const auto& s : cohort) {
            // Accessing private members of Student via friend privileges:
            double acc = (s.totalQuestionsAttempted > 0)
                         ? ((double)s.totalCorrectAnswers / s.totalQuestionsAttempted * 100.0)
                         : 0.0;
            cout << left << setw(14) << s.studentId
                 << setw(20) << s.fullName
                 << setw(10) << s.creditPoints
                 << setw(9)  << (to_string(s.currentStreak) + "d")
                 << setw(12) << s.totalQuestionsAttempted
                 << setw(10) << s.totalCorrectAnswers
                 << fixed << setprecision(1) << setw(11) << (to_string(acc).substr(0, 4) + "%")
                 << setw(10) << s.completedTopics.size()
                 << "\n";

            totalQuestions += s.totalQuestionsAttempted;
            totalCorrect += s.totalCorrectAnswers;
            totalCredits += s.creditPoints;
            totalTopicsCompleted += s.completedTopics.size();
        }

        cout << "--------------------------------------------------------------------------------\n";
        cout << " Cohort Summary Statistics:\n";
        cout << "  • Total Registered Students   : " << cohort.size() << "\n";
        cout << "  • Total Questions Attempted   : " << totalQuestions << "\n";
        cout << "  • Total Correct Answers       : " << totalCorrect << "\n";
        cout << "  • Total Incorrect Answers     : " << (totalQuestions - totalCorrect) << "\n";
        double cohortAcc = (totalQuestions > 0) ? ((double)totalCorrect / totalQuestions * 100.0) : 0.0;
        cout << "  • Overall Cohort Accuracy     : " << fixed << setprecision(1) << cohortAcc << "%\n";
        cout << "  • Total Topic Milestones Done : " << totalTopicsCompleted << "\n";
        cout << "  • Total Credits in Circulation: " << totalCredits << " pts\n";
        cout << "================================================================================\n";
    }

    // Function 3: Identify Top Performer and Students Recommended for Practice
    // Function 4: Export Cohort Audit Report using C++ File Streams (ofstream)
    void exportAuditReport(const vector<Student>& cohort, const string& filepath) const {
        ofstream outFile(filepath);
        if (!outFile.is_open()) {
            cerr << "Error opening file for audit export!\n";
            return;
        }
        outFile << "================================================================================\n";
        outFile << "           SKILLARC C++ OOP ADMIN AUDIT REPORT (FILE STREAM I/O)                \n";
        outFile << "           Inspector: " << adminName << " (" << adminId << ")\n";
        outFile << "================================================================================\n";
        for (const auto& s : cohort) {
            double acc = (s.totalQuestionsAttempted > 0)
                         ? ((double)s.totalCorrectAnswers / s.totalQuestionsAttempted * 100.0) : 0.0;
            outFile << "Roll ID: " << s.studentId << " | " << s.fullName 
                    << " | Credits: " << s.creditPoints << " pts | Accuracy: " << fixed << setprecision(1) << acc << "%\n";
        }
        outFile << "================================================================================\n";
        outFile.close();
        cout << ">> [C++ File I/O] Successfully exported cohort audit to: " << filepath << "\n";
    }

    void generateLearningInsights(const vector<Student>& cohort) const {
        if (cohort.empty()) return;

        const Student* topStudent = &cohort[0];
        double topAcc = -1.0;
        vector<string> practiceCandidates;

        for (const auto& s : cohort) {
            double acc = (s.totalQuestionsAttempted > 0)
                         ? ((double)s.totalCorrectAnswers / s.totalQuestionsAttempted * 100.0)
                         : 0.0;
            if (acc > topAcc && s.totalQuestionsAttempted > 0) {
                topAcc = acc;
                topStudent = &s;
            }
            if (s.totalQuestionsAttempted > 0 && acc < 75.0) {
                practiceCandidates.push_back(s.fullName + " (" + to_string(acc).substr(0, 4) + "%)");
            }
        }

        cout << "\n============================================================\n";
        cout << "          ACADEMIC PERFORMANCE INSIGHTS (ADMIN)             \n";
        cout << "============================================================\n";
        cout << " 🌟 Highest Quiz Accuracy   : " << topStudent->fullName 
             << " (" << fixed << setprecision(1) << topAcc << "% accuracy, " 
             << topStudent->creditPoints << " pts)\n";

        cout << " 💡 Recommended for Practice: ";
        if (practiceCandidates.empty()) {
            cout << "All active students currently maintain >= 75% accuracy.\n";
        } else {
            for (size_t i = 0; i < practiceCandidates.size(); i++) {
                cout << practiceCandidates[i] << (i + 1 < practiceCandidates.size() ? ", " : "\n");
            }
        }
        cout << "============================================================\n\n";
    }
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

        bool isCorrect = quizQuestions[i].validateAnswer(userChoice);
        student.recordQuestionResult(isCorrect);

        if (isCorrect) {
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
    student.addCompletedTopic("DSA Fundamentals Quiz");

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

    // ========================================================================
    // DEMONSTRATION OF C++ ADMIN CLASS & FRIEND CLASS ACCESS
    // ========================================================================
    cout << "\n************************************************************\n";
    cout << "   LAUNCHING C++ OOP ADMIN AUDIT CONSOLE (FRIEND CLASS DEMO) \n";
    cout << "************************************************************\n";

    // Create Admin instance
    Admin facultyAdmin("ADMIN01", "Prof. Rajesh Sharma", "Faculty of CSE & IT");

    // Construct cohort of students using actual SkillArc student models
    vector<Student> cohort;
    cohort.push_back(student); // Tanisha with freshly completed quiz
    cohort.push_back(Student("2510370150", "Samiksha Gurung", "B.Tech CSE (Year 2)", 140, 4, 4, 4, {"Arrays", "Stack"}));
    cohort.push_back(Student("2510370530", "Vaibhavi Thapliyal", "B.Tech CSE (Year 2)", 160, 5, 8, 7, {"Arrays", "Stack"}));
    cohort.push_back(Student("2510370156", "Vanshika Parmar", "B.Tech IT (Year 2)", 50, 1, 0, 0, {}));
    cohort.push_back(Student("2510370594", "Naina Vashistha", "B.Tech CSE (Year 2)", 50, 1, 0, 0, {}));

    // Admin examines ALL students via friend class privileges
    facultyAdmin.displayAllStudentsOverview(cohort);

    // Admin audits a specific individual student
    facultyAdmin.displayStudentReport(cohort[1]); // Samiksha Gurung

    // Admin generates academic insights
    facultyAdmin.generateLearningInsights(cohort);
    facultyAdmin.exportAuditReport(cohort, "skillarc_audit_report.txt");

    return 0;
}

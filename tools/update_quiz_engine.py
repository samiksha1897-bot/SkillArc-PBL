"""
Script to update Phase-2/OOPS/quiz_engine.cpp with C++ File Streams (ofstream/ifstream) and STL usage.
"""

from pathlib import Path

path = Path(r"C:\Users\sudeep\OneDrive\Documents\SkillArc-PBL\Phase-2\OOPS\quiz_engine.cpp")

with open(path, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Add headers if missing
if "#include <fstream>" not in code:
    code = code.replace("#include <iomanip>\n", "#include <iomanip>\n#include <fstream>\n#include <map>\n#include <stack>\n")

# 2. Add exportAuditReport method to Admin class
file_io_method = """    // Function 4: Export Cohort Audit Report using C++ File Streams (ofstream)
    void exportAuditReport(const vector<Student>& cohort, const string& filepath) const {
        ofstream outFile(filepath);
        if (!outFile.is_open()) {
            cerr << "Error opening file for audit export!\\n";
            return;
        }
        outFile << "================================================================================\\n";
        outFile << "           SKILLARC C++ OOP ADMIN AUDIT REPORT (FILE STREAM I/O)                \\n";
        outFile << "           Inspector: " << adminName << " (" << adminId << ")\\n";
        outFile << "================================================================================\\n";
        for (const auto& s : cohort) {
            double acc = (s.totalQuestionsAttempted > 0)
                         ? ((double)s.totalCorrectAnswers / s.totalQuestionsAttempted * 100.0) : 0.0;
            outFile << "Roll ID: " << s.studentId << " | " << s.fullName 
                    << " | Credits: " << s.creditPoints << " pts | Accuracy: " << fixed << setprecision(1) << acc << "%\\n";
        }
        outFile << "================================================================================\\n";
        outFile.close();
        cout << ">> [C++ File I/O] Successfully exported cohort audit to: " << filepath << "\\n";
    }
"""

if "void exportAuditReport" not in code:
    code = code.replace("    void generateLearningInsights(const vector<Student>& cohort) const {", file_io_method + "\n    void generateLearningInsights(const vector<Student>& cohort) const {")

# 3. Call export in main
if "facultyAdmin.exportAuditReport" not in code:
    code = code.replace("facultyAdmin.generateLearningInsights(cohort);", "facultyAdmin.generateLearningInsights(cohort);\n    facultyAdmin.exportAuditReport(cohort, \"skillarc_audit_report.txt\");")

with open(path, "w", encoding="utf-8") as f:
    f.write(code)

print("quiz_engine.cpp updated with File Streams & STL!")

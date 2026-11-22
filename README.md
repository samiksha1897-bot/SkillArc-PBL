# SkillArc — Phase III Gamified Learning Platform
**Repository:** [https://github.com/samiksha1897-bot/SkillArc-PBL](https://github.com/samiksha1897-bot/SkillArc-PBL)  
**Evaluation Phase:** Phase III Project-Based Learning (PBL)  
**Team Apex (B.Tech CSE — 2nd Year):**
- **Samiksha Gurung** (Lead — DSA Modules in C)
- **Vaibhavi Thapliyal** (Lead — Interface, Dashboard & Min-Heap Engine)
- **Tanisha Rai** (Lead — C++ OOP Module, Friend Class & File Streams)

---

## About SkillArc
**SkillArc** is an interactive, gamified learning platform tailored for undergraduate computer science students mastering **Data Structures & Algorithms in C** and **Object-Oriented Programming in C++**.

In **Phase III**, SkillArc goes beyond teaching DSA and OOP: **it actively implements these computer science concepts within the platform's own application architecture.**

---

## ⚡ Real DSA Concepts Implemented in SkillArc

1. **Min-Heap (Priority Queue):**
   - Drives the **Live Student Leaderboard** using Python's `heapq`.
   - Stores negative credit values (`-credits`) so the highest-scoring learner floats to the root.
   - Deterministic tie-breaking uses negative streaks (`-streak`) and student roll IDs.
   - **Time Complexity:** $O(N)$ build via `heapify()`, $O(N \log N)$ sorted rank extraction.

2. **Prefix Tree (Trie):**
   - Powers the **Concept & Topic Search Engine**.
   - Enables instant prefix autocomplete across all 17 topics, subtopics, and programming terms in $O(L)$ time.

3. **Inverted Index (Hash Map):**
   - Maps technical keywords (e.g., `vtable`, `malloc`, `recursion`, `bfs`, `destructor`) directly to relevant course pages with $O(1)$ average lookup time.

4. **Course Prerequisite Graph (DAG):**
   - Models curriculum dependencies as a **Directed Acyclic Graph**.
   - Runs **Breadth-First Search (BFS)** to calculate the shortest prerequisite path between any two modules.
   - Runs **Depth-First Search (DFS)** to generate the complete topological sequence of the curriculum.

5. **LIFO Navigation Stack:**
   - Tracks in-app page history, allowing students to backtrack with the "⬅️ Previous Page" stack-pop button in $O(1)$ time.

6. **FIFO Study Task Queue:**
   - Enqueues recommended practice tasks in chronological sequence. Students complete and dequeue the top task in $O(1)$ time.

7. **Singly Linked List:**
   - Telemetry activity stream implemented with dynamic nodes supporting $O(1)$ head insertion and $O(N)$ traversal.

---

## 🛡️ OOP Concepts Implemented in SkillArc

1. **Inheritance & Abstraction (`core/oop_models.py`):**
   - Abstract Base Class `User(ABC)` derived into `StudentUser` and `AdminUser`.
   - Abstract Base Class `LearningModule(ABC)` derived into `DSAModule` and `OOPModule`.
2. **Encapsulation:**
   - Sensitive student metrics (credits, streak, quiz results, password hashes) are protected by private attributes, modified strictly through validated member methods (`add_credits()`, `record_quiz_attempt()`).
3. **Polymorphism:**
   - Virtual-style method overrides for `get_role_badge()` and `has_admin_privileges()`.
4. **Friend Class in C++ (`Phase-2/OOPS/quiz_engine.cpp`):**
   - `class Student` declares `friend class Admin;`, granting authorized faculty direct supervisory access to audit private student fields without exposing them to public modification.
5. **C++ File Streams (`<fstream>`):**
   - The native C++ engine exports formal cohort reports to `skillarc_audit_report.txt` using `std::ofstream`.
6. **C++ STL:**
   - Demonstrates `std::vector`, `std::map`, and `std::stack` containers.

---

## 🔒 Cryptographic Security & Password Hashing
- Passwords are encrypted using **PBKDF2-HMAC-SHA256** with unique 128-bit random salts and 100,000 iterations.
- Legacy plain-text passwords auto-migrate seamlessly on first run with zero data loss.
- Constant-time hash verification (`hmac.compare_digest`) prevents timing attacks.

---

## 📚 17 Curriculum Modules

### Data Structures in C (10 Topics)
1. **Arrays in C** (Contiguous allocation, pointer offset arithmetic)
2. **Stack (LIFO)** (Array stack, overflow, postfix evaluation)
3. **Queue & Circular Queue** (FIFO, wrap-around modulo)
4. **Linked Lists** (Singly, Doubly, Circular, in-place reversal, cycle detection)
5. **Trees & BST** (Binary Search Tree invariant, Inorder, Preorder, Postorder)
6. **Graphs & Traversals** (Adjacency Matrix, BFS queue, DFS recursion)
7. **Searching** (Linear Search vs. Binary Search, overflow-safe mid calculation)
8. **Sorting** (Bubble, Insertion, Merge $O(n \log n)$, Quick Sort)
9. **Hashing** (Hash functions, Linear Probing, Separate Chaining, Load Factor)
10. **Advanced DSA** (DMA `malloc`/`free`, Dangling Pointers, Sparse Matrices, Infix to Postfix)

### Object-Oriented Programming in C++ (7 Topics)
1. **C++ Fundamentals** (`cin`/`cout`, namespaces, function overloading, inline functions)
2. **Classes and Objects** (Encapsulation, access specifiers, `this` pointer)
3. **Constructors & Destructors** (Parameterized, copy constructor, destructor, static members)
4. **Inheritance Types** (Single, Multiple, Multilevel, Diamond Problem & Virtual Base Classes)
5. **Polymorphism** (Function overloading, operator overloading, virtual functions, pure virtual, vtable)
6. **Exception Handling & File Streams** (`try`/`catch`/`throw`, `ifstream`, `ofstream`, file modes)
7. **Templates & STL Containers** (Function/class templates, `vector`, `map`, `set`, `stack`, `std::sort`)

---

## 🚀 How to Run the Application

### 1. Requirements
Ensure you have Python 3.10+ and a C++ compiler (`g++` via MSYS2 / MinGW):
```bash
pip install streamlit
```

### 2. Launch Streamlit Application
From the repository root directory:
```bash
python -m streamlit run app.py
```
Open your browser at **`http://localhost:8501`**.

### 3. Demo Accounts
- **Samiksha Gurung (DSA Lead):** One-Click Demo button or ID `2510370150` / `apex123`
- **Vaibhavi Thapliyal (UI Lead):** One-Click Demo button or ID `2510370530` / `apex123`
- **Tanisha Rai (OOP Lead):** One-Click Demo button or ID `2510370080` / `apex123`
- **Faculty Administrator:** One-Click Demo button `🛡️ Faculty Admin` or ID `ADMIN01` / `admin123`

### 4. Run C++ Quiz Engine Standalone
```bash
cd Phase-2/OOPS
g++ -std=c++17 -Wall quiz_engine.cpp -o quiz_engine.exe
./quiz_engine.exe
```

---

## 📑 Phase III Implementation Report
For detailed algorithmic complexity breakdowns, before-and-after comparisons, and test suite logs, refer to:  
👉 **[PHASE_3_IMPLEMENTATION_REPORT.md](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/PHASE_3_IMPLEMENTATION_REPORT.md)**

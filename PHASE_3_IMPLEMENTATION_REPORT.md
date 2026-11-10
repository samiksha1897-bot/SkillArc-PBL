# SkillArc — Phase III Implementation & Architecture Report
**Project Title:** SkillArc: A Gamified Learning Platform for DSA (C) and OOP (C++)  
**Evaluation Phase:** Phase III Project-Based Learning (PBL)  
**Team Apex (B.Tech CSE — 2nd Year):**
- **Samiksha Gurung** (Student ID: `2510370150`) — DSA Modules Lead (C)
- **Vaibhavi Thapliyal** (Student ID: `2510370530`) — UI, Gamification & Min-Heap Engine Lead
- **Tanisha Rai** (Student ID: `2510370080`) — C++ OOP Engine, Friend Class & File I/O Lead

---

## Executive Summary
In Phase III, **SkillArc** has evolved from an interactive prototype into a comprehensive, production-grade learning platform. This release dramatically expands the academic syllabus to **17 comprehensive modules** (10 in DSA using C, 7 in OOP using C++), introduces **cryptographic PBKDF2 password hashing**, and—most importantly—**implements genuine Data Structures and Object-Oriented Programming concepts within the platform's own underlying architecture**.

Rather than merely displaying static lessons, SkillArc actively uses:
1. A **Min-Heap (Priority Queue)** to compute real-time student leaderboard rankings in $O(N \log N)$ time.
2. A **Prefix Tree (Trie)** and **Inverted Index Hash Map** to deliver instantaneous global search and autocomplete across topics, subtopics, and keywords in $O(L)$ time.
3. A **Course Prerequisite Graph (Directed Acyclic Graph - DAG)** with **BFS** for finding shortest prerequisite pathways and **DFS** for computing topological curriculum sequences.
4. A **LIFO Navigation Stack** for seamless page backtracking and breadcrumb navigation.
5. A **FIFO Study Task Queue** to manage pending practice activities.
6. A **Singly Linked List** for dynamic $O(1)$ head insertion in the real-time activity stream.
7. An **OOP Class Hierarchy** (`User` $\to$ `StudentUser`, `AdminUser`) with encapsulation, inheritance, polymorphism, and composition.
8. A **Native C++ Engine** utilizing `friend class Admin;`, **C++ File Streams** (`std::ofstream`/`std::ifstream`), and **STL** (`vector`, `map`, `stack`).

---

## SECTION A: New Learning Modules

The curriculum has been expanded from the initial 5 topics to **17 complete topics**, fully aligned with the second-year B.Tech CSE syllabus. Each topic is equipped with beginner-friendly theory notes (`concepts.md`), complete compilable source code with step-by-step walkthroughs (`notes.md`), video tutorials, LeetCode / GeeksforGeeks practice problems, and interactive quizzes.

### 1. Data Structures and Algorithms in C (10 Modules)
- **`Arrays`** (Existing): Contiguous 1D/2D layouts, pointer offset formula `*(arr + i)`, spatial cache locality, bounds checking.
- **`Stack`** (Existing): LIFO discipline, array-based overflow/underflow, expression parsing, call stack mechanics.
- **`Queue`** (Existing): FIFO order, linear queue false-overflow, Circular Queue modulo wrap-around `(rear + 1) % N`.
- **`Linked_Lists`** (NEW):
  - *Subtopics:* Singly Linked Lists, Doubly Linked Lists (`prev` and `next`), Circular Linked Lists, dynamic memory allocation with `malloc()` and `free()`, node insertion (head, middle, tail), deletion, pointer manipulation, in-place $O(n)$ iterative list reversal, Floyd's Cycle Detection (Tortoise and Hare).
  - *Code Implementation:* Compilable C program [`linked_lists.c`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/Phase-3/DSA/linked_lists.c) demonstrating dynamic allocation, bidirectional traversal, and in-place reversal.
- **`Trees`** (NEW):
  - *Subtopics:* Tree terminology (root, leaf, height, depth), Binary Trees, Binary Search Tree (BST) invariant ($\text{Left} < \text{Root} < \text{Right}$), Inorder, Preorder, Postorder traversals, search, recursive insertion, deletion with Inorder Successor, leaf node counting.
  - *Code Implementation:* Compilable C program [`trees.c`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/Phase-3/DSA/trees.c) demonstrating BST insertion, searching in $O(\log n)$, and sorted Inorder traversal.
- **`Graphs`** (NEW):
  - *Subtopics:* Graph models $G=(V, E)$, directed vs. undirected, weighted vs. unweighted, cyclic vs. DAG, Adjacency Matrix ($O(V^2)$ space) vs. Adjacency List ($O(V+E)$ space), Breadth-First Search (BFS) using a FIFO queue, Depth-First Search (DFS) using recursion, topological ordering.
  - *Code Implementation:* Compilable C program [`graphs.c`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/Phase-3/DSA/graphs.c) with Adjacency Matrix, queue-based BFS, and recursive DFS.
- **`Searching`** (NEW):
  - *Subtopics:* Linear Search ($O(n)$), Binary Search ($O(\log n)$), iterative vs. recursive Divide and Conquer, precondition of sorted data, integer overflow prevention using `low + (high - low) / 2`.
  - *Code Implementation:* Compilable C program [`searching.c`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/Phase-3/DSA/searching.c) comparing Linear and Binary search approaches.
- **`Sorting`** (NEW):
  - *Subtopics:* Bubble Sort (with early-termination flag), Selection Sort, Insertion Sort (ideal for small/nearly sorted data), Merge Sort (guaranteed $O(n \log n)$ Divide and Conquer, stable), Quick Sort (pivot partitioning, average $O(n \log n)$, worst-case $O(n^2)$), stability comparison.
  - *Code Implementation:* Compilable C program [`sorting.c`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/Phase-3/DSA/sorting.c) implementing Bubble, Merge, and Quick Sort.
- **`Hashing`** (NEW):
  - *Subtopics:* Hash functions, direct addressing, Pigeonhole principle, collisions, Open Addressing (Linear Probing $(h(k)+i)\%m$, Quadratic Probing, Double Hashing), Closed Addressing (Separate Chaining with linked lists), Load Factor $\alpha = n/m$, primary clustering.
  - *Code Implementation:* Compilable C program [`hashing.c`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/Phase-3/DSA/hashing.c) implementing a hash table with Linear Probing and search.
- **`Advanced_DSA`** (NEW):
  - *Subtopics:* Pointers and pointer arithmetic, Dynamic Memory Allocation (`malloc`, `calloc`, `realloc`, `free`), memory leaks, dangling pointers, recursion and call stack activation records, Sparse Matrix 3-tuple representation `(row, col, val)`, Infix to Postfix expression conversion using Stacks.
  - *Code Implementation:* Compilable C program [`advanced_dsa.c`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/Phase-3/DSA/advanced_dsa.c) demonstrating dynamic stack allocation and infix-to-postfix parsing.

### 2. Object-Oriented Programming in C++ (7 Modules)
- **`CPP_Fundamentals`** (NEW):
  - *Subtopics:* Evolution from C to C++, streams `cin` and `cout`, `namespace std`, function overloading by parameter signature, default arguments, `inline` functions for call-overhead elimination, pass-by-reference `&`.
  - *Code Implementation:* Compilable C++ program [`cpp_fundamentals.cpp`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/Phase-3/OOPS/cpp_fundamentals.cpp).
- **`Classes_Objects`** (Existing): Class blueprints, data members, member functions, access specifiers (`public`, `private`, `protected`), encapsulation, implicit `this` pointer.
- **`Constructors`** (Existing): Default constructor, parameterized constructor, member initializer lists, copy constructor (`const ClassName&`), constructor overloading, destructor `~ClassName()`, `static` members and methods, friend functions.
- **`Inheritance`** (Existing & Expanded):
  - *Subtopics:* Single, Multiple, Multilevel, Hierarchical, and Hybrid inheritance, `public`, `protected`, and `private` inheritance modes, constructor execution order, the **Diamond Problem**, resolution via **`virtual` base classes**.
- **`Polymorphism`** (Existing & Expanded):
  - *Subtopics:* Compile-time polymorphism (function overloading, operator overloading), runtime dynamic polymorphism (function overriding, `virtual` functions, pure virtual functions `= 0`, Abstract Base Classes, virtual method table `vtable` and `vptr`).
- **`Exception_FileIO`** (NEW):
  - *Subtopics:* Runtime anomaly handling (`try`, `catch`, `throw`), `std::exception` hierarchy, file stream I/O (`<fstream>`), `ifstream` (reading), `ofstream` (writing), `fstream` (read/write), file modes (`ios::in`, `ios::out`, `ios::app`), error handling during disk I/O.
  - *Code Implementation:* Compilable C++ program [`exception_fileio.cpp`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/Phase-3/OOPS/exception_fileio.cpp).
- **`Templates_STL`** (NEW):
  - *Subtopics:* Generic programming, function templates (`template <typename T>`), class templates, Standard Template Library (STL) architecture: Sequence Containers (`vector`, `list`, `deque`), Associative Containers (`map`, `set`), Container Adaptors (`stack`, `queue`), Iterators, STL algorithms (`std::sort`, `std::binary_search`).
  - *Code Implementation:* Compilable C++ program [`templates_stl.cpp`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/Phase-3/OOPS/templates_stl.cpp).

---

## SECTION B: DSA Concepts Used Inside the SkillArc Application

SkillArc demonstrates the practical engineering utility of Data Structures and Algorithms by embedding them directly into the platform's features:

| Data Structure / Algorithm | Application Feature | File Location | Rationale & Practical Purpose | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Min-Heap (Priority Queue)** | Student Leaderboard Ranking | [`core/dsa_engine.py`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/core/dsa_engine.py#L22-L95) | Computes rankings using negative credit keys (`-credits`). The learner with the highest credit balance floats to root. Ties are broken deterministically using negative streaks and roll IDs. | $O(N)$ build via `heapify()`, $O(N \log N)$ pop extraction | $O(N)$ |
| **Prefix Tree (Trie)** | Global Search & Autocomplete | [`core/dsa_engine.py`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/core/dsa_engine.py#L98-L167) | Enables instant character-by-character autocomplete over topic names, subtopics, and concepts. Avoids scanning through large text bodies. | $O(L)$ insertion, $O(P + M)$ prefix retrieval | $O(\Sigma \cdot L \cdot N)$ |
| **Hash Map (Inverted Index)** | Keyword-to-Topic Indexing | [`core/dsa_engine.py`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/core/dsa_engine.py#L170-L190) | Maps programming keywords (e.g., `vtable`, `malloc`, `inorder`, `bfs`) directly to matching curriculum modules for instantaneous lookup. | $O(1)$ average lookup | $O(K)$ |
| **Directed Acyclic Graph (DAG)** | Course Prerequisites & Pathways | [`core/dsa_engine.py`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/core/dsa_engine.py#L193-L285) | Represents prerequisite dependencies between all 17 topics. Runs **BFS** to find shortest prerequisite sequence and **DFS** to compute topological learning order. | $O(V + E)$ for BFS & DFS | $O(V + E)$ |
| **LIFO Stack** | In-App Page Backtracking | [`core/dsa_engine.py`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/core/dsa_engine.py#L288-L318) | Pushes visited pages onto navigation stack. Clicking "⬅️ Previous Page" pops the top page in $O(1)$ time, demonstrating LIFO behavior. | $O(1)$ push / pop / peek | $O(D)$ where $D \le 20$ |
| **FIFO Queue** | Recommended Study Task Queue | [`core/dsa_engine.py`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/core/dsa_engine.py#L321-L343) | Enqueues practice tasks in chronological sequence. Students complete and dequeue the front task in $O(1)$ time. | $O(1)$ enqueue / dequeue | $O(Q)$ |
| **Singly Linked List** | Real-Time Activity Feed | [`core/dsa_engine.py`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/core/dsa_engine.py#L346-L395) | Stores student actions in dynamic nodes. Head insertion runs in $O(1)$ time, and linear traversal renders the activity stream. | $O(1)$ prepend, $O(N)$ display | $O(N)$ |
| **Binary Search** | Sorted Index & Quiz Lookup | [`app.py`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/app.py) | Applied across alphabetically sorted topic registries and question lookups. | $O(\log N)$ | $O(1)$ |

---

## SECTION C: OOP Concepts Used Inside the SkillArc Application

SkillArc demonstrates Object-Oriented Programming both in its Python interface and its C++ backend:

### 1. Python OOP Architecture ([`core/oop_models.py`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/core/oop_models.py))
- **Abstraction:** `class User(ABC)` and `class LearningModule(ABC)` define pure abstract base interfaces (`@abstractmethod`) that derived classes must implement.
- **Inheritance:** Derived classes `StudentUser(User)` and `AdminUser(User)` inherit core properties (`user_id`, `name`, `email`, `role`, `department`, `avatar`).
- **Encapsulation:** Sensitive student state (`_credits`, `_streak_days`, `_completed_topics`, `_quiz_history`, `_password_hash`) is protected by private/protected attributes. State updates occur strictly via validated member methods (`add_credits()`, `deduct_credits()`, `mark_topic_completed()`, `record_quiz_attempt()`).
- **Polymorphism:** `get_role_badge()` and `has_admin_privileges()` are overridden polymorphically in `StudentUser` (returns student badge, `False`) and `AdminUser` (returns admin badge, `True`).
- **Composition:** `StudentUser` encapsulates an `ActivityLinkedList` instance for dynamic activity telemetry and a `ProgressTracker` dict.

### 2. C++ OOP Engine ([`Phase-2/OOPS/quiz_engine.cpp`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/Phase-2/OOPS/quiz_engine.cpp))
- **`class Question`:** Encapsulates question ID, topic, prompt, options, correct index, points, and explanation. Provides `display()` and `validateAnswer()`.
- **`class Student`:** Encapsulates private student progress fields (`creditPoints`, `totalQuestionsAttempted`, `totalCorrectAnswers`, `completedTopics`).
- **`friend class Admin;`:** Declared inside `class Student`. Grants `Admin` direct access to private student metrics for cohort audits while keeping them strictly inaccessible to external code.
- **`class Admin`:** Provides supervisor audit functions: `displayStudentReport()`, `displayAllStudentsOverview()`, and `generateLearningInsights()`.
- **C++ File Streams (`<fstream>`):** Implements `exportAuditReport()` which writes `skillarc_audit_report.txt` using `std::ofstream`.
- **C++ STL:** Integrates `std::vector`, `std::map`, and `std::stack` for managing questions, student rosters, and topic analytics.

---

## SECTION D: Existing Features Improved in Phase III

1. **Authentication System:** Upgraded from plain-text storage to **salted PBKDF2-HMAC-SHA256 hashing** (100,000 iterations). Auto-migrates legacy records seamlessly without losing student data.
2. **Leaderboard:** Replaced simple sorting with a true **Min-Heap (heapq)** with negative credit keys and deterministic tie-breaking.
3. **Quiz System:** Expanded from 5 topics to **all 17 topics** (57 total questions). Added Easy, Medium, and Hard difficulty filters, optional quiz timer (5/10 mins), question jump matrix, and anti-abuse protection preventing credit farming on repeat attempts.
4. **Search System:** Introduced a dedicated global search page powered by a **Trie** and **Inverted Index Hash Map** with direct one-click navigation to topics.
5. **Admin Suite:** Full cohort oversight across all 17 topics, topic-level error rate analysis, and one-click CSV report exports.
6. **Learning Roadmaps:** Redesigned into responsive 3-column cards with visual prerequisite DAG analysis (BFS shortest path and DFS topological sort).

---

## SECTION E: Before & After Comparison (Phase II vs. Phase III)

| Feature / Dimension | Phase II Status | Phase III Implementation |
| :--- | :--- | :--- |
| **Curriculum Coverage** | 7 topics (Arrays, Stack, Queue, Classes, Constructors, Inheritance, Polymorphism) | **17 topics** (added Linked Lists, Trees, Graphs, Searching, Sorting, Hashing, Advanced DSA, C++ Fundamentals, Exception/File I/O, Templates/STL) |
| **Password Storage** | Plain-text strings (`apex123`, `admin123`) | **Cryptographic PBKDF2-HMAC-SHA256** with individual 128-bit random salts & 100,000 iterations |
| **Leaderboard Engine** | Standard Python `sorted()` list | **Genuine Min-Heap (`heapq`)** with inverted keys and deterministic tie-breaking |
| **Search Functionality** | None (manual topic selection only) | **Dedicated Search Page** powered by **Trie** autocomplete and **Inverted Index Hash Map** |
| **Course Dependencies** | Static text mention | **Directed Acyclic Graph (DAG)** with **BFS** shortest path and **DFS** topological sort |
| **Quiz Question Bank** | 18 questions across 5 topics | **57 questions across 17 topics** with Easy/Medium/Hard difficulty filters and explanations |
| **Quiz Anti-Abuse** | Partial | **Robust Retake Tracking**: repeat attempts update score and retakes count, but do not re-award credits |
| **Recent Activity Feed** | Plain Python list | **Singly Linked List** with $O(1)$ head insertion and linear traversal |
| **In-App Navigation** | Direct radio clicks | **LIFO Navigation Stack** with "⬅️ Previous Page" pop backtracking |
| **Study Task Queue** | None | **FIFO Queue** with top task preview, topic jump, and dequeue action |
| **C++ File Streams & STL** | Terminal stdout only | **`std::ofstream`** file export (`skillarc_audit_report.txt`) and **STL** containers |

---

## SECTION F: File-Wise Inventory of Changes

| File Path | Status | Purpose & Description |
| :--- | :--- | :--- |
| [`core/__init__.py`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/core/__init__.py) | **NEW** | Core package initialization exposing security, DSA engines, and OOP models. |
| [`core/security.py`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/core/security.py) | **NEW** | PBKDF2-HMAC-SHA256 password hashing, constant-time verification, and JSON migration. |
| [`core/dsa_engine.py`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/core/dsa_engine.py) | **NEW** | Min-Heap Leaderboard, Trie, Inverted Index, Course Graph DAG, Navigation Stack, Study Queue, and Singly Linked List. |
| [`core/oop_models.py`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/core/oop_models.py) | **NEW** | Abstract `User`, `StudentUser`, `AdminUser`, `LearningModule`, `DSAModule`, and `OOPModule`. |
| [`app.py`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/app.py) | **MODIFIED** | Streamlit application integrating all 17 topics, Trie search, Min-Heap, DAG analysis, and upgraded quiz system. |
| [`data/quizzes.json`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/data/quizzes.json) | **MODIFIED** | Expanded to 57 questions across 17 topics with difficulty tags, question types, and explanations. |
| [`data/student_state.json`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/data/student_state.json) | **MODIFIED** | Student and admin accounts migrated from plain-text passwords to secure PBKDF2 hashes. |
| [`Phase-2/DSA/resources.json`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/Phase-2/DSA/resources.json) | **MODIFIED** | Video links and practice problems populated for all 17 topics. |
| [`Phase-2/OOPS/quiz_engine.cpp`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/Phase-2/OOPS/quiz_engine.cpp) | **MODIFIED** | Enhanced with C++ File Streams (`ofstream` audit export) and STL containers; recompiled to `quiz_engine.exe`. |
| [`Phase-2/DSA/Linked_Lists/`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/Phase-2/DSA/Linked_Lists) | **NEW** | `concepts.md` and `notes.md` for Linked Lists. |
| [`Phase-2/DSA/Trees/`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/Phase-2/DSA/Trees) | **NEW** | `concepts.md` and `notes.md` for Binary Search Trees. |
| [`Phase-2/DSA/Graphs/`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/Phase-2/DSA/Graphs) | **NEW** | `concepts.md` and `notes.md` for Graphs, BFS, and DFS. |
| [`Phase-2/DSA/Searching/`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/Phase-2/DSA/Searching) | **NEW** | `concepts.md` and `notes.md` for Linear and Binary Search. |
| [`Phase-2/DSA/Sorting/`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/Phase-2/DSA/Sorting) | **NEW** | `concepts.md` and `notes.md` for Bubble, Merge, and Quick Sort. |
| [`Phase-2/DSA/Hashing/`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/Phase-2/DSA/Hashing) | **NEW** | `concepts.md` and `notes.md` for Hash Tables and Linear Probing. |
| [`Phase-2/DSA/Advanced_DSA/`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/Phase-2/DSA/Advanced_DSA) | **NEW** | `concepts.md` and `notes.md` for DMA, Pointers, and Infix to Postfix. |
| [`Phase-2/OOPS/CPP_Fundamentals/`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/Phase-2/OOPS/CPP_Fundamentals) | **NEW** | `concepts.md` and `notes.md` for C++ Fundamentals and Functions. |
| [`Phase-2/OOPS/Exception_FileIO/`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/Phase-2/OOPS/Exception_FileIO) | **NEW** | `concepts.md` and `notes.md` for Exception Handling and File Streams. |
| [`Phase-2/OOPS/Templates_STL/`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/Phase-2/OOPS/Templates_STL) | **NEW** | `concepts.md` and `notes.md` for Generic Templates and STL. |
| [`Phase-3/DSA/`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/Phase-3/DSA) | **NEW** | Standalone compilable C source code files (`linked_lists.c`, `trees.c`, `graphs.c`, `searching.c`, `sorting.c`, `hashing.c`, `advanced_dsa.c`). |
| [`Phase-3/OOPS/`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/Phase-3/OOPS) | **NEW** | Standalone compilable C++ source code files (`cpp_fundamentals.cpp`, `exception_fileio.cpp`, `templates_stl.cpp`). |
| [`tools/verify_phase3.py`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/tools/verify_phase3.py) | **NEW** | Automated test suite validating all 10 Phase III subsystems. |

---

## SECTION G: Testing & Verification Results

The automated verification suite ([`tools/verify_phase3.py`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/tools/verify_phase3.py)) was executed directly on the repository:

```
==================================================
      SKILLARC PHASE III VERIFICATION SUITE       
==================================================

[TEST 1] Cryptographic Password Hashing (PBKDF2-HMAC-SHA256)
  [PASS] PBKDF2 hash generation & constant-time verification passed!

[TEST 2] Auto-Migration of Stored JSON Records
  [PASS] Passwords inspected. Total migrated to PBKDF2: 6
  [PASS] All student and admin records securely hashed with individual salts!
  [PASS] Existing demo credentials (apex123, admin123) verified against PBKDF2 hashes!

[TEST 3] Min-Heap Leaderboard Ranking (heapq)
  [PASS] Min-Heap correctly extracted 9 ranked students in descending order:
     Rank #1: Aditya Verma — 280 pts (9d streak)
     Rank #2: Pooja Hegde — 230 pts (7d streak)
     Rank #3: Tanisha Rai — 165 pts (4d streak)

[TEST 4] Prefix Tree (Trie) Autocomplete Engine
  [PASS] Trie successfully completed prefix lookups for 'link', 'inord', 'virt' in O(L) time!

[TEST 5] Course Prerequisite Graph (DAG), BFS & DFS
  [PASS] BFS Shortest Prerequisite Path (Arrays -> Graphs): Arrays -> Linked_Lists -> Trees -> Graphs
  [PASS] DFS Topological Course Sequencing: Arrays -> Stack -> Queue -> Linked_Lists -> Trees -> Graphs

[TEST 6] LIFO Navigation Stack
  [PASS] Navigation Stack correctly popped to previous page in O(1) LIFO order!

[TEST 7] FIFO Study Task Queue
  [PASS] Study Task Queue correctly dequeued first-in task in O(1) FIFO order!

[TEST 8] Singly Linked List Activity Feed
  [PASS] Activity Linked List verified: Head insertion in O(1) and linear traversal in O(N)!

[TEST 9] OOP Models, Inheritance & Polymorphism
  [PASS] Base User, StudentUser, and AdminUser verified with polymorphic method overrides!

[TEST 10] Quizzes Question Bank Verification
  [PASS] Total Quiz Modules in Question Bank: 17
  [PASS] Total Questions Loaded across 17 topics: 57
  [PASS] All 17 quiz modules and questions validated with explanations!

==================================================
  * ALL 10 VERIFICATION TESTS PASSED SUCCESSFULLY! 
==================================================
```

### C++ Native Binary Verification:
The C++ Quiz Engine ([`Phase-2/OOPS/quiz_engine.cpp`](file:///C:/Users/sudeep/OneDrive/Documents/SkillArc-PBL/Phase-2/OOPS/quiz_engine.cpp)) was compiled using MSYS2 `g++ -std=c++17 -Wall quiz_engine.cpp -o quiz_engine.exe`. When run, it demonstrated:
1. Interactive Question evaluation and credit point award.
2. Direct supervisory audit of private Student members by the Admin class via `friend class Admin;`.
3. Export of `skillarc_audit_report.txt` using standard C++ File Streams (`ofstream`).

### Known Scope Limitations & Future Phase IV Work:
- **Database Engine:** The system currently uses atomic JSON flat-file storage; Phase IV will migrate to an embedded SQLite or PostgreSQL backend.
- **Compiler Sandbox:** Coding practice currently links directly to LeetCode and GeeksforGeeks; Phase IV could introduce an in-browser WebAssembly C/C++ compiler.

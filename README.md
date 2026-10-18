# SkillArc

**SkillArc** is a learning platform designed to help students learn **Data Structures and Algorithms (DSA) and C++** through structured learning roadmaps, learning resources, coding practice, quizzes, and progress tracking.

The project is being developed as part of the **Project Based Learning (PBL)** program.

---

## Problem Statement

Students often find it difficult to follow a structured path while learning Data Structures and Algorithms. Learning resources, coding practice, quizzes, and progress tracking are usually spread across different platforms.

**SkillArc** aims to bring these learning components together into a single platform where students can learn concepts in a structured manner, practice problems, test their understanding, and track their progress.

---

## Objectives

The main objectives of SkillArc are:

* Provide a structured roadmap for learning DSA and C++.
* Organize topics according to learning levels and difficulty.
* Provide curated learning resources for different topics.
* Provide coding practice opportunities.
* Include quizzes to test conceptual understanding.
* Track student learning progress.
* Encourage consistent practice through a gamified learning approach.

---

## Team Members & Roles

| Team Member            | Role                                 |
| ---------------------- | ------------------------------------ |
| **Samiksha Gurung**    | DSA / Data Structures and Algorithms |
| **Vaibhavi Thapliyal** | Interface / UI Development           |
| **Tanisha Rai**        | OOPs / C++ Development               |

---

## Technologies & Tools

### Programming Languages

* C
* C++
* Python

### Development & Project Tools

* Streamlit
* SQLite
* GitHub

### Learning & Development Resources

* roadmap.sh
* LeetCode

---

## Major Features

### 1. Structured Learning Roadmap

A topic-wise roadmap to help students follow a systematic path while learning DSA and C++.

### 2. Topic-Based Learning

Topics are organized according to different learning levels and difficulty categories:

* Easy
* Medium
* Hard

### 3. Learning Resources

Curated resources will be provided for different topics to help students understand concepts and improve their skills.

### 4. Coding Practice

Students will be guided toward coding practice problems to strengthen their problem-solving skills.

### 5. Quizzes

Topic-based quizzes will be used to test students' understanding of concepts.

### 6. Progress Tracking

The platform will track students' learning progress and completed topics.

### 7. Gamification

The platform will include features such as:

* Credit points
* Rewards
* Contests
* Leaderboard
* Monthly incentives

---

## Project Structure

```text
SkillArc-PBL/
│
├── Phase-1/
│   ├── PBL Report
│   └── PBL Presentation
│
├── Phase-2/
│   └── Development files will be added during Phase 2
│
├── Phase-3/
│   └── Development files will be added during Phase 3
│
└── README.md
```

---

## Project Development

The project is being developed in multiple phases as part of the PBL process.

### Phase 1 — Completed

* Project idea and problem statement finalized.
* Project objectives defined.
* Proposed features and modules identified.
* Development roadmap prepared.
* Phase 1 report and presentation completed.

### Phase 2 — Completed (Prototype Evaluation Build)

The working interactive prototype for Phase 2 has been completed:

* **DSA Learning Roadmap & Modules:** Arrays, Stack, and Queue with concept notes, C code implementations, and curated YouTube/LeetCode resources.
* **C++ OOP Learning Modules & Engine:** Classes & Objects, Constructors, Inheritance, and Polymorphism, backed by a native C++ OOP quiz engine (`quiz_engine.cpp`) implementing `Student` and `Question` classes.
* **Streamlit Interface & Dashboard:** Modern navy/purple student dashboard with real-time streak tracking, completion metrics, and sidebar navigation.
* **Interactive Quizzes:** Multi-question topic-wise quizzes with answer review, explanations, and anti-abuse credit point awards.
* **Gamification & Rewards:** Credit point wallet, unlocked/locked achievement badges, student leaderboard, and redeemable campus perks.
* **Notes & Peer Learning:** Interactive community study notes with local persistence.

---

## How to Run the Phase-2 Prototype

### 1. Run the Streamlit Web Application
From the repository root directory:
```bash
python -m streamlit run app.py
```
Or double-click `run_skillarc.bat` on Windows. The application will launch in your browser at `http://localhost:8501`.

### 2. Run the C++ OOP Quiz Engine (Terminal Mode)
To compile and test the standalone C++ OOP module:
```bash
g++ -std=c++17 Phase-2/OOPS/quiz_engine.cpp -o Phase-2/OOPS/quiz_engine.exe
./Phase-2/OOPS/quiz_engine.exe
```

---

### Phase 3 — Upcoming

Further development, integration, testing, and improvements will be carried out in the later phase of the project.

---

## Current Project Status

**Status: Phase-II Prototype Completed & Ready for Evaluation**

| Phase                                   | Status         |
| --------------------------------------- | -------------- |
| Phase 1 – Planning & Documentation      | Completed    |
| Phase 2 – Core Prototype Development    | Completed    |
| Phase 3 – Full Integration & Testing    | Upcoming     |

---

## Individual Contributions

The project work is divided among the three team members:

* **Samiksha Gurung (Team Lead):** DSA roadmap, concept notes, C code implementations, and practice problem curation for Arrays, Stack, and Queue.
* **Vaibhavi Thapliyal:** Streamlit dashboard interface, visual design, progress & streak tracking, gamification UI, and sidebar navigation.
* **Tanisha Rai:** C++ OOP learning modules (Classes, Constructors, Inheritance, Polymorphism) and C++ OOP quiz engine with `Student` and `Question` classes.

Individual contributions are reflected through the modular project structure and Git history.


---

## Future Scope

Future improvements to SkillArc may include:

* More DSA and C++ topics
* Additional coding challenges
* Advanced progress analytics
* More gamification features
* Improved leaderboard and reward systems
* Additional learning resources
* User-friendly interface improvements

---

## Project Documentation

Project documentation and presentation material are maintained in the respective phase folders of this repository.

* **Phase 1:** Project report and presentation
* **Phase 2:** Development work will be added as the project progresses
* **Phase 3:** Further project work will be added during the later development phase

---

## Project Repository

This repository contains the ongoing development, documentation, and progress of the **SkillArc PBL Project**.

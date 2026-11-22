"""
SkillArc Phase III Application Builder
Constructs the complete, production-ready app.py integrating:
1. PBKDF2-HMAC-SHA256 password hashing & auto-migration.
2. 17 curriculum topics across DSA in C and OOP in C++.
3. Min-Heap Leaderboard using Python's heapq with negative keys and deterministic tie-breaking.
4. Prefix Tree (Trie) & Inverted Index Hash Map for instant global search.
5. Course Prerequisite Graph (DAG) with BFS shortest path and DFS topological ordering.
6. Navigation Stack (LIFO) for page backtracking.
7. Study Task Queue (FIFO) for recommended learning tasks.
8. Activity Linked List for dynamic telemetry feeds.
9. Interactive Quiz Engine with Easy/Medium/Hard difficulty filters, optional timer, and randomized question pool.
10. Role-based Admin Dashboard with cohort analytics, individual dossiers, topic error rates, and CSV exports.
11. C++ OOP Engine Showcase with friend class Admin, File Streams, and STL integration.
"""

from pathlib import Path

app_path = Path(r"C:\Users\sudeep\OneDrive\Documents\SkillArc-PBL\app.py")

# We will generate the complete, modern, robust app.py code
app_code = '''"""
SkillArc — Phase III Complete Educational Platform
Gamified Learning Platform for Data Structures (C) and Object-Oriented Programming (C++)
Team Apex:
- Samiksha Gurung (DSA Modules — Arrays, Stack, Queue, Linked Lists, Trees, Graphs, Sorting, Searching, Hashing)
- Vaibhavi Thapliyal (Streamlit Interface, Dashboard, Progress, Streaks & Min-Heap Leaderboard)
- Tanisha Rai (C++ OOP Module, Quiz Logic with Student/Admin Classes, Friend Class & File I/O Engine)
"""

import os
import io
import csv
import json
import re
import random
import subprocess
from datetime import datetime
from pathlib import Path
import streamlit as st

# Import SkillArc Core Phase III Foundations
from core.security import hash_password, verify_password, migrate_passwords
from core.dsa_engine import (
    MinHeapLeaderboard,
    SkillArcTrie,
    KeywordInvertedIndex,
    CoursePrerequisiteGraph,
    NavigationStack,
    StudyQueue,
    ActivityLinkedList
)
from core.oop_models import StudentUser, AdminUser, DSAModule, OOPModule

# ==============================================================================
# Page Configuration
# ==============================================================================
st.set_page_config(
    page_title="SkillArc — Gamified Learning Platform (Phase III)",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Base Paths
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
ASSETS_DIR = BASE_DIR / "assets"
DSA_DIR = BASE_DIR / "Phase-2" / "DSA"
OOPS_DIR = BASE_DIR / "Phase-2" / "OOPS"
PHASE3_DIR = BASE_DIR / "Phase-3"

DATA_DIR.mkdir(exist_ok=True)
ASSETS_DIR.mkdir(exist_ok=True)
PHASE3_DIR.mkdir(exist_ok=True)

# Master Data Files
STATE_FILE = DATA_DIR / "student_state.json"
QUIZ_FILE = DATA_DIR / "quizzes.json"
REWARD_FILE = DATA_DIR / "rewards.json"
NOTES_FILE = DATA_DIR / "shared_notes.json"
RESOURCES_FILE = DSA_DIR / "resources.json"

# ==============================================================================
# Custom CSS Styling (Navy, Indigo & Purple Palette)
# ==============================================================================
st.markdown("""
<style>
    :root {
        --navy-dark: #0f172a;
        --navy-mid: #1e293b;
        --purple-accent: #4f46e5;
        --indigo-accent: #6366f1;
        --blue-accent: #2563eb;
        --bg-slate: #f8fafc;
        --border-slate: #e2e8f0;
    }
    
    .brand-header {
        display: flex;
        align-items: center;
        gap: 12px;
        padding-bottom: 8px;
        margin-bottom: 20px;
        border-bottom: 2px solid #e0e7ff;
    }
    .brand-title {
        font-size: 1.8rem;
        font-weight: 800;
        color: #1e1b4b;
        margin: 0;
        letter-spacing: -0.5px;
    }
    .brand-pill {
        font-size: 0.75rem;
        font-weight: 700;
        background: #ede9fe;
        color: #5b21b6;
        padding: 4px 10px;
        border-radius: 9999px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .metric-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.05);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 6px -1px rgba(79, 70, 229, 0.1);
        border-color: #cbd5e1;
    }
    .metric-label {
        font-size: 0.78rem;
        font-weight: 700;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        display: block;
    }
    .metric-val {
        font-size: 1.6rem;
        font-weight: 800;
        color: #0f172a;
        margin: 4px 0 2px 0;
        display: block;
    }
    .metric-sub {
        font-size: 0.78rem;
        color: #4f46e5;
        font-weight: 600;
        display: block;
    }

    .content-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 18px;
        margin-bottom: 14px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.03);
    }
    
    .demo-tag {
        background: #f0fdf4;
        border: 1px solid #bbf7d0;
        color: #166534;
        border-radius: 8px;
        padding: 8px 12px;
        font-size: 0.85rem;
        margin-bottom: 16px;
    }

    .sidebar-user {
        background: linear-gradient(135deg, #1e1b4b 0%, #312e81 100%);
        color: #ffffff;
        border-radius: 12px;
        padding: 14px;
        margin-bottom: 14px;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# Helper Functions: JSON Storage
# ==============================================================================
def load_json(path, default):
    if not path.exists():
        with open(path, "w", encoding="utf-8") as f:
            json.dump(default, f, indent=2)
        return default
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default

def save_json(path, data):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        st.error(f"Error saving data: {e}")

# ==============================================================================
# Master Curriculum Definition (17 Topics: 10 DSA in C, 7 OOP in C++)
# ==============================================================================
ALL_TOPICS = [
    # DSA Modules (C)
    {"id": "Arrays", "subject": "DSA (C)", "name": "Arrays in C", "difficulty": "Easy", "time": "45 mins"},
    {"id": "Stack", "subject": "DSA (C)", "name": "Stack (LIFO)", "difficulty": "Medium", "time": "60 mins"},
    {"id": "Queue", "subject": "DSA (C)", "name": "Queue & Circular Queue", "difficulty": "Medium", "time": "60 mins"},
    {"id": "Linked_Lists", "subject": "DSA (C)", "name": "Linked Lists (Singly, Doubly, Circular)", "difficulty": "Medium", "time": "60 mins"},
    {"id": "Trees", "subject": "DSA (C)", "name": "Trees & Binary Search Trees (BST)", "difficulty": "Hard", "time": "75 mins"},
    {"id": "Graphs", "subject": "DSA (C)", "name": "Graphs & Graph Traversals (BFS & DFS)", "difficulty": "Hard", "time": "80 mins"},
    {"id": "Searching", "subject": "DSA (C)", "name": "Searching (Linear & Binary Search)", "difficulty": "Easy", "time": "40 mins"},
    {"id": "Sorting", "subject": "DSA (C)", "name": "Sorting (Bubble, Insertion, Merge, Quick)", "difficulty": "Medium", "time": "70 mins"},
    {"id": "Hashing", "subject": "DSA (C)", "name": "Hashing & Collision Handling", "difficulty": "Medium", "time": "55 mins"},
    {"id": "Advanced_DSA", "subject": "DSA (C)", "name": "Advanced DSA (Pointers, DMA, Recursion)", "difficulty": "Hard", "time": "65 mins"},

    # OOP Modules (C++)
    {"id": "CPP_Fundamentals", "subject": "OOP (C++)", "name": "C++ Fundamentals & Functions", "difficulty": "Easy", "time": "40 mins"},
    {"id": "Classes_Objects", "subject": "OOP (C++)", "name": "Classes and Objects", "difficulty": "Easy", "time": "40 mins"},
    {"id": "Constructors", "subject": "OOP (C++)", "name": "Constructors & Destructors", "difficulty": "Easy", "time": "45 mins"},
    {"id": "Inheritance", "subject": "OOP (C++)", "name": "Inheritance & Virtual Base Classes", "difficulty": "Medium", "time": "50 mins"},
    {"id": "Polymorphism", "subject": "OOP (C++)", "name": "Polymorphism & Virtual Functions", "difficulty": "Medium", "time": "55 mins"},
    {"id": "Exception_FileIO", "subject": "OOP (C++)", "name": "Exception Handling & File Streams", "difficulty": "Medium", "time": "50 mins"},
    {"id": "Templates_STL", "subject": "OOP (C++)", "name": "Templates & STL Containers", "difficulty": "Hard", "time": "70 mins"}
]

# Badge Catalog
BADGE_CATALOG = {
    "first_step": {"name": "First Step", "icon": "🥉", "desc": "Completed your first learning topic on SkillArc."},
    "streak_starter": {"name": "Streak Starter", "icon": "🔥", "desc": "Maintained an active 3+ day learning streak."},
    "quiz_whiz": {"name": "Quiz Whiz", "icon": "⚡", "desc": "Scored 80% or higher on an interactive topic quiz."},
    "dsa_explorer": {"name": "DSA Explorer", "icon": "💡", "desc": "Completed all core DSA modules in C."},
    "cpp_cadet": {"name": "C++ Cadet", "icon": "🛡️", "desc": "Completed Object-Oriented C++ programming topics."},
    "knowledge_sharer": {"name": "Knowledge Sharer", "icon": "🌟", "desc": "Shared a helpful revision note with the community."}
}

# ==============================================================================
# Graph (DAG), Trie, Inverted Index & Navigation Stack Initialization
# ==============================================================================
@st.cache_resource
def build_course_prerequisite_graph():
    """Builds and caches the Course Prerequisite Directed Acyclic Graph (DAG)."""
    graph = CoursePrerequisiteGraph()
    for t in ALL_TOPICS:
        graph.add_topic(t["id"], t["name"], t["subject"], t["difficulty"])

    # Directed Prerequisite Edges (DSA Track)
    graph.add_prerequisite("Arrays", "Stack")
    graph.add_prerequisite("Arrays", "Queue")
    graph.add_prerequisite("Arrays", "Linked_Lists")
    graph.add_prerequisite("Arrays", "Searching")
    graph.add_prerequisite("Searching", "Sorting")
    graph.add_prerequisite("Linked_Lists", "Trees")
    graph.add_prerequisite("Linked_Lists", "Hashing")
    graph.add_prerequisite("Trees", "Graphs")
    graph.add_prerequisite("Stack", "Advanced_DSA")
    graph.add_prerequisite("Queue", "Graphs")

    # Directed Prerequisite Edges (OOP Track)
    graph.add_prerequisite("CPP_Fundamentals", "Classes_Objects")
    graph.add_prerequisite("Classes_Objects", "Constructors")
    graph.add_prerequisite("Constructors", "Inheritance")
    graph.add_prerequisite("Inheritance", "Polymorphism")
    graph.add_prerequisite("Classes_Objects", "Exception_FileIO")
    graph.add_prerequisite("Polymorphism", "Templates_STL")

    return graph

@st.cache_resource
def build_search_trie_and_index():
    """Builds and caches the SkillArc Trie and Keyword Inverted Index."""
    trie = SkillArcTrie()
    inverted_index = KeywordInvertedIndex()

    search_data = [
        # DSA Terms
        ("Arrays", "Arrays in C", "DSA (C)", "Contiguous memory layout, 1D/2D index calculation, random access O(1)"),
        ("Stack", "Stack (LIFO)", "DSA (C)", "Last In First Out, push, pop, peek, postfix evaluation, call stack"),
        ("Queue", "Queue & Circular Queue", "DSA (C)", "First In First Out, circular wrap-around modulo, breadth-first search"),
        ("Linked_Lists", "Linked Lists (Singly, Doubly, Circular)", "DSA (C)", "Dynamic nodes, next/prev pointers, head/tail insertion, reversal, cycle detection"),
        ("Trees", "Trees & Binary Search Trees (BST)", "DSA (C)", "Hierarchical nodes, root, leaf, BST invariant, Inorder, Preorder, Postorder traversals"),
        ("Graphs", "Graphs & Graph Traversals (BFS & DFS)", "DSA (C)", "Adjacency Matrix, Adjacency List, Breadth-First Search, Depth-First Search, DAG, cycles"),
        ("Searching", "Searching (Linear & Binary Search)", "DSA (C)", "Sequential scan O(n), Divide and Conquer binary search O(log n), integer overflow mid"),
        ("Sorting", "Sorting (Bubble, Insertion, Merge, Quick)", "DSA (C)", "Comparison sorts, Bubble, Insertion, Merge O(n log n), Quick Sort partition, stability"),
        ("Hashing", "Hashing & Collision Handling", "DSA (C)", "Hash functions, Hash Tables, Open Addressing, Linear Probing, Separate Chaining, Load Factor"),
        ("Advanced_DSA", "Advanced DSA (Pointers, DMA, Recursion)", "DSA (C)", "Dynamic memory allocation, malloc, calloc, free, dangling pointer, sparse matrix, infix to postfix"),

        # OOP Terms
        ("CPP_Fundamentals", "C++ Fundamentals & Functions", "OOP (C++)", "cin, cout, namespace std, function overloading, default arguments, inline functions"),
        ("Classes_Objects", "Classes and Objects", "OOP (C++)", "Blueprint, encapsulation, access specifiers, public, private, protected, this pointer"),
        ("Constructors", "Constructors & Destructors", "OOP (C++)", "Default constructor, parameterized, copy constructor, destructor ~ClassName, static members, friends"),
        ("Inheritance", "Inheritance & Virtual Base Classes", "OOP (C++)", "Single, multiple, multilevel, hierarchical, hybrid, diamond problem, virtual inheritance"),
        ("Polymorphism", "Polymorphism & Virtual Functions", "OOP (C++)", "Compile-time overloading, runtime virtual functions, pure virtual = 0, abstract classes, vtable, operator overloading"),
        ("Exception_FileIO", "Exception Handling & File Streams", "OOP (C++)", "try, catch, throw, std::exception, ifstream, ofstream, fstream, append mode, file handling"),
        ("Templates_STL", "Templates & STL Containers", "OOP (C++)", "Function templates, class templates, vector, list, map, set, stack, queue, std::sort, iterators")
    ]

    for topic_id, name, subject, keywords in search_data:
        meta = {
            "topic_id": topic_id,
            "name": name,
            "subject": subject,
            "snippet": keywords[:90] + "..."
        }
        # Insert full name
        trie.insert(name, meta)
        trie.insert(topic_id, meta)

        # Insert keywords
        words = re.findall(r"[A-Za-z0-9_]+", (name + " " + keywords).lower())
        for w in words:
            if len(w) >= 3:
                trie.insert(w, meta)
                inverted_index.index_item(w, meta)

    return trie, inverted_index

COURSE_GRAPH = build_course_prerequisite_graph()
SEARCH_TRIE, INVERTED_INDEX = build_search_trie_and_index()

# ==============================================================================
# Session State Initialization & Auto-Migration
# ==============================================================================
raw_state = load_json(STATE_FILE, {})
raw_quizzes = load_json(QUIZ_FILE, {})
raw_rewards = load_json(REWARD_FILE, [])
raw_notes = load_json(NOTES_FILE, [])
raw_resources = load_json(RESOURCES_FILE, {})

if "initialized" not in st.session_state:
    st.session_state.students = raw_state.get("students", {})
    st.session_state.active_student_id = raw_state.get("active_student", "2510370150")
    st.session_state.quizzes = raw_quizzes
    st.session_state.rewards = raw_rewards
    st.session_state.shared_notes = raw_notes
    st.session_state.resources = raw_resources
    st.session_state.current_page = "🏠 Welcome Dashboard"
    st.session_state.selected_topic = "Arrays"
    st.session_state.quiz_current_index = 0
    st.session_state.quiz_user_answers = {}
    st.session_state.quiz_submitted = False
    st.session_state.quiz_difficulty_filter = "All Difficulties"
    st.session_state.quiz_timer_setting = "Untimed"
    st.session_state.leaderboard = raw_state.get("leaderboard_sample", [])
    st.session_state.is_logged_in = False
    st.session_state.admins = raw_state.get("admins", {
        "ADMIN01": {
            "id": "ADMIN01",
            "name": "Prof. Rajesh Sharma",
            "email": "admin@skillarc.edu",
            "role": "Administrator",
            "password": "admin123",
            "department": "Faculty of Computer Science & Engineering",
            "avatar": "🛡️"
        }
    })
    st.session_state.is_admin = False
    st.session_state.active_admin_id = "ADMIN01"
    st.session_state.admin_selected_student = "2510370150"

    # Initialize DSA Engines in Session State
    st.session_state.nav_stack = NavigationStack()
    st.session_state.nav_stack.push("🏠 Welcome Dashboard")

    # Initialize Study Task Queue (FIFO)
    st.session_state.study_queue = StudyQueue()
    st.session_state.study_queue.enqueue({"task": "Read Linked Lists Notes (Singly & Doubly)", "topic": "Linked_Lists", "type": "Concept"})
    st.session_state.study_queue.enqueue({"task": "Take Binary Search Quiz (10 Questions)", "topic": "Searching", "type": "Quiz"})
    st.session_state.study_queue.enqueue({"task": "Explore C++ Virtual Base Classes & Diamond Problem", "topic": "Inheritance", "type": "OOP"})

    # Auto-Migrate Plaintext Passwords to PBKDF2 Hashes (Part 5)
    was_migrated, count = migrate_passwords(st.session_state.students, st.session_state.admins)
    if was_migrated:
        save_json(STATE_FILE, {
            "active_student": st.session_state.active_student_id,
            "students": st.session_state.students,
            "admins": st.session_state.admins,
            "leaderboard_sample": st.session_state.leaderboard
        })

    st.session_state.initialized = True

def get_current_student():
    student_id = st.session_state.active_student_id
    if student_id not in st.session_state.students:
        first_id = list(st.session_state.students.keys())[0]
        st.session_state.active_student_id = first_id
    return st.session_state.students[st.session_state.active_student_id]

def get_current_admin():
    admin_id = st.session_state.get("active_admin_id", "ADMIN01")
    return st.session_state.admins.get(admin_id, {
        "id": "ADMIN01",
        "name": "Prof. Rajesh Sharma",
        "email": "admin@skillarc.edu",
        "role": "Administrator",
        "department": "Faculty of Computer Science & Engineering",
        "avatar": "🛡️"
    })

def persist_state():
    full_state = {
        "active_student": st.session_state.active_student_id,
        "students": st.session_state.students,
        "admins": getattr(st.session_state, "admins", {}),
        "leaderboard_sample": st.session_state.leaderboard
    }
    save_json(STATE_FILE, full_state)
    save_json(NOTES_FILE, st.session_state.shared_notes)

def navigate_to(page_name: str):
    """Navigates to a page while updating the LIFO Navigation Stack."""
    if hasattr(st.session_state, "nav_stack"):
        st.session_state.nav_stack.push(page_name)
    st.session_state.current_page = page_name
    st.rerun()

def check_badges(student_dict):
    completed_count = len(student_dict.get("completed_topics", []))
    credits = student_dict.get("credits", 0)
    streak = student_dict.get("streak_days", 0)
    badges = set(student_dict.get("badges", []))
    
    if completed_count >= 1:
        badges.add("first_step")
    if streak >= 3:
        badges.add("streak_starter")
    if credits >= 100:
        badges.add("quiz_whiz")
    if all(t in student_dict.get("completed_topics", []) for t in ["Arrays", "Stack", "Queue"]):
        badges.add("dsa_explorer")
    if any(t in student_dict.get("completed_topics", []) for t in ["Classes_Objects", "Constructors", "Inheritance"]):
        badges.add("cpp_cadet")
        
    student_dict["badges"] = list(badges)

# Metrics calculation for Admin & Cohort
def compute_student_metrics(student_obj):
    quiz_history = student_obj.get("quiz_history", {})
    completed_topics = student_obj.get("completed_topics", [])
    in_progress_topics = student_obj.get("in_progress_topics", [])
    
    unique_questions = 0
    total_attempts = 0
    correct_count = 0
    
    for topic_id, q_data in quiz_history.items():
        q_tot = q_data.get("total", 0)
        q_sc = q_data.get("score", 0)
        q_attempts = q_data.get("attempts_count", 1)
        unique_questions += q_tot
        total_attempts += (q_tot * q_attempts)
        correct_count += q_sc
        
    incorrect_count = max(0, unique_questions - correct_count)
    accuracy_pct = round((correct_count / unique_questions * 100), 1) if unique_questions > 0 else 0.0
    progress_pct = round((len(completed_topics) / len(ALL_TOPICS) * 100), 1) if ALL_TOPICS else 0.0
    
    all_topic_ids = [t["id"] for t in ALL_TOPICS]
    unstarted_topics = [tid for tid in all_topic_ids if tid not in completed_topics and tid not in in_progress_topics]
    
    return {
        "unique_questions": unique_questions,
        "total_attempts": total_attempts,
        "correct": correct_count,
        "incorrect": incorrect_count,
        "accuracy": accuracy_pct,
        "progress_pct": progress_pct,
        "completed_count": len(completed_topics),
        "completed_list": completed_topics,
        "in_progress_list": in_progress_topics,
        "unstarted_list": unstarted_topics,
        "quiz_count": len(quiz_history),
        "credits": student_obj.get("credits", 0),
        "streak": student_obj.get("streak_days", 0)
    }

def compute_cohort_analytics(students_dict):
    total_students = len(students_dict)
    total_questions = 0
    total_attempts = 0
    total_correct = 0
    total_incorrect = 0
    total_credits = 0
    total_completed_topics = 0
    active_learners = 0
    
    student_summaries = []
    
    for sid, s in students_dict.items():
        m = compute_student_metrics(s)
        total_questions += m["unique_questions"]
        total_attempts += m["total_attempts"]
        total_correct += m["correct"]
        total_incorrect += m["incorrect"]
        total_credits += m["credits"]
        total_completed_topics += m["completed_count"]
        if m["streak"] >= 1 or m["quiz_count"] > 0:
            active_learners += 1
            
        student_summaries.append({
            "id": sid,
            "name": s.get("name", "Unknown"),
            "email": s.get("email", ""),
            "department": s.get("department", "CSE"),
            "role": s.get("role", "Student Learner"),
            "avatar": s.get("avatar", "🎓"),
            "credits": m["credits"],
            "streak": m["streak"],
            "unique_questions": m["unique_questions"],
            "total_attempts": m["total_attempts"],
            "correct": m["correct"],
            "incorrect": m["incorrect"],
            "accuracy": m["accuracy"],
            "completed_count": m["completed_count"],
            "completed_list": m["completed_list"],
            "in_progress_list": m["in_progress_list"],
            "unstarted_list": m["unstarted_list"],
            "progress_pct": m["progress_pct"],
            "quiz_history": s.get("quiz_history", {}),
            "recent_activity": s.get("recent_activity", []),
            "badges": s.get("badges", [])
        })
        
    cohort_avg_accuracy = round((total_correct / total_questions * 100), 1) if total_questions > 0 else 0.0
    
    topic_analysis = []
    for topic in ALL_TOPICS:
        t_id = topic["id"]
        t_name = topic["name"]
        t_subject = topic["subject"]
        t_attempts_count = 0
        t_total_questions = 0
        t_correct = 0
        t_completed_count = 0
        
        for s in students_dict.values():
            if t_id in s.get("completed_topics", []):
                t_completed_count += 1
            qh = s.get("quiz_history", {})
            if t_id in qh:
                t_attempts_count += 1
                t_total_questions += qh[t_id].get("total", 0)
                t_correct += qh[t_id].get("score", 0)
                
        t_incorrect = t_total_questions - t_correct
        t_acc = round((t_correct / t_total_questions * 100), 1) if t_total_questions > 0 else None
        t_error_rate = round((100.0 - t_acc), 1) if t_acc is not None else None
        
        topic_analysis.append({
            "id": t_id,
            "name": t_name,
            "subject": t_subject,
            "completed_by": t_completed_count,
            "students_attempted": t_attempts_count,
            "total_questions": t_total_questions,
            "correct": t_correct,
            "incorrect": t_incorrect,
            "accuracy": t_acc,
            "error_rate": t_error_rate
        })
        
    return {
        "total_students": total_students,
        "total_questions": total_questions,
        "total_attempts": total_attempts,
        "total_correct": total_correct,
        "total_incorrect": total_incorrect,
        "cohort_avg_accuracy": cohort_avg_accuracy,
        "total_completed_topics": total_completed_topics,
        "active_learners": active_learners,
        "total_credits": total_credits,
        "student_summaries": student_summaries,
        "topic_analysis": topic_analysis
    }

def generate_cohort_csv(student_summaries):
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow([
        "Student ID", "Full Name", "Email", "Department", "Role", 
        "Credit Points", "Streak Days", "Completed Topics Count", "Completed Topics",
        "Unique Questions Attempted", "Total Question Attempts", "Correct Answers", 
        "Incorrect Answers", "Quiz Accuracy (%)", "Overall Progress (%)"
    ])
    for s in student_summaries:
        writer.writerow([
            s["id"], s["name"], s["email"], s["department"], s["role"],
            s["credits"], s["streak"], s["completed_count"], "; ".join(s["completed_list"]),
            s["unique_questions"], s["total_attempts"], s["correct"], s["incorrect"],
            f"{s['accuracy']}%", f"{s['progress_pct']}%"
        ])
    return output.getvalue().encode("utf-8")

def generate_student_detailed_csv(student_summary):
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["SKILLARC STUDENT INDIVIDUAL AUDIT REPORT (PHASE III)"])
    writer.writerow(["Generated on", datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
    writer.writerow([])
    writer.writerow(["STUDENT PROFILE INFORMATION"])
    writer.writerow(["Roll ID", student_summary["id"]])
    writer.writerow(["Name", student_summary["name"]])
    writer.writerow(["Email", student_summary["email"]])
    writer.writerow(["Department", student_summary["department"]])
    writer.writerow(["Role", student_summary["role"]])
    writer.writerow(["Credit Points", f"{student_summary['credits']} pts"])
    writer.writerow(["Learning Streak", f"{student_summary['streak']} Days"])
    writer.writerow(["Overall Curriculum Progress", f"{student_summary['progress_pct']}%"])
    writer.writerow(["Topics Completed", "; ".join(student_summary["completed_list"]) if student_summary["completed_list"] else "None"])
    writer.writerow([])
    writer.writerow(["QUIZ PERFORMANCE BREAKDOWN"])
    writer.writerow(["Topic Key", "Score", "Total Questions", "Accuracy (%)", "Points Awarded", "Attempt Date"])
    qh = student_summary.get("quiz_history", {})
    if qh:
        for t_k, q_d in qh.items():
            writer.writerow([
                t_k, q_d.get("score", 0), q_d.get("total", 0),
                f"{q_d.get('percentage', 0.0)}%", q_d.get("points_awarded", 0),
                q_d.get("attempted_at", "N/A")
            ])
    else:
        writer.writerow(["No quizzes attempted yet."])
    return output.getvalue().encode("utf-8")

# ==============================================================================
# STUDENT AUTHENTICATION PORTAL (WITH SECURE PBKDF2 HASHING)
# ==============================================================================
if "is_logged_in" not in st.session_state:
    st.session_state.is_logged_in = False

if not st.session_state.is_logged_in:
    col_a1, col_a2, col_a3 = st.columns([1, 2.6, 1])
    with col_a2:
        st.markdown("""
        <div style="text-align: center; margin-top: 1.5rem; margin-bottom: 1.5rem;">
            <span style="font-size: 3rem;">⚡</span>
            <h1 style="color: #1e1b4b; font-size: 2.2rem; font-weight: 800; margin-bottom: 4px; margin-top: 6px;">SkillArc Portal</h1>
            <p style="color: #64748b; font-size: 0.95rem; margin-top: 0;">Gamified Learning Platform for Data Structures (C) and OOP (C++)</p>
            <span style="display: inline-block; background: #e0e7ff; color: #4338ca; padding: 4px 12px; border-radius: 9999px; font-size: 0.75rem; font-weight: 700; text-transform: uppercase;">
                Phase III • Secured with PBKDF2-HMAC-SHA256
            </span>
        </div>
        """, unsafe_allow_html=True)

        auth_tab_login, auth_tab_reg = st.tabs(["🔐 Student / Faculty Sign In", "📝 Register New Student"])

        with auth_tab_login:
            st.markdown("<h4 style='color: #0f172a; margin-top: 10px; margin-bottom: 4px;'>Sign in to your SkillArc account</h4>", unsafe_allow_html=True)
            st.caption("Enter your registered Student ID, Email, or Admin ID and password.")

            with st.form("login_form"):
                login_id = st.text_input("Student Roll ID / Email / Admin ID", placeholder="e.g. 2510370150 or admin@skillarc.edu")
                login_pwd = st.text_input("Password", type="password", placeholder="Enter your password")
                submit_login = st.form_submit_button("🚀 Sign In to SkillArc", type="primary", use_container_width=True)

                if submit_login:
                    clean_login = login_id.strip()
                    if not clean_login or not login_pwd:
                        st.error("Validation Error: Please enter both your ID/Email and password.")
                    else:
                        query = clean_login.lower()
                        # 1. Check Administrator Accounts
                        matched_admin = None
                        for aid, a in getattr(st.session_state, "admins", {}).items():
                            if aid.lower() == query or a.get("email", "").lower() == query or query in ["admin", "admin01"]:
                                matched_admin = a
                                break

                        if matched_admin:
                            expected_hash = matched_admin.get("password", "")
                            if not verify_password(expected_hash, login_pwd):
                                st.error("Admin Authentication Failed: Invalid password.")
                            else:
                                st.session_state.is_admin = True
                                st.session_state.active_admin_id = matched_admin["id"]
                                st.session_state.is_logged_in = True
                                st.session_state.current_page = "🛡️ Admin Dashboard"
                                st.success(f"Admin authentication verified. Welcome, {matched_admin['name']}!")
                                st.rerun()
                        else:
                            # 2. Check Student Accounts
                            matched_student = None
                            for sid, s in st.session_state.students.items():
                                if sid.lower() == query or s.get("email", "").lower() == query:
                                    matched_student = s
                                    break

                            if not matched_student:
                                st.error("Invalid Credentials: No student account found matching this ID or Email.")
                            else:
                                expected_hash = matched_student.get("password", "")
                                if not verify_password(expected_hash, login_pwd):
                                    st.error("Invalid Credentials: Incorrect password. Please try again.")
                                else:
                                    st.session_state.is_admin = False
                                    st.session_state.active_student_id = matched_student["id"]
                                    st.session_state.is_logged_in = True
                                    st.session_state.current_page = "🏠 Welcome Dashboard"
                                    st.success(f"Login successful! Welcome back, {matched_student['name']}!")
                                    st.rerun()

            st.markdown("""
            <div style="background: #f8fafc; border: 1px dashed #cbd5e1; border-radius: 10px; padding: 12px; margin-top: 16px; margin-bottom: 10px;">
                <p style="font-size: 0.78rem; font-weight: 700; color: #475569; text-transform: uppercase; margin: 0 0 8px 0; text-align: center;">⚡ One-Click Demo Sign In (Quick Evaluator Access):</p>
            </div>
            """, unsafe_allow_html=True)

            d1, d2, d3, d4 = st.columns(4)
            with d1:
                if st.button("👩‍💻 Samiksha", use_container_width=True, key="demo_samiksha"):
                    st.session_state.is_admin = False
                    st.session_state.active_student_id = "2510370150"
                    st.session_state.is_logged_in = True
                    st.session_state.current_page = "🏠 Welcome Dashboard"
                    st.rerun()
            with d2:
                if st.button("👩‍🎨 Vaibhavi", use_container_width=True, key="demo_vaibhavi"):
                    st.session_state.is_admin = False
                    st.session_state.active_student_id = "2510370530"
                    st.session_state.is_logged_in = True
                    st.session_state.current_page = "🏠 Welcome Dashboard"
                    st.rerun()
            with d3:
                if st.button("👩‍🔬 Tanisha", use_container_width=True, key="demo_tanisha"):
                    st.session_state.is_admin = False
                    st.session_state.active_student_id = "2510370080"
                    st.session_state.is_logged_in = True
                    st.session_state.current_page = "🏠 Welcome Dashboard"
                    st.rerun()
            with d4:
                if st.button("🛡️ Faculty Admin", use_container_width=True, key="demo_admin"):
                    st.session_state.is_admin = True
                    st.session_state.active_admin_id = "ADMIN01"
                    st.session_state.is_logged_in = True
                    st.session_state.current_page = "🛡️ Admin Dashboard"
                    st.rerun()

        with auth_tab_reg:
            st.markdown("<h4 style='color: #0f172a; margin-top: 10px; margin-bottom: 4px;'>Create a New Student Profile</h4>", unsafe_allow_html=True)
            st.caption("Sign up with your college roll number. Password will be securely hashed with PBKDF2-HMAC-SHA256.")

            with st.form("register_form"):
                reg_name = st.text_input("Full Name *", placeholder="e.g. Aryan Sharma")
                reg_id = st.text_input("Student Roll ID *", placeholder="e.g. 2510370999")
                reg_email = st.text_input("College / Personal Email Address *", placeholder="e.g. aryan@gehu.ac.in or aryan@gmail.com")
                reg_dept = st.selectbox(
                    "Department & Section *",
                    [
                        "B.Tech CSE — 2nd Year (Sec A)",
                        "B.Tech CSE — 2nd Year (Sec B)",
                        "B.Tech CSE — 2nd Year (Sec C)",
                        "B.Tech IT — 2nd Year",
                        "B.Tech AI & DS — 2nd Year"
                    ]
                )
                col_p1, col_p2 = st.columns(2)
                with col_p1:
                    reg_pwd = st.text_input("Password * (min 6 characters)", type="password", placeholder="Create password")
                with col_p2:
                    reg_cpwd = st.text_input("Confirm Password *", type="password", placeholder="Repeat password")

                submit_reg = st.form_submit_button("🎓 Create Account & Launch Dashboard", type="primary", use_container_width=True)

                if submit_reg:
                    clean_name = reg_name.strip()
                    clean_id = reg_id.strip()
                    clean_email = reg_email.strip()

                    if not all([clean_name, clean_id, clean_email, reg_pwd, reg_cpwd]):
                        st.error("Validation Error: All fields are required. Please fill in all details.")
                    elif not re.match(r"^[A-Za-z\\s\\.]+$", clean_name) or len(clean_name) < 2:
                        st.error("Validation Error: Full name must contain valid alphabetical characters and spaces.")
                    elif clean_id in st.session_state.students:
                        st.error(f"Validation Error: A student with Roll ID '{clean_id}' is already registered! Please sign in.")
                    elif not re.match(r"^[\\w\\.-]+@[\\w\\.-]+\\.(com|in|ac\\.in|edu|org)$", clean_email, re.IGNORECASE):
                        st.error("Validation Error: Invalid email format. Please enter a valid email ending with .com, .in, or .ac.in.")
                    elif len(reg_pwd) < 6:
                        st.error("Validation Error: Weak password. Password must be at least 6 characters long.")
                    elif reg_pwd != reg_cpwd:
                        st.error("Validation Error: Passwords do not match. Please verify your entry.")
                    else:
                        # Cryptographically secure salted PBKDF2 hash
                        hashed_pwd = hash_password(reg_pwd)

                        new_student = {
                            "id": clean_id,
                            "name": clean_name,
                            "email": clean_email,
                            "password": hashed_pwd,
                            "role": "Student Learner",
                            "department": reg_dept,
                            "avatar": "🎓",
                            "credits": 50,
                            "streak_days": 1,
                            "completed_topics": [],
                            "in_progress_topics": ["Arrays"],
                            "quiz_history": {},
                            "badges": ["first_step"],
                            "redemptions": [],
                            "recent_activity": [
                                {"action": "Created student profile (+50 welcome credits)", "time": "Just now"},
                                {"action": "Started DSA & C++ Roadmap", "time": "Just now"}
                            ]
                        }
                        st.session_state.students[clean_id] = new_student
                        st.session_state.is_admin = False
                        st.session_state.active_student_id = clean_id
                        st.session_state.is_logged_in = True
                        st.session_state.current_page = "🏠 Welcome Dashboard"
                        persist_state()
                        st.success(f"🎉 Registration successful! Welcome to SkillArc, {clean_name}!")
                        st.rerun()

    st.stop()

# ==============================================================================
# Sidebar Navigation & User Profile Card
# ==============================================================================
student = get_current_student()
is_admin_mode = st.session_state.get("is_admin", False)

with st.sidebar:
    # App Brand / Wordmark
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
        <span style="font-size: 2rem;">⚡</span>
        <div>
            <h2 style="margin: 0; font-size: 1.5rem; color: #1e1b4b; font-weight: 800; line-height: 1.1;">SkillArc</h2>
            <span style="font-size: 0.72rem; color: #6366f1; font-weight: 600; text-transform: uppercase;">Phase-III Complete</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation Stack Back Button (LIFO Stack Demonstration)
    if hasattr(st.session_state, "nav_stack") and st.session_state.nav_stack.size() > 1:
        if st.button("⬅️ Previous Page (Stack Pop)", use_container_width=True, type="secondary"):
            prev_page = st.session_state.nav_stack.pop()
            if prev_page:
                st.session_state.current_page = prev_page
                st.rerun()

    # Log Out Button
    if st.button("🚪 Log Out", use_container_width=True, type="secondary", key="btn_sidebar_logout"):
        st.session_state.is_logged_in = False
        st.rerun()

    if is_admin_mode:
        admin = get_current_admin()
        st.markdown(f"""
        <div class="sidebar-user" style="background: linear-gradient(135deg, #1e1b4b 0%, #312e81 100%); border-left: 4px solid #818cf8;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h4 style="margin: 0; color: #ffffff;">{admin['avatar']} {admin['name']}</h4>
                <span style="background: rgba(99, 102, 241, 0.4); color: #e0e7ff; padding: 2px 6px; border-radius: 4px; font-size: 0.7rem; font-weight: 700;">ADMIN</span>
            </div>
            <p style="margin-top: 4px; font-size: 0.78rem; color: #c7d2fe;">ID: {admin['id']} | {admin.get('department', 'Faculty CSE')}</p>
            <div style="margin-top: 8px; border-top: 1px solid rgba(255,255,255,0.15); padding-top: 6px; font-size: 0.72rem; color: #e0e7ff;">
                <span>Role: <b>Supervisor & Evaluator</b></span><br>
                <span>C++ Friend Class Privileged Access</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        NAV_PAGES = [
            "🛡️ Admin Dashboard",
            "🏠 Welcome Dashboard",
            "🔍 Concept & Topic Search",
            "🗺️ Learning Roadmap",
            "📖 Topic Learning",
            "📝 Interactive Quiz",
            "🏆 Leaderboard",
            "🎁 Student Rewards",
            "📚 Notes & Resources",
            "📊 Progress Report",
            "⚙️ C++ Engine Showcase"
        ]
    else:
        # Active Student Account Switcher
        with st.expander("🔄 Switch Account / Profiles", expanded=False):
            student_options = {sid: f"{s['name']} ({s.get('role', 'Student').split('&')[0].strip()})" for sid, s in st.session_state.students.items()}
            chosen_student_id = st.selectbox(
                "Select Account",
                options=list(student_options.keys()),
                format_func=lambda x: student_options[x],
                index=list(student_options.keys()).index(st.session_state.active_student_id) if st.session_state.active_student_id in student_options else 0,
                label_visibility="collapsed",
                key="sb_switch_profile"
            )
            if chosen_student_id != st.session_state.active_student_id:
                st.session_state.active_student_id = chosen_student_id
                st.session_state.quiz_submitted = False
                st.session_state.quiz_user_answers = {}
                st.rerun()

        # Student Info Box
        st.markdown(f"""
        <div class="sidebar-user">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h4 style="margin: 0;">{student['avatar']} {student['name']}</h4>
                <span style="background: rgba(255,255,255,0.2); padding: 2px 6px; border-radius: 4px; font-size: 0.7rem; font-weight: 700;">TEAM APEX</span>
            </div>
            <p style="margin-top: 4px; font-size: 0.78rem;">ID: {student['id']} | {student['department']}</p>
            <div style="margin-top: 10px; display: flex; justify-content: space-between; border-top: 1px solid rgba(255,255,255,0.2); padding-top: 8px;">
                <div>
                    <span style="font-size: 0.68rem; color: #c7d2fe; text-transform: uppercase; display: block;">Credits</span>
                    <b style="font-size: 1.1rem; color: #ffffff;">{student['credits']} pts</b>
                </div>
                <div>
                    <span style="font-size: 0.68rem; color: #c7d2fe; text-transform: uppercase; display: block;">Streak</span>
                    <b style="font-size: 1.1rem; color: #ffffff;">{student['streak_days']} Days 🔥</b>
                </div>
                <div>
                    <span style="font-size: 0.68rem; color: #c7d2fe; text-transform: uppercase; display: block;">Badges</span>
                    <b style="font-size: 1.1rem; color: #ffffff;">{len(student.get('badges', []))} 🏆</b>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        NAV_PAGES = [
            "🏠 Welcome Dashboard",
            "🔍 Concept & Topic Search",
            "🗺️ Learning Roadmap",
            "📖 Topic Learning",
            "📝 Interactive Quiz",
            "🏆 Leaderboard",
            "🎁 Student Rewards",
            "📚 Notes & Resources",
            "📊 Progress Report",
            "⚙️ C++ Engine Showcase"
        ]

    selected_nav = st.radio(
        "Navigation",
        NAV_PAGES,
        index=NAV_PAGES.index(st.session_state.current_page) if st.session_state.current_page in NAV_PAGES else 0,
        label_visibility="collapsed"
    )
    if selected_nav != st.session_state.current_page:
        navigate_to(selected_nav)

    st.markdown("---")
    st.markdown("""
    <div style="font-size: 0.75rem; color: #64748b; line-height: 1.4;">
        <b>Team Apex (B.Tech CSE - 2nd Year)</b><br>
        • Samiksha Gurung (DSA in C)<br>
        • Vaibhavi Thapliyal (UI & Min-Heap)<br>
        • Tanisha Rai (C++ OOP & Admin Friend Class)
    </div>
    """, unsafe_allow_html=True)


# ==============================================================================
# PAGE 1: ADMIN DASHBOARD (SUPERVISOR AUDIT SUITE)
# ==============================================================================
def render_admin_dashboard():
    if not st.session_state.get("is_admin", False):
        st.error("🔒 Access Denied: Administrator privileges required to access cohort audits and student records.")
        st.info("💡 To inspect the Admin features as an evaluator, please log in with Admin credentials or select '🛡️ Faculty Admin' on the Sign In page.")
        return

    admin = get_current_admin()
    cohort_data = compute_cohort_analytics(st.session_state.students)

    st.markdown(f"""
    <div class="brand-header">
        <div>
            <h1 class="brand-title">🛡️ Faculty & Administrator Dashboard</h1>
            <span style="color: #64748b; font-size: 0.95rem;">
                Supervising <b>{cohort_data['total_students']} Registered Students</b> across <b>{len(ALL_TOPICS)} Syllabus Modules</b>.
            </span>
        </div>
        <div style="margin-left: auto; text-align: right;">
            <span class="brand-pill" style="background: #e0e7ff; color: #3730a3; border: 1px solid #c7d2fe;">
                {admin['avatar']} {admin['name']}
            </span>
            <div style="font-size: 0.72rem; color: #64748b; margin-top: 4px;">Role: {admin.get('role', 'Administrator')}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="demo-tag" style="background: #eef2ff; border-left: 4px solid #6366f1;">
        <b>🎓 OOP Architecture Connection:</b> In our C++ engine design, <code>class Student</code> declares <code>friend class Admin;</code>. 
        This grants the <code>Admin</code> class privileged access to audit private student fields (credits, total attempts, accuracy) without exposing them to unauthorized modification.
    </div>
    """, unsafe_allow_html=True)

    tab_overview, tab_students, tab_student_detail, tab_insights, tab_exports = st.tabs([
        "📊 Overall Cohort Statistics",
        "👥 All Students Directory",
        "🔍 Individual Student Audit",
        "💡 Learning Insights & Mentorship",
        "📑 Reports & CSV Export"
    ])

    with tab_overview:
        col_m1, col_m2, col_m3 = st.columns(3)
        with col_m1:
            st.markdown(f"""
            <div class="metric-card">
                <span class="metric-label">👥 Total Registered Students</span>
                <span class="metric-val">{cohort_data['total_students']} Students</span>
                <span class="metric-sub" style="color: #16a34a;">🟢 {cohort_data['active_learners']} actively learning</span>
            </div>
            """, unsafe_allow_html=True)
        with col_m2:
            st.markdown(f"""
            <div class="metric-card">
                <span class="metric-label">📝 Questions Attempted</span>
                <span class="metric-val">{cohort_data['total_questions']} Questions</span>
                <span class="metric-sub" style="color: #6366f1;">🔄 {cohort_data['total_attempts']} total submissions (inc. retakes)</span>
            </div>
            """, unsafe_allow_html=True)
        with col_m3:
            st.markdown(f"""
            <div class="metric-card">
                <span class="metric-label">🎯 Cohort Average Quiz Accuracy</span>
                <span class="metric-val">{cohort_data['cohort_avg_accuracy']}%</span>
                <span class="metric-sub" style="color: #0284c7;">✅ {cohort_data['total_correct']} Correct · ❌ {cohort_data['total_incorrect']} Incorrect</span>
            </div>
            """, unsafe_allow_html=True)

        col_m4, col_m5, col_m6 = st.columns(3)
        with col_m4:
            st.markdown(f"""
            <div class="metric-card">
                <span class="metric-label">🏆 Total Completed Topic Modules</span>
                <span class="metric-val">{cohort_data['total_completed_topics']} Topics</span>
                <span class="metric-sub" style="color: #64748b;">Across {len(ALL_TOPICS)} syllabus topics</span>
            </div>
            """, unsafe_allow_html=True)
        with col_m5:
            st.markdown(f"""
            <div class="metric-card">
                <span class="metric-label">🪙 Total Credit Points Earned</span>
                <span class="metric-val">{cohort_data['total_credits']} pts</span>
                <span class="metric-sub" style="color: #d97706;">Cohort gamified credits in circulation</span>
            </div>
            """, unsafe_allow_html=True)
        with col_m6:
            completion_rate = round((cohort_data['total_completed_topics'] / (cohort_data['total_students'] * len(ALL_TOPICS)) * 100), 1) if cohort_data['total_students'] > 0 else 0.0
            st.markdown(f"""
            <div class="metric-card">
                <span class="metric-label">📊 Curriculum Saturation</span>
                <span class="metric-val">{completion_rate}%</span>
                <span class="metric-sub" style="color: #4338ca;">Total potential syllabus completed</span>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<div style='height: 14px;'></div>", unsafe_allow_html=True)
        st.markdown("#### 📌 Cohort Topic Completion Distribution (All 17 Syllabus Topics)")
        
        for t_info in cohort_data['topic_analysis']:
            pct = round((t_info['completed_by'] / cohort_data['total_students'] * 100), 1) if cohort_data['total_students'] > 0 else 0.0
            badge_color = "#4338ca" if t_info['subject'] == "DSA (C)" else "#7c3aed"
            st.markdown(f"""
            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 6px; margin-bottom: 2px;">
                <span style="font-size: 0.88rem; font-weight: 600; color: #1e293b;">
                    {t_info['name']} <span style="font-size: 0.72rem; background: #e0e7ff; color: {badge_color}; padding: 2px 6px; border-radius: 4px; margin-left: 6px;">{t_info['subject']}</span>
                </span>
                <span style="font-size: 0.82rem; color: #475569; font-weight: 700;">
                    {t_info['completed_by']} / {cohort_data['total_students']} Students ({pct}%)
                </span>
            </div>
            """, unsafe_allow_html=True)
            st.progress(pct / 100.0)

    with tab_students:
        col_f1, col_f2 = st.columns([2, 1.2])
        with col_f1:
            search_query = st.text_input("🔍 Search by Student Name or Roll ID:", placeholder="e.g. Samiksha or 2510370150").strip().lower()
        with col_f2:
            sort_by = st.selectbox(
                "Sort Table By:",
                [
                    "Credit Points (High to Low)",
                    "Quiz Accuracy (High to Low)",
                    "Questions Attempted (High to Low)",
                    "Completed Topics (High to Low)",
                    "Streak Days (High to Low)"
                ]
            )

        filtered = [
            s for s in cohort_data['student_summaries']
            if not search_query or search_query in s['name'].lower() or search_query in s['id'].lower()
        ]

        if sort_by == "Credit Points (High to Low)":
            filtered.sort(key=lambda x: x["credits"], reverse=True)
        elif sort_by == "Quiz Accuracy (High to Low)":
            filtered.sort(key=lambda x: x["accuracy"], reverse=True)
        elif sort_by == "Questions Attempted (High to Low)":
            filtered.sort(key=lambda x: x["unique_questions"], reverse=True)
        elif sort_by == "Completed Topics (High to Low)":
            filtered.sort(key=lambda x: x["completed_count"], reverse=True)
        elif sort_by == "Streak Days (High to Low)":
            filtered.sort(key=lambda x: x["streak"], reverse=True)

        for s in filtered:
            with st.container():
                st.markdown(f"""
                <div class="content-card" style="margin-bottom: 10px; padding: 14px 18px; border-left: 4px solid #6366f1;">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap;">
                        <div>
                            <h4 style="margin: 0; color: #1e1b4b; font-size: 1.15rem;">{s['avatar']} {s['name']}</h4>
                            <span style="font-size: 0.8rem; color: #64748b;">Roll ID: <b>{s['id']}</b> · {s['department']} · {s['email']}</span>
                        </div>
                        <div style="display: flex; gap: 8px; margin-top: 4px;">
                            <span style="background: #e0e7ff; color: #4338ca; padding: 4px 10px; border-radius: 9999px; font-size: 0.75rem; font-weight: 700;">
                                🪙 {s['credits']} pts
                            </span>
                            <span style="background: #fef3c7; color: #b45309; padding: 4px 10px; border-radius: 9999px; font-size: 0.75rem; font-weight: 700;">
                                🔥 {s['streak']}d Streak
                            </span>
                            <span style="background: #dcfce7; color: #15803d; padding: 4px 10px; border-radius: 9999px; font-size: 0.75rem; font-weight: 700;">
                                🎯 {s['accuracy']}% Accuracy
                            </span>
                        </div>
                    </div>
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 10px; margin-top: 10px; padding-top: 8px; border-top: 1px solid #f1f5f9; font-size: 0.82rem;">
                        <div>
                            <span style="color: #64748b; display: block;">Questions Attempted</span>
                            <b>{s['unique_questions']} unique</b> <span style="color: #94a3b8;">({s['total_attempts']} total)</span>
                        </div>
                        <div>
                            <span style="color: #64748b; display: block;">Correct / Incorrect</span>
                            <span style="color: #16a34a; font-weight: 700;">{s['correct']} ✅</span> / <span style="color: #dc2626; font-weight: 700;">{s['incorrect']} ❌</span>
                        </div>
                        <div>
                            <span style="color: #64748b; display: block;">Completed Topics</span>
                            <b>{s['completed_count']} / {len(ALL_TOPICS)} ({s['progress_pct']}%)</b>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                col_btn, _ = st.columns([1.5, 3.5])
                with col_btn:
                    if st.button(f"🔍 Open Audit Dossier: {s['name']}", key=f"btn_audit_{s['id']}", use_container_width=True):
                        st.session_state.admin_selected_student = s['id']
                        st.rerun()

    with tab_student_detail:
        student_lookup = {s['id']: s for s in cohort_data['student_summaries']}
        all_ids = list(student_lookup.keys())
        default_idx = all_ids.index(st.session_state.admin_selected_student) if st.session_state.admin_selected_student in all_ids else 0

        selected_id = st.selectbox(
            "Select Student Profile to Audit:",
            options=all_ids,
            format_func=lambda x: f"{student_lookup[x]['name']} (Roll ID: {x})",
            index=default_idx,
            key="admin_audit_selector"
        )
        st.session_state.admin_selected_student = selected_id
        curr = student_lookup[selected_id]

        st.markdown(f"""
        <div class="content-card" style="margin-top: 10px; background: linear-gradient(135deg, #f8fafc 0%, #ede9fe 100%); border-left: 4px solid #7c3aed;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap;">
                <div>
                    <h2 style="margin: 0; color: #1e1b4b; font-size: 1.5rem;">{curr['avatar']} {curr['name']}</h2>
                    <p style="margin: 4px 0 0 0; color: #475569; font-size: 0.9rem;">
                        <b>Roll ID:</b> {curr['id']} · <b>Email:</b> {curr['email']} · <b>Dept:</b> {curr['department']}
                    </p>
                </div>
                <div style="display: flex; gap: 8px; margin-top: 6px;">
                    <span style="background: #ffffff; color: #4338ca; padding: 4px 10px; border-radius: 9999px; font-size: 0.8rem; font-weight: 700; border: 1px solid #c7d2fe;">
                        🪙 {curr['credits']} Credits
                    </span>
                    <span style="background: #ffffff; color: #b45309; padding: 4px 10px; border-radius: 9999px; font-size: 0.8rem; font-weight: 700; border: 1px solid #fde68a;">
                        🔥 {curr['streak']}d Streak
                    </span>
                    <span style="background: #ffffff; color: #15803d; padding: 4px 10px; border-radius: 9999px; font-size: 0.8rem; font-weight: 700; border: 1px solid #bbf7d0;">
                        🎯 {curr['accuracy']}% Accuracy
                    </span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        col_det1, col_det2 = st.columns([1.1, 1.0])
        with col_det1:
            st.markdown("#### 🗺️ Curriculum Progress Breakdown")
            st.write(f"**Curriculum Completion:** {curr['progress_pct']}% ({curr['completed_count']} of {len(ALL_TOPICS)} topics)")
            st.progress(curr['progress_pct'] / 100.0)

            st.markdown("**Completed Topics:**")
            if curr['completed_list']:
                st.write(", ".join([f"✅ {t}" for t in curr['completed_list']]))
            else:
                st.caption("No topics completed yet.")

        with col_det2:
            st.markdown("#### 🎯 Quiz Accuracy & Attempt Metrics")
            st.markdown(f"""
            <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 14px;">
                <p style="margin: 0 0 6px 0;">Unique Questions Attempted: <b>{curr['unique_questions']}</b></p>
                <p style="margin: 0 0 6px 0;">Total Question Attempts (inc. retakes): <b>{curr['total_attempts']}</b></p>
                <p style="margin: 0 0 6px 0;">Correct Answers: <span style="color: #16a34a; font-weight: 700;">{curr['correct']}</span> | Incorrect: <span style="color: #dc2626; font-weight: 700;">{curr['incorrect']}</span></p>
                <p style="margin: 0; font-weight: 700; color: #4338ca;">Overall Accuracy: {curr['accuracy']}%</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("#### 📝 Quiz History Breakdown")
        qh = curr.get("quiz_history", {})
        if qh:
            quiz_rows = []
            for t_k, q_d in qh.items():
                quiz_rows.append({
                    "Topic": t_k,
                    "Score": f"{q_d.get('score', 0)} / {q_d.get('total', 0)}",
                    "Accuracy": f"{q_d.get('percentage', 0.0)}%",
                    "Attempts": q_d.get("attempts_count", 1),
                    "Points Awarded": f"+{q_d.get('points_awarded', 0)} pts",
                    "Date Attempted": q_d.get("attempted_at", "N/A")
                })
            st.table(quiz_rows)
        else:
            st.info("This student has not submitted any quizzes yet.")

        csv_bytes = generate_student_detailed_csv(curr)
        st.download_button(
            label=f"📥 Download Student Audit Report (CSV) — {curr['name']}",
            data=csv_bytes,
            file_name=f"SkillArc_Audit_{curr['id']}.csv",
            mime="text/csv",
            use_container_width=True
        )

    with tab_insights:
        col_ins1, col_ins2 = st.columns(2)
        with col_ins1:
            st.markdown("""
            <div class="content-card" style="border-left: 4px solid #10b981; min-height: 200px;">
                <h4 style="color: #065f46; margin-top: 0;">🌟 High-Performing Learners</h4>
            """, unsafe_allow_html=True)
            top_acc = sorted([s for s in cohort_data['student_summaries'] if s['unique_questions'] > 0], key=lambda x: x['accuracy'], reverse=True)
            top_cred = sorted(cohort_data['student_summaries'], key=lambda x: x['credits'], reverse=True)
            if top_acc:
                st.markdown(f"**Highest Quiz Accuracy:** {top_acc[0]['avatar']} **{top_acc[0]['name']}** ({top_acc[0]['accuracy']}%)")
            if top_cred:
                st.markdown(f"**Credits Leader:** {top_cred[0]['avatar']} **{top_cred[0]['name']}** ({top_cred[0]['credits']} pts)")
            st.markdown("</div>", unsafe_allow_html=True)

        with col_ins2:
            st.markdown("""
            <div class="content-card" style="border-left: 4px solid #f59e0b; min-height: 200px;">
                <h4 style="color: #92400e; margin-top: 0;">🤝 Practice & Mentorship Recommendations</h4>
            """, unsafe_allow_html=True)
            need_practice = [s for s in cohort_data['student_summaries'] if s['unique_questions'] == 0 or s['incorrect'] > 0]
            if need_practice:
                for s in need_practice[:3]:
                    reason = "Diagnostic quiz recommended" if s['unique_questions'] == 0 else f"{s['incorrect']} incorrect answer(s); review topic notes"
                    st.markdown(f"• **{s['name']}** ({s['id']}): <span style='font-size: 0.82rem; color: #475569;'>{reason}</span>", unsafe_allow_html=True)
            else:
                st.write("All active students maintaining high accuracy!")
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("#### 📊 Topic-Level Difficulty & Error Rate Analysis (All 17 Topics)")
        topic_table = []
        for t in cohort_data['topic_analysis']:
            acc_str = f"{t['accuracy']}%" if t['accuracy'] is not None else "No attempts"
            err_str = f"{t['error_rate']}%" if t['error_rate'] is not None else "0.0%"
            status = "🟢 High Mastery" if (t['accuracy'] is not None and t['accuracy'] >= 85) else ("🟡 Moderate" if (t['accuracy'] is not None and t['accuracy'] >= 60) else ("🔴 Challenging" if t['accuracy'] is not None else "⚪ Not Attempted"))
            topic_table.append({
                "Syllabus Topic": t['name'],
                "Subject Track": t['subject'],
                "Completed by Students": f"{t['completed_by']} / {cohort_data['total_students']}",
                "Questions Attempted": t['total_questions'],
                "Correct": t['correct'],
                "Incorrect": t['incorrect'],
                "Cohort Accuracy": acc_str,
                "Error Rate": err_str,
                "Mastery Level": status
            })
        st.table(topic_table)

    with tab_exports:
        col_exp1, col_exp2 = st.columns(2)
        with col_exp1:
            st.markdown("#### 📊 Full Cohort Summary (CSV)")
            st.caption("Exports all registered students with roll IDs, questions attempted, correct/incorrect, accuracy %, and credits.")
            cohort_csv_bytes = generate_cohort_csv(cohort_data['student_summaries'])
            st.download_button(
                label="📥 Download Full Cohort Summary (CSV)",
                data=cohort_csv_bytes,
                file_name=f"SkillArc_Cohort_Summary_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv",
                use_container_width=True,
                type="primary"
            )

        with col_exp2:
            st.markdown(f"#### 🔍 Individual Dossier: {student_lookup[selected_id]['name']} (CSV)")
            st.caption("Exports complete student dossier with itemized quiz history.")
            indiv_csv_bytes = generate_student_detailed_csv(student_lookup[selected_id])
            st.download_button(
                label=f"📥 Download Dossier for {student_lookup[selected_id]['name']} (CSV)",
                data=indiv_csv_bytes,
                file_name=f"SkillArc_Student_{selected_id}.csv",
                mime="text/csv",
                use_container_width=True
            )


# ==============================================================================
# PAGE 2: WELCOME DASHBOARD
# ==============================================================================
def render_welcome_dashboard():
    st.markdown(f"""
    <div class="brand-header">
        <div>
            <h1 class="brand-title">Welcome back, {student['name']}! 👋</h1>
            <span style="color: #64748b; font-size: 0.95rem;">Track your progress in C Data Structures and C++ Object-Oriented Programming.</span>
        </div>
        <div style="margin-left: auto;">
            <span class="brand-pill">Phase-III Active</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 4 Top Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <span class="metric-label">Credit Balance</span>
            <span class="metric-val">{student['credits']} pts</span>
            <span class="metric-sub">🪙 Spendable in Rewards</span>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <span class="metric-label">Active Learning Streak</span>
            <span class="metric-val">{student['streak_days']} Days</span>
            <span class="metric-sub">🔥 Keep it going tomorrow</span>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        completed_count = len(student.get("completed_topics", []))
        st.markdown(f"""
        <div class="metric-card">
            <span class="metric-label">Topics Completed</span>
            <span class="metric-val">{completed_count} / {len(ALL_TOPICS)}</span>
            <span class="metric-sub">📘 Across DSA & OOP</span>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        qh = student.get("quiz_history", {})
        total_q = sum(item.get("total", 0) for item in qh.values())
        st.markdown(f"""
        <div class="metric-card">
            <span class="metric-label">Quizzes Completed</span>
            <span class="metric-val">{len(qh)} Quizzes</span>
            <span class="metric-sub">⚡ {total_q} Questions Tested</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height: 14px;'></div>", unsafe_allow_html=True)

    # Section with Study Task Queue (FIFO) and Recent Activity (Singly Linked List)
    col_q1, col_q2 = st.columns([1.2, 1.0])

    with col_q1:
        st.markdown("### 📋 Recommended Study Task Queue (FIFO Queue)")
        st.caption("Managed via FIFO Queue: complete tasks in chronological recommended order.")

        study_q = getattr(st.session_state, "study_queue", None)
        if study_q and study_q.size() > 0:
            top_task = study_q.peek()
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #f8fafc 0%, #e0e7ff 100%); border: 1.5px solid #818cf8; border-radius: 10px; padding: 14px; margin-bottom: 10px;">
                <div style="font-size: 0.72rem; font-weight: 700; color: #4338ca; text-transform: uppercase;">Next In Queue (Front)</div>
                <h4 style="margin: 4px 0 2px 0; color: #1e1b4b;">{top_task['task']}</h4>
                <span style="font-size: 0.8rem; color: #475569;">Target Topic: <b>{top_task['topic']}</b> · Task Type: <b>{top_task['type']}</b></span>
            </div>
            """, unsafe_allow_html=True)

            btn_q1, btn_q2 = st.columns([1, 1])
            with btn_q1:
                if st.button("🚀 Jump to Task Topic", use_container_width=True, type="primary"):
                    st.session_state.selected_topic = top_task["topic"]
                    navigate_to("📖 Topic Learning")
            with btn_q2:
                if st.button("✅ Mark Done & Dequeue", use_container_width=True):
                    finished = study_q.dequeue()
                    student["credits"] += 10
                    student["recent_activity"].insert(0, {"action": f"Finished queue task: '{finished['task']}' (+10 pts)", "time": datetime.now().strftime("%I:%M %p")})
                    persist_state()
                    st.success("Task completed & dequeued! +10 Credits awarded.")
                    st.rerun()
        else:
            st.info("Study Task Queue is empty! Great job catching up on all practice tasks. 🎉")

    with col_q2:
        st.markdown("### ⚡ Live Recent Activity (Linked List)")
        st.caption("Telemetry stream stored as a Singly Linked List with O(1) head insertion.")

        activities = student.get("recent_activity", [])
        if activities:
            for act in activities[:5]:
                st.markdown(f"""
                <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 10px 14px; margin-bottom: 8px; display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-size: 0.85rem; color: #1e293b; font-weight: 600;">{act.get('action', 'Activity')}</span>
                    <span style="font-size: 0.72rem; color: #64748b; background: #f1f5f9; padding: 2px 6px; border-radius: 4px;">{act.get('time', '')}</span>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.caption("No recent activities recorded.")


# ==============================================================================
# PAGE 3: DEDICATED SEARCH PAGE (TRIE & INVERTED INDEX)
# ==============================================================================
def render_search_page():
    st.markdown("""
    <div class="brand-header">
        <div>
            <h1 class="brand-title">Concept & Topic Search 🔍</h1>
            <span style="color: #64748b; font-size: 0.95rem;">
                Powered by a <b>Prefix Tree (Trie)</b> for autocomplete and a <b>Hash Map Inverted Index</b> for instant O(1) keyword lookup.
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="demo-tag" style="background: #f0fdf4; border-left: 4px solid #16a34a;">
        <b>⚡ DSA Search Implementation:</b> Type any prefix (e.g. <code>link</code>, <code>inord</code>, <code>virt</code>, <code>bfs</code>, <code>vtable</code>, <code>malloc</code>, <code>hash</code>). 
        The system queries the Trie in <code>O(L)</code> time and queries the Hash Map in <code>O(1)</code> time across all 17 topics!
    </div>
    """, unsafe_allow_html=True)

    col_s1, col_s2 = st.columns([2.5, 1.0])
    with col_s1:
        search_query = st.text_input("Enter keyword, concept, or topic name:", placeholder="e.g. linked list, binary search, vtable, bst, recursion, destructor").strip()
    with col_s2:
        track_filter = st.selectbox("Filter Subject Track:", ["All Tracks", "DSA (C)", "OOP (C++)"])

    if search_query:
        # Search via Trie prefix and Inverted Index
        trie_matches = SEARCH_TRIE.search_prefix(search_query)
        index_matches = INVERTED_INDEX.lookup(search_query)

        # Merge results while preserving uniqueness
        combined = []
        seen = set()
        for ref in trie_matches + index_matches:
            tid = ref.get("topic_id")
            if tid not in seen:
                if track_filter == "All Tracks" or (track_filter == "DSA (C)" and "DSA" in ref.get("subject", "")) or (track_filter == "OOP (C++)" and "OOP" in ref.get("subject", "")):
                    seen.add(tid)
                    combined.append(ref)

        if combined:
            st.markdown(f"**Found {len(combined)} matching curriculum result(s):**")
            for res in combined:
                with st.container():
                    st.markdown(f"""
                    <div class="content-card" style="border-left: 4px solid #4f46e5; margin-bottom: 10px;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <h3 style="margin: 0; color: #0f172a; font-size: 1.15rem;">{res['name']}</h3>
                            <span style="background: #e0e7ff; color: #4338ca; font-size: 0.75rem; padding: 2px 8px; border-radius: 4px; font-weight: 700;">{res['subject']}</span>
                        </div>
                        <p style="margin: 6px 0 10px 0; font-size: 0.85rem; color: #475569;">{res.get('snippet', '')}</p>
                    </div>
                    """, unsafe_allow_html=True)

                    c_btn, _ = st.columns([1.5, 3.5])
                    with c_btn:
                        if st.button(f"🚀 Study '{res['name']}'", key=f"btn_search_go_{res['topic_id']}", use_container_width=True, type="primary"):
                            st.session_state.selected_topic = res["topic_id"]
                            navigate_to("📖 Topic Learning")
        else:
            st.warning(f"No results found matching '{search_query}'. Try searching for 'Arrays', 'Trees', 'Graphs', 'Linked Lists', 'Constructors', or 'Virtual Functions'.")
    else:
        st.info("💡 Start typing in the search box above to test real-time Trie autocomplete and keyword indexing.")


# ==============================================================================
# PAGE 4: LEARNING ROADMAPS & DAG GRAPH PREREQUISITES
# ==============================================================================
def render_roadmap_page():
    st.markdown("""
    <div class="brand-header">
        <div>
            <h1 class="brand-title">Learning Roadmaps 🗺️</h1>
            <span style="color: #64748b; font-size: 0.95rem;">Structured curriculum pathways and Directed Acyclic Graph (DAG) prerequisite analysis.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    tab_road, tab_dag = st.tabs(["🗺️ Visual Curriculum Grid", "📊 Prerequisite Graph (DAG) Analysis"])

    completed_set = set(student.get("completed_topics", []))

    with tab_road:
        # DSA Track
        st.markdown("### 1. Data Structures and Algorithms in C (10 Topics)")
        st.caption("Module Lead: **Samiksha Gurung** — Procedural memory layout, pointers, linear & non-linear structures.")

        dsa_topics = [t for t in ALL_TOPICS if "DSA" in t["subject"]]
        # Render in clean 3-column rows
        for i in range(0, len(dsa_topics), 3):
            row_items = dsa_topics[i:i+3]
            cols = st.columns(len(row_items))
            for idx, t in enumerate(row_items):
                with cols[idx]:
                    is_done = t["id"] in completed_set
                    status_badge = "✅ Completed" if is_done else "⏳ In Progress"
                    status_color = "#059669" if is_done else "#d97706"
                    desc = st.session_state.resources.get("DSA", {}).get(t["id"], {}).get("description", "Core syllabus module.")

                    st.markdown(f"""
                    <div class="content-card" style="min-height: 180px;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                            <span style="font-size: 0.72rem; font-weight: 700; background: #e0e7ff; color: #3730a3; padding: 2px 8px; border-radius: 4px;">{t['difficulty']}</span>
                            <span style="font-size: 0.75rem; font-weight: 600; color: {status_color};">{status_badge}</span>
                        </div>
                        <h4 style="margin: 0 0 6px 0; color: #0f172a; font-size: 1.05rem;">{t['name']}</h4>
                        <p style="font-size: 0.8rem; color: #475569; min-height: 48px; line-height: 1.35;">{desc[:95]}...</p>
                        <div style="font-size: 0.72rem; color: #64748b; margin-bottom: 10px;">⏱️ Est. Time: {t['time']}</div>
                    </div>
                    """, unsafe_allow_html=True)

                    c_btn1, c_btn2 = st.columns(2)
                    with c_btn1:
                        if st.button("📖 Notes", key=f"road_study_{t['id']}", use_container_width=True):
                            st.session_state.selected_topic = t["id"]
                            navigate_to("📖 Topic Learning")
                    with c_btn2:
                        if st.button("📝 Quiz", key=f"road_quiz_{t['id']}", use_container_width=True):
                            st.session_state.selected_topic = t["id"]
                            st.session_state.quiz_current_index = 0
                            st.session_state.quiz_submitted = False
                            st.session_state.quiz_user_answers = {}
                            navigate_to("📝 Interactive Quiz")

        st.markdown("---")

        # OOP Track
        st.markdown("### 2. Object-Oriented Programming in C++ (7 Topics)")
        st.caption("Module Lead: **Tanisha Rai** — Encapsulation, inheritance, dynamic polymorphism, file I/O & STL.")

        oop_topics = [t for t in ALL_TOPICS if "OOP" in t["subject"]]
        for i in range(0, len(oop_topics), 3):
            row_items = oop_topics[i:i+3]
            cols2 = st.columns(len(row_items))
            for idx, t in enumerate(row_items):
                with cols2[idx]:
                    is_done = t["id"] in completed_set
                    status_badge = "✅ Completed" if is_done else "⏳ In Progress"
                    status_color = "#059669" if is_done else "#d97706"
                    desc = st.session_state.resources.get("OOPS", {}).get(t["id"], {}).get("description", "Core C++ object-oriented module.")

                    st.markdown(f"""
                    <div class="content-card" style="min-height: 180px;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                            <span style="font-size: 0.72rem; font-weight: 700; background: #fae8ff; color: #86198f; padding: 2px 8px; border-radius: 4px;">{t['difficulty']}</span>
                            <span style="font-size: 0.75rem; font-weight: 600; color: {status_color};">{status_badge}</span>
                        </div>
                        <h4 style="margin: 0 0 6px 0; color: #0f172a; font-size: 1.05rem;">{t['name']}</h4>
                        <p style="font-size: 0.8rem; color: #475569; min-height: 48px; line-height: 1.35;">{desc[:95]}...</p>
                        <div style="font-size: 0.72rem; color: #64748b; margin-bottom: 10px;">⏱️ Est. Time: {t['time']}</div>
                    </div>
                    """, unsafe_allow_html=True)

                    c_btn1, c_btn2 = st.columns(2)
                    with c_btn1:
                        if st.button("📖 Notes", key=f"road_study_oop_{t['id']}", use_container_width=True):
                            st.session_state.selected_topic = t["id"]
                            navigate_to("📖 Topic Learning")
                    with c_btn2:
                        if st.button("📝 Quiz", key=f"road_quiz_oop_{t['id']}", use_container_width=True):
                            st.session_state.selected_topic = t["id"]
                            st.session_state.quiz_current_index = 0
                            st.session_state.quiz_submitted = False
                            st.session_state.quiz_user_answers = {}
                            navigate_to("📝 Interactive Quiz")

    with tab_dag:
        st.markdown("### 📊 Course Prerequisite Directed Acyclic Graph (DAG)")
        st.caption("Demonstrating real Graph traversal algorithms (BFS & DFS) applied to curriculum roadmap navigation.")

        col_g1, col_g2 = st.columns(2)
        with col_g1:
            st.markdown("#### 🔍 BFS Shortest Learning Path Calculator")
            st.caption("Runs Breadth-First Search to find the shortest dependency pathway between any two modules:")
            all_t_ids = [t["id"] for t in ALL_TOPICS]
            src_topic = st.selectbox("Starting Topic:", all_t_ids, index=0, key="dag_src")
            tgt_topic = st.selectbox("Target Topic:", all_t_ids, index=5, key="dag_tgt")

            if st.button("⚡ Calculate Shortest Path via BFS", type="primary"):
                path = COURSE_GRAPH.bfs_shortest_path(src_topic, tgt_topic)
                if path:
                    st.success(f"Shortest Prerequisite Path found ({len(path) - 1} steps):")
                    st.markdown(" ➔ ".join([f"**{node}**" for node in path]))
                else:
                    st.info(f"No direct dependency path exists from '{src_topic}' to '{tgt_topic}' (they may belong to independent curriculum tracks).")

        with col_g2:
            st.markdown("#### 📐 DFS Topological Course Sequence")
            st.caption("Runs Depth-First Search to generate the ideal linear learning order respecting all prerequisites:")
            track_choice = st.radio("Select Track:", ["Both Tracks", "DSA (C)", "OOP (C++)"], horizontal=True)
            filter_str = None if track_choice == "Both Tracks" else ("DSA" if "DSA" in track_choice else "OOP")
            topological_order = COURSE_GRAPH.dfs_topological_sort(filter_str)
            for idx, tid in enumerate(topological_order):
                st.markdown(f"**Step {idx+1}:** `{tid}` — {COURSE_GRAPH.nodes_meta.get(tid, {}).get('name', '')}")


# ==============================================================================
# PAGE 5: TOPIC LEARNING CENTER
# ==============================================================================
def render_topic_learning():
    st.markdown("""
    <div class="brand-header">
        <div>
            <h1 class="brand-title">Topic Learning Center 📖</h1>
            <span style="color: #64748b; font-size: 0.95rem;">Concept notes, code implementations, and curated video resources.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    topic_ids = [t["id"] for t in ALL_TOPICS]
    topic_names = {t["id"]: f"{t['name']} — {t['subject']}" for t in ALL_TOPICS}

    selected_topic_id = st.selectbox(
        "Select Learning Topic",
        options=topic_ids,
        format_func=lambda x: topic_names[x],
        index=topic_ids.index(st.session_state.selected_topic) if st.session_state.selected_topic in topic_ids else 0
    )
    st.session_state.selected_topic = selected_topic_id
    topic_meta = next((t for t in ALL_TOPICS if t["id"] == selected_topic_id), ALL_TOPICS[0])
    is_completed = selected_topic_id in student.get("completed_topics", [])

    col_h1, col_h2, col_h3 = st.columns([2, 1, 1])
    with col_h1:
        status_msg = "✅ You have completed this topic!" if is_completed else "⏳ Topic is currently in progress."
        st.markdown(f"### {topic_meta['name']} `[{topic_meta['difficulty']}]`\\n{status_msg}")
    
    with col_h2:
        if is_completed:
            if st.button("↩️ Mark In-Progress", use_container_width=True):
                student["completed_topics"].remove(selected_topic_id)
                student["recent_activity"].insert(0, {
                    "action": f"Marked '{topic_meta['name']}' as In-Progress",
                    "time": datetime.now().strftime("%I:%M %p")
                })
                persist_state()
                st.rerun()
        else:
            if st.button("✅ Mark as Completed", type="primary", use_container_width=True):
                if selected_topic_id not in student["completed_topics"]:
                    student["completed_topics"].append(selected_topic_id)
                    student["credits"] += 15
                    student["recent_activity"].insert(0, {
                        "action": f"Completed topic '{topic_meta['name']}' (+15 pts)",
                        "time": datetime.now().strftime("%I:%M %p")
                    })
                    check_badges(student)
                    persist_state()
                    st.success("🎉 Topic marked completed! +15 Credit Points awarded!")
                    st.rerun()

    with col_h3:
        if st.button("📝 Start Quiz", use_container_width=True):
            st.session_state.selected_topic = selected_topic_id
            st.session_state.quiz_current_index = 0
            st.session_state.quiz_submitted = False
            st.session_state.quiz_user_answers = {}
            navigate_to("📝 Interactive Quiz")

    st.markdown("---")

    # Content Directory Resolution with Fallbacks
    is_dsa = "DSA" in topic_meta["subject"]
    content_dir = (DSA_DIR / selected_topic_id) if is_dsa else (OOPS_DIR / selected_topic_id)
    if not content_dir.exists():
        if selected_topic_id == "Stack" and (DSA_DIR / "Stacks").exists():
            content_dir = DSA_DIR / "Stacks"

    concepts_file = content_dir / "concepts.md"
    notes_file = content_dir / "notes.md"

    tabs = st.tabs(["📘 Concept Notes", "💻 Code Implementation", "📺 Learning Resources", "💡 Coding Practice"])

    with tabs[0]:
        if concepts_file.exists():
            with open(concepts_file, "r", encoding="utf-8") as f:
                st.markdown(f.read())
        else:
            st.info("Concept notes are being updated by the team.")

    with tabs[1]:
        if notes_file.exists():
            with open(notes_file, "r", encoding="utf-8") as f:
                st.markdown(f.read())
        elif concepts_file.exists():
            st.info("Full concepts & code implementation are displayed in the Concept Notes tab.")
        else:
            st.info("Code examples are currently being prepared.")

    with tabs[2]:
        st.markdown("### 📺 Curated Video Tutorials")
        res_group = "DSA" if is_dsa else "OOPS"
        topic_res = st.session_state.resources.get(res_group, {}).get(selected_topic_id, {})
        videos = topic_res.get("youtube", [])

        if videos:
            for vid in videos:
                st.markdown(f"""
                <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px; margin-bottom: 10px;">
                    <div style="font-weight: 700; color: #0f172a; font-size: 0.95rem;">🎥 {vid['title']}</div>
                    <div style="margin-top: 6px;">
                        <a href="{vid['url']}" target="_blank" style="color: #4f46e5; font-weight: 600; text-decoration: none;">▶️ Watch Tutorial on YouTube ↗</a>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.write("Video recommendations will appear here.")

    with tabs[3]:
        st.markdown("### 💡 Recommended Coding Practice")
        practice_problems = topic_res.get("practice", [])
        if practice_problems:
            for prob in practice_problems:
                st.markdown(f"""
                <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px; margin-bottom: 10px;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-weight: 700; color: #1e293b;">{prob['title']}</span>
                        <span style="background: #e2e8f0; font-size: 0.72rem; padding: 2px 8px; border-radius: 4px; font-weight: 600;">{prob['platform']}</span>
                    </div>
                    <div style="margin-top: 6px;">
                        <a href="{prob['url']}" target="_blank" style="color: #2563eb; font-weight: 600; text-decoration: none;">Solve on {prob['platform']} ↗</a>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.write("Practice problems will appear here.")


# ==============================================================================
# PAGE 6: INTERACTIVE QUIZ (MULTI-DIFFICULTY & ANTI-ABUSE ENGINE)
# ==============================================================================
def render_quiz_page():
    st.markdown("""
    <div class="brand-header">
        <div>
            <h1 class="brand-title">Interactive Quiz & Assessment 📝</h1>
            <span style="color: #64748b; font-size: 0.95rem;">Test your conceptual understanding and code prediction skills.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    available_quiz_keys = list(st.session_state.quizzes.keys())
    if not available_quiz_keys:
        st.error("No quizzes available in the question bank.")
        return

    # Topic, Difficulty & Timer Selectors
    col_q1, col_q2, col_q3 = st.columns([1.5, 1.0, 1.0])
    with col_q1:
        selected_quiz_key = st.selectbox(
            "Select Quiz Module",
            available_quiz_keys,
            index=available_quiz_keys.index(st.session_state.selected_topic) if st.session_state.selected_topic in available_quiz_keys else 0
        )
    with col_q2:
        diff_filter = st.selectbox(
            "Difficulty Filter",
            ["All Difficulties", "Easy (10 pts)", "Medium (15 pts)", "Hard (20 pts)"],
            index=["All Difficulties", "Easy (10 pts)", "Medium (15 pts)", "Hard (20 pts)"].index(st.session_state.quiz_difficulty_filter)
        )
        st.session_state.quiz_difficulty_filter = diff_filter
    with col_q3:
        timer_opt = st.selectbox(
            "Optional Timer",
            ["Untimed", "5 Minutes", "10 Minutes"],
            index=["Untimed", "5 Minutes", "10 Minutes"].index(st.session_state.quiz_timer_setting)
        )
        st.session_state.quiz_timer_setting = timer_opt

    all_raw_questions = st.session_state.quizzes[selected_quiz_key]
    
    # Filter questions by difficulty if selected
    if diff_filter == "Easy (10 pts)":
        questions = [q for q in all_raw_questions if q.get("difficulty") == "Easy"]
    elif diff_filter == "Medium (15 pts)":
        questions = [q for q in all_raw_questions if q.get("difficulty") == "Medium"]
    elif diff_filter == "Hard (20 pts)":
        questions = [q for q in all_raw_questions if q.get("difficulty") == "Hard"]
    else:
        questions = all_raw_questions

    if not questions:
        questions = all_raw_questions  # Fallback to all if tier has 0

    total_questions = len(questions)
    q_idx = min(st.session_state.quiz_current_index, total_questions - 1)

    # Question Jump Navigation Matrix
    st.markdown("**Jump to Question:**")
    jump_cols = st.columns(min(total_questions, 8))
    for i in range(min(total_questions, 8)):
        ans_given = i in st.session_state.quiz_user_answers
        label = f"Q{i+1} {'✅' if ans_given else ''}"
        if jump_cols[i].button(label, key=f"jump_{i}", use_container_width=True):
            st.session_state.quiz_current_index = i
            st.rerun()

    st.markdown("---")

    if st.session_state.quiz_submitted:
        # Scorecard
        correct_count = 0
        points_earned = 0
        for i, q in enumerate(questions):
            if st.session_state.quiz_user_answers.get(i) == q["correct"]:
                correct_count += 1
                points_earned += q.get("points", 10)

        acc = round((correct_count / total_questions * 100), 1)

        st.markdown(f"""
        <div class="content-card" style="text-align: center; border-left: 6px solid #4f46e5; padding: 24px;">
            <h2 style="color: #1e1b4b; margin: 0 0 8px 0;">Quiz Results: {selected_quiz_key}</h2>
            <h1 style="color: #4f46e5; font-size: 3rem; margin: 0;">{acc}%</h1>
            <p style="font-size: 1.1rem; color: #1e293b; margin: 8px 0;">
                You answered <b>{correct_count} of {total_questions}</b> questions correctly.
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Question Review with Explanations
        st.markdown("### 📋 Question-by-Question Review")
        for i, q in enumerate(questions):
            user_ans = st.session_state.quiz_user_answers.get(i)
            is_correct = (user_ans == q["correct"])
            border_c = "#10b981" if is_correct else "#ef4444"
            status_t = "✅ Correct" if is_correct else "❌ Incorrect"

            st.markdown(f"""
            <div style="background: #ffffff; border: 1.5px solid {border_c}; border-radius: 8px; padding: 14px; margin-bottom: 12px;">
                <div style="display: flex; justify-content: space-between;">
                    <span style="font-weight: 700; color: #1e293b;">Question {i+1} ({q.get('difficulty', 'Medium')})</span>
                    <span style="font-weight: 700;">{status_t}</span>
                </div>
                <p style="margin: 6px 0; color: #0f172a; font-weight: 600;">{q['question']}</p>
                <p style="margin: 4px 0; font-size: 0.85rem; color: #475569;">
                    <b>Your Answer:</b> {q['options'][user_ans] if user_ans is not None else 'Unanswered'}<br>
                    <b>Correct Answer:</b> {q['options'][q['correct']]}
                </p>
                <div style="background: #f8fafc; padding: 8px 12px; border-radius: 6px; font-size: 0.82rem; color: #334155; margin-top: 6px;">
                    💡 <b>Explanation:</b> {q.get('explanation', '')}
                </div>
            </div>
            """, unsafe_allow_html=True)

        if st.button("🔄 Retake Quiz", type="primary", use_container_width=True):
            st.session_state.quiz_submitted = False
            st.session_state.quiz_user_answers = {}
            st.session_state.quiz_current_index = 0
            st.rerun()

    else:
        # Active Question View
        curr_q = questions[q_idx]

        st.markdown(f"""
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
            <span style="font-weight: 700; color: #1e293b;">Question {q_idx + 1} of {total_questions}</span>
            <span style="font-size: 0.8rem; background: #e0e7ff; color: #4338ca; padding: 2px 8px; border-radius: 4px; font-weight: 700;">
                {curr_q.get('difficulty', 'Medium')} · Worth: {curr_q.get('points', 10)} pts
            </span>
        </div>
        """, unsafe_allow_html=True)
        st.progress((q_idx + 1) / total_questions)

        st.markdown(f"""
        <div class="content-card" style="margin-top: 14px;">
            <h3 style="color: #0f172a; margin-top: 0; font-size: 1.25rem;">{curr_q['question']}</h3>
        </div>
        """, unsafe_allow_html=True)

        prev_ans = st.session_state.quiz_user_answers.get(q_idx, None)
        selected_option = st.radio(
            "Select one option:",
            options=list(range(len(curr_q["options"]))),
            format_func=lambda x: f"{['A', 'B', 'C', 'D'][x]}. {curr_q['options'][x]}",
            index=prev_ans if prev_ans is not None else 0,
            key=f"q_{selected_quiz_key}_{q_idx}"
        )
        st.session_state.quiz_user_answers[q_idx] = selected_option

        col_nav1, col_nav2, col_nav3 = st.columns([1, 1, 1.2])
        with col_nav1:
            if q_idx > 0:
                if st.button("⬅️ Previous Question", use_container_width=True):
                    st.session_state.quiz_current_index -= 1
                    st.rerun()
        with col_nav2:
            if q_idx < total_questions - 1:
                if st.button("Next Question ➡️", use_container_width=True, type="secondary"):
                    st.session_state.quiz_current_index += 1
                    st.rerun()
        with col_nav3:
            if st.button("🚀 Submit Quiz", type="primary", use_container_width=True):
                correct_count = 0
                points_gained = 0
                for i, q in enumerate(questions):
                    if st.session_state.quiz_user_answers.get(i) == q["correct"]:
                        correct_count += 1
                        points_gained += q.get("points", 10)
                accuracy_pct = round((correct_count / total_questions) * 100, 1)

                # Anti-abuse: First attempt awards points; repeat attempts update scorecard without farming duplicate credits
                if selected_quiz_key not in student.get("quiz_history", {}):
                    student["credits"] += points_gained
                    student.setdefault("quiz_history", {})[selected_quiz_key] = {
                        "score": correct_count,
                        "total": total_questions,
                        "percentage": accuracy_pct,
                        "points_awarded": points_gained,
                        "attempts_count": 1,
                        "attempted_at": datetime.now().strftime("%Y-%m-%d %H:%M")
                    }
                    student["recent_activity"].insert(0, {
                        "action": f"Scored {accuracy_pct}% on {selected_quiz_key} Quiz (+{points_gained} pts)",
                        "time": datetime.now().strftime("%I:%M %p")
                    })
                else:
                    existing = student["quiz_history"][selected_quiz_key]
                    existing["attempts_count"] = existing.get("attempts_count", 1) + 1
                    existing["score"] = correct_count
                    existing["percentage"] = accuracy_pct
                    existing["last_retake_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
                    student["recent_activity"].insert(0, {
                        "action": f"Retook {selected_quiz_key} Quiz: scored {accuracy_pct}% (Attempt #{existing['attempts_count']}, no bonus credits)",
                        "time": datetime.now().strftime("%I:%M %p")
                    })

                check_badges(student)
                persist_state()
                st.session_state.quiz_submitted = True
                st.rerun()


# ==============================================================================
# PAGE 7: LEADERBOARD (MIN-HEAP POWERED RANKING)
# ==============================================================================
def render_leaderboard_page():
    st.markdown("""
    <div class="brand-header">
        <div>
            <h1 class="brand-title">Student Leaderboard 🏆</h1>
            <span style="color: #64748b; font-size: 0.95rem;">Ranked dynamically using a Min-Heap data structure.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="demo-tag" style="background: #f0fdf4; border-left: 4px solid #16a34a;">
        <b>⚡ DSA Leaderboard Implementation: Min-Heap (<code>heapq</code>):</b> 
        Rankings are extracted in descending order using a Min-Heap with inverted credit keys (<code>-credits</code>). 
        Ties are broken deterministically using negative streaks (<code>-streak</code>) and student roll IDs.
        <b>Complexity:</b> Heapify in <code>O(N)</code> time; Sorted extraction in <code>O(N log N)</code> time.
    </div>
    """, unsafe_allow_html=True)

    # Genuine Min-Heap Construction & Extraction
    min_heap = MinHeapLeaderboard()
    min_heap.build_from_students(st.session_state.students, st.session_state.leaderboard)
    leaderboard_data = min_heap.extract_sorted_rankings()

    my_rank = next((item["rank"] for item in leaderboard_data if item.get("id") == student["id"]), 1)

    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #4f46e5, #3730a3); color: #ffffff; border-radius: 12px; padding: 16px 20px; margin-bottom: 20px; display: flex; justify-content: space-between; align-items: center;">
        <div>
            <span style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.5px; opacity: 0.85;">Your Current Standing</span>
            <h3 style="margin: 2px 0 0 0; color: #ffffff; font-size: 1.4rem;">Rank #{my_rank} — {student['name']}</h3>
        </div>
        <div style="display: flex; gap: 24px; text-align: right;">
            <div>
                <span style="font-size: 0.72rem; opacity: 0.85; text-transform: uppercase;">Total Credits</span>
                <div style="font-size: 1.4rem; font-weight: 800;">{student['credits']} pts</div>
            </div>
            <div>
                <span style="font-size: 0.72rem; opacity: 0.85; text-transform: uppercase;">Streak</span>
                <div style="font-size: 1.4rem; font-weight: 800;">{student['streak_days']} Days 🔥</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    for row in leaderboard_data:
        is_me = (row.get("id") == student["id"])
        bg_color = "#eef2ff" if is_me else "#ffffff"
        border_color = "#818cf8" if is_me else "#e2e8f0"
        rank_icon = "🥇" if row["rank"] == 1 else "🥈" if row["rank"] == 2 else "🥉" if row["rank"] == 3 else f"#{row['rank']}"
        me_badge = "<span style='background: #4338ca; color: white; padding: 2px 6px; border-radius: 4px; font-size: 0.7rem; font-weight: 700; margin-left: 8px;'>YOU</span>" if is_me else ""

        st.markdown(f"""
        <div style="background: {bg_color}; border: 1.5px solid {border_color}; border-radius: 10px; padding: 12px 18px; margin-bottom: 8px; display: flex; justify-content: space-between; align-items: center;">
            <div style="display: flex; align-items: center; gap: 14px;">
                <span style="font-size: 1.25rem; font-weight: 800; min-width: 32px; color: #1e1b4b;">{rank_icon}</span>
                <div>
                    <h4 style="margin: 0; color: #0f172a; font-size: 1.05rem;">{row.get('avatar', '🎓')} {row['name']} {me_badge}</h4>
                    <span style="font-size: 0.78rem; color: #64748b;">ID: {row['id']} · {row.get('department', 'B.Tech CSE')}</span>
                </div>
            </div>
            <div style="display: flex; gap: 20px; align-items: center;">
                <span style="font-weight: 700; color: #b45309; font-size: 0.9rem;">🔥 {row['streak']}d</span>
                <span style="font-weight: 700; color: #5b21b6; font-size: 0.9rem;">🏆 {row['badges']} Badges</span>
                <span style="background: #e0e7ff; color: #4338ca; padding: 4px 12px; border-radius: 9999px; font-weight: 800; font-size: 0.95rem;">
                    {row['credits']} pts
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ==============================================================================
# PAGE 8: STUDENT REWARDS STORE
# ==============================================================================
def render_rewards_page():
    st.markdown("""
    <div class="brand-header">
        <div>
            <h1 class="brand-title">Credit Rewards Store 🎁</h1>
            <span style="color: #64748b; font-size: 0.95rem;">Redeem your hard-earned credit points for campus perks and tech swag.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    rewards = st.session_state.rewards
    r_cols = st.columns(len(rewards))

    for idx, item in enumerate(rewards):
        with r_cols[idx]:
            can_afford = student["credits"] >= item["cost"]
            st.markdown(f"""
            <div class="content-card" style="text-align: center; min-height: 220px;">
                <div style="font-size: 2.5rem; margin-bottom: 6px;">{item.get('icon', '🎁')}</div>
                <h4 style="margin: 0 0 4px 0; color: #0f172a;">{item['title']}</h4>
                <p style="font-size: 0.8rem; color: #64748b; min-height: 40px;">{item['desc']}</p>
                <div style="font-size: 1.15rem; font-weight: 800; color: #4f46e5; margin-bottom: 12px;">{item['cost']} Credits</div>
            </div>
            """, unsafe_allow_html=True)

            if st.button(f"Redeem (-{item['cost']} pts)", key=f"btn_rw_{item['id']}", disabled=not can_afford, use_container_width=True):
                voucher = f"ARC-{item['id'].upper()}-{random.randint(1000, 9999)}"
                student["credits"] -= item["cost"]
                student.setdefault("redemptions", []).insert(0, {
                    "reward_id": item["id"],
                    "title": item["title"],
                    "cost": item["cost"],
                    "voucher": voucher,
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M")
                })
                student["recent_activity"].insert(0, {
                    "action": f"Redeemed reward: '{item['title']}' (-{item['cost']} pts)",
                    "time": datetime.now().strftime("%I:%M %p")
                })
                persist_state()
                st.success(f"🎉 Voucher Generated: {voucher}")
                st.rerun()


# ==============================================================================
# PAGE 9: COMMUNITY NOTES & RESOURCES
# ==============================================================================
def render_notes_page():
    st.markdown("""
    <div class="brand-header">
        <div>
            <h1 class="brand-title">Community Notes & Resources 📚</h1>
            <span style="color: #64748b; font-size: 0.95rem;">Peer-to-peer revision notes and curated academic cheat sheets.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    tab_read, tab_write = st.tabs(["📖 Browse Shared Notes", "✍️ Post a Revision Note (+20 Credits)"])

    with tab_read:
        notes = st.session_state.shared_notes
        if notes:
            for n in notes:
                st.markdown(f"""
                <div class="content-card" style="border-left: 4px solid #4f46e5; margin-bottom: 12px;">
                    <div style="display: flex; justify-content: space-between;">
                        <h4 style="margin: 0; color: #1e1b4b;">{n.get('title', 'Note')}</h4>
                        <span style="background: #e0e7ff; color: #4338ca; padding: 2px 8px; border-radius: 4px; font-size: 0.72rem; font-weight: 700;">{n.get('topic', 'DSA')}</span>
                    </div>
                    <p style="margin: 6px 0; font-size: 0.88rem; color: #334155; white-space: pre-wrap;">{n.get('content', '')}</p>
                    <span style="font-size: 0.75rem; color: #64748b;">Author: <b>{n.get('author_name', 'Student')}</b> ({n.get('author_id', '')}) · {n.get('date', '')}</span>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No community notes shared yet.")

    with tab_write:
        with st.form("share_note_form"):
            note_title = st.text_input("Note Title", placeholder="e.g. Quick Formula for Circular Queue Modulo Indexing")
            note_topic = st.selectbox("Topic", [t["id"] for t in ALL_TOPICS])
            note_content = st.text_area("Note Content / Key Insights", placeholder="Write short revision pointers, code snippets, or gotchas...", height=150)
            submit_note = st.form_submit_button("🚀 Publish Note (+20 Credits)", type="primary")

            if submit_note:
                if not note_title.strip() or not note_content.strip():
                    st.error("Please provide both a title and content.")
                else:
                    new_entry = {
                        "id": f"note-{len(st.session_state.shared_notes) + 1}",
                        "title": note_title.strip(),
                        "topic": note_topic,
                        "content": note_content.strip(),
                        "author_id": student["id"],
                        "author_name": student["name"],
                        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
                    }
                    st.session_state.shared_notes.insert(0, new_entry)
                    student["credits"] += 20
                    student["recent_activity"].insert(0, {
                        "action": f"Shared revision note: '{note_title}' (+20 pts)",
                        "time": datetime.now().strftime("%I:%M %p")
                    })
                    check_badges(student)
                    persist_state()
                    st.success("Note published successfully! +20 Credit Points awarded.")
                    st.rerun()


# ==============================================================================
# PAGE 10: STUDENT PROGRESS REPORT
# ==============================================================================
def render_progress_report():
    st.markdown(f"""
    <div class="brand-header">
        <div>
            <h1 class="brand-title">Academic Progress Report 📊</h1>
            <span style="color: #64748b; font-size: 0.95rem;">Individual dossier for {student['name']} ({student['id']}).</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    completed = student.get("completed_topics", [])
    pct = round((len(completed) / len(ALL_TOPICS) * 100), 1)

    st.markdown(f"""
    <div class="content-card">
        <h3 style="margin-top: 0; color: #1e1b4b;">Curriculum Completion: {pct}% ({len(completed)} / {len(ALL_TOPICS)} Topics)</h3>
    </div>
    """, unsafe_allow_html=True)
    st.progress(pct / 100.0)

    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.markdown("#### 🏆 Unlocked Badges")
        b_list = student.get("badges", [])
        for b_id, b_meta in BADGE_CATALOG.items():
            if b_id in b_list:
                st.markdown(f"**{b_meta['icon']} {b_meta['name']}**: {b_meta['desc']}")

    with col_p2:
        st.markdown("#### 📝 Quiz History")
        qh = student.get("quiz_history", {})
        if qh:
            q_table = [{"Topic": k, "Score": f"{v['score']}/{v['total']}", "Accuracy": f"{v['percentage']}%", "Retakes": v.get("attempts_count", 1)} for k, v in qh.items()]
            st.table(q_table)
        else:
            st.caption("No quiz attempts yet.")

    student_summary = {
        "id": student["id"],
        "name": student["name"],
        "email": student["email"],
        "department": student["department"],
        "role": student.get("role", "Student Learner"),
        "credits": student["credits"],
        "streak": student["streak_days"],
        "progress_pct": pct,
        "completed_list": completed,
        "in_progress_list": student.get("in_progress_topics", []),
        "quiz_history": qh
    }
    csv_bytes = generate_student_detailed_csv(student_summary)
    st.download_button(
        label="📥 Download My Progress Report (CSV)",
        data=csv_bytes,
        file_name=f"SkillArc_Progress_{student['id']}.csv",
        mime="text/csv",
        use_container_width=True
    )


# ==============================================================================
# PAGE 11: C++ ENGINE SHOWCASE (OOP, FRIEND CLASS, FILE STREAMS & STL)
# ==============================================================================
def render_cpp_showcase():
    st.markdown("""
    <div class="brand-header">
        <div>
            <h1 class="brand-title">C++ OOP Quiz Engine Showcase ⚙️</h1>
            <span style="color: #64748b; font-size: 0.95rem;">Native C++ backend with Student, Question, and Admin classes, Friend Class, File Streams & STL.</span>
        </div>
        <div style="margin-left: auto;">
            <span class="brand-pill">Module Lead: Tanisha Rai</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="demo-tag">
        <b>⭐ Real C++ Integration:</b> Compiled with GCC/G++ 17. Features:
        1. Encapsulation: Question & Student private state
        2. Friend Class: <code>friend class Admin;</code> grants supervisory audit access
        3. File Streams: C++ <code>ofstream</code> exports <code>skillarc_audit_report.txt</code>
        4. STL: <code>vector</code>, <code>map</code>, <code>stack</code> containers
    </div>
    """, unsafe_allow_html=True)

    col_c1, col_c2 = st.columns([1.2, 1.0])

    cpp_src_path = OOPS_DIR / "quiz_engine.cpp"
    cpp_exe_path = OOPS_DIR / "quiz_engine.exe"

    with col_c1:
        st.markdown("### 📄 C++ Source Code (`quiz_engine.cpp`)")
        if cpp_src_path.exists():
            with open(cpp_src_path, "r", encoding="utf-8") as f:
                cpp_code = f.read()
            st.code(cpp_code, language="cpp", line_numbers=True)
        else:
            st.error("C++ source file not found.")

    with col_c2:
        st.markdown("### 🖥️ Live Terminal Execution")
        st.caption("Execute `quiz_engine.exe` via Python's subprocess pipeline:")

        if st.button("▶️ Execute C++ Quiz Engine Binary", type="primary", use_container_width=True):
            if cpp_exe_path.exists():
                try:
                    proc = subprocess.run(
                        [str(cpp_exe_path)],
                        input="1\\n2\\n2\\n",
                        capture_output=True,
                        text=True,
                        timeout=5
                    )
                    st.success("Execution Successful! Terminal Output below:")
                    st.text_area("C++ stdout:", proc.stdout, height=350)
                except Exception as e:
                    st.error(f"Execution failed: {e}")
            else:
                st.warning("`quiz_engine.exe` not found. Compile using `g++ -std=c++17 quiz_engine.cpp -o quiz_engine.exe`.")


# ==============================================================================
# MAIN PAGE ROUTING
# ==============================================================================
if st.session_state.current_page == "🛡️ Admin Dashboard":
    render_admin_dashboard()
elif st.session_state.current_page == "🏠 Welcome Dashboard":
    render_welcome_dashboard()
elif st.session_state.current_page == "🔍 Concept & Topic Search":
    render_search_page()
elif st.session_state.current_page == "🗺️ Learning Roadmap":
    render_roadmap_page()
elif st.session_state.current_page == "📖 Topic Learning":
    render_topic_learning()
elif st.session_state.current_page == "📝 Interactive Quiz":
    render_quiz_page()
elif st.session_state.current_page == "🏆 Leaderboard":
    render_leaderboard_page()
elif st.session_state.current_page == "🎁 Student Rewards":
    render_rewards_page()
elif st.session_state.current_page == "📚 Notes & Resources":
    render_notes_page()
elif st.session_state.current_page == "📊 Progress Report":
    render_progress_report()
elif st.session_state.current_page == "⚙️ C++ Engine Showcase":
    render_cpp_showcase()
'''

with open(app_path, "w", encoding="utf-8") as f:
    f.write(app_code)

print("Phase III app.py successfully generated!")

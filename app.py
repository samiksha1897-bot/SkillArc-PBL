"""
SkillArc — Phase-II Interactive Prototype
Gamified Learning Platform for Data Structures (C) and Object-Oriented Programming (C++)
Team Apex:
- Samiksha Gurung (DSA Modules — Arrays, Stack, Queue)
- Vaibhavi Thapliyal (Streamlit Interface, Dashboard, Progress & Streaks)
- Tanisha Rai (C++ OOP Module & Quiz Logic with Student and Question Classes)
"""

import os
import json
import subprocess
from datetime import datetime
from pathlib import Path
import streamlit as st

# ==============================================================================
# Page Configuration
# ==============================================================================
st.set_page_config(
    page_title="SkillArc — Gamified Learning Platform",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Paths
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
ASSETS_DIR = BASE_DIR / "assets"
DSA_DIR = BASE_DIR / "Phase-2" / "DSA"
OOPS_DIR = BASE_DIR / "Phase-2" / "OOPS"

# Ensure directories exist
DATA_DIR.mkdir(exist_ok=True)
ASSETS_DIR.mkdir(exist_ok=True)

# ==============================================================================
# Custom CSS Styling (Navy, Indigo & Purple Palette)
# ==============================================================================
st.markdown("""
<style>
    /* Global Color Variables */
    :root {
        --navy-dark: #0f172a;
        --navy-mid: #1e293b;
        --purple-accent: #4f46e5;
        --indigo-accent: #6366f1;
        --blue-accent: #2563eb;
        --bg-slate: #f8fafc;
        --border-slate: #e2e8f0;
    }
    
    /* Wordmark & Header */
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
    
    /* Metric Cards */
    .metric-box {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 18px;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.05);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    .metric-box:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 6px -1px rgba(79, 70, 229, 0.1);
        border-color: #cbd5e1;
    }
    .metric-label {
        font-size: 0.8rem;
        font-weight: 600;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .metric-val {
        font-size: 1.7rem;
        font-weight: 800;
        color: #0f172a;
        margin: 4px 0 2px 0;
    }
    .metric-sub {
        font-size: 0.8rem;
        color: #4f46e5;
        font-weight: 600;
    }

    /* Cards */
    .content-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 16px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.03);
    }
    
    /* Badges */
    .badge-unlocked {
        background-color: #f5f3ff;
        border: 1.5px solid #8b5cf6;
        color: #4c1d95;
        border-radius: 10px;
        padding: 10px 14px;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        gap: 10px;
        font-weight: 600;
    }
    .badge-locked {
        background-color: #f8fafc;
        border: 1.5px dashed #cbd5e1;
        color: #94a3b8;
        border-radius: 10px;
        padding: 10px 14px;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        gap: 10px;
        font-weight: 500;
        filter: grayscale(100%);
    }

    /* Code Block Label */
    .code-label {
        font-size: 0.75rem;
        font-weight: 700;
        color: #475569;
        text-transform: uppercase;
        margin-bottom: 4px;
    }
    
    /* Demo Alert */
    .demo-tag {
        background: #f0fdf4;
        border: 1px solid #bbf7d0;
        color: #166534;
        border-radius: 8px;
        padding: 8px 12px;
        font-size: 0.85rem;
        margin-bottom: 16px;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# Data Helpers & Session State Initialization
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

# Load master files
STATE_FILE = DATA_DIR / "student_state.json"
QUIZ_FILE = DATA_DIR / "quizzes.json"
REWARD_FILE = DATA_DIR / "rewards.json"
NOTES_FILE = DATA_DIR / "shared_notes.json"
RESOURCES_FILE = DSA_DIR / "resources.json"

raw_state = load_json(STATE_FILE, {})
raw_quizzes = load_json(QUIZ_FILE, {})
raw_rewards = load_json(REWARD_FILE, [])
raw_notes = load_json(NOTES_FILE, [])
raw_resources = load_json(RESOURCES_FILE, {})

# Initialize Session State
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
    st.session_state.leaderboard = raw_state.get("leaderboard_sample", [])
    st.session_state.initialized = True

def get_current_student():
    student_id = st.session_state.active_student_id
    if student_id not in st.session_state.students:
        # Fallback to first student
        first_id = list(st.session_state.students.keys())[0]
        st.session_state.active_student_id = first_id
    return st.session_state.students[st.session_state.active_student_id]

def persist_state():
    full_state = {
        "active_student": st.session_state.active_student_id,
        "students": st.session_state.students,
        "leaderboard_sample": st.session_state.leaderboard
    }
    save_json(STATE_FILE, full_state)
    save_json(NOTES_FILE, st.session_state.shared_notes)

# Helper to check and award badges
def check_badges(student):
    badges = set(student.get("badges", []))
    # Badge 1: First Step (Completed at least 1 topic)
    if len(student.get("completed_topics", [])) >= 1:
        badges.add("first_step")
    # Badge 2: Streak Starter (3+ days streak)
    if student.get("streak_days", 0) >= 3:
        badges.add("streak_starter")
    # Badge 3: DSA Explorer (Completed all 3 DSA topics)
    dsa_all = {"Arrays", "Stack", "Queue"}
    if dsa_all.issubset(set(student.get("completed_topics", []))):
        badges.add("dsa_explorer")
    # Badge 4: C++ Cadet (Completed at least one OOP topic)
    oop_topics = {"Classes_Objects", "Constructors", "Inheritance", "Polymorphism"}
    if any(t in oop_topics for t in student.get("completed_topics", [])):
        badges.add("cpp_cadet")
    # Badge 5: Quiz Whiz (Scored 80% or more on any quiz)
    for q_data in student.get("quiz_history", {}).values():
        if q_data.get("percentage", 0) >= 80:
            badges.add("quiz_whiz")
            break
    student["badges"] = list(badges)

# Definition of all badges
BADGE_CATALOG = {
    "first_step": {"name": "First Step", "icon": "🥉", "desc": "Completed your first learning topic on SkillArc."},
    "streak_starter": {"name": "Streak Starter", "icon": "🔥", "desc": "Maintained an active 3+ day learning streak."},
    "quiz_whiz": {"name": "Quiz Whiz", "icon": "⚡", "desc": "Scored 80% or higher on an interactive topic quiz."},
    "dsa_explorer": {"name": "DSA Explorer", "icon": "💡", "desc": "Completed all core DSA modules: Arrays, Stack, and Queue."},
    "cpp_cadet": {"name": "C++ Cadet", "icon": "🛡️", "desc": "Completed Object-Oriented C++ programming topics."},
    "knowledge_sharer": {"name": "Knowledge Sharer", "icon": "🌟", "desc": "Shared a helpful revision note with the community."}
}

# Total curriculum list
ALL_TOPICS = [
    {"id": "Arrays", "subject": "DSA (C)", "name": "Arrays in C", "difficulty": "Easy", "time": "45 mins"},
    {"id": "Stack", "subject": "DSA (C)", "name": "Stack (LIFO)", "difficulty": "Medium", "time": "60 mins"},
    {"id": "Queue", "subject": "DSA (C)", "name": "Queue & Circular Queue", "difficulty": "Medium", "time": "60 mins"},
    {"id": "Classes_Objects", "subject": "OOP (C++)", "name": "Classes and Objects", "difficulty": "Easy", "time": "40 mins"},
    {"id": "Constructors", "subject": "OOP (C++)", "name": "Constructors & Destructors", "difficulty": "Easy", "time": "45 mins"},
    {"id": "Inheritance", "subject": "OOP (C++)", "name": "Inheritance Types", "difficulty": "Medium", "time": "50 mins"},
    {"id": "Polymorphism", "subject": "OOP (C++)", "name": "Polymorphism & Virtual Functions", "difficulty": "Medium", "time": "55 mins"},
]

# ==============================================================================
# Sidebar Navigation & Student Profile
# ==============================================================================
student = get_current_student()

with st.sidebar:
    # App Brand / Wordmark
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
        <span style="font-size: 2rem;">⚡</span>
        <div>
            <h2 style="margin: 0; font-size: 1.5rem; color: #1e1b4b; font-weight: 800; line-height: 1.1;">SkillArc</h2>
            <span style="font-size: 0.72rem; color: #6366f1; font-weight: 600; text-transform: uppercase;">Phase-II Prototype</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Active Student Selector (Switch between Team Apex members for demonstration)
    st.markdown("<p style='font-size: 0.8rem; font-weight: 600; color: #64748b; margin-bottom: 4px;'>SWITCH DEMO STUDENT</p>", unsafe_allow_html=True)
    student_options = {sid: f"{s['name']} ({s['role'].split('&')[0].strip()})" for sid, s in st.session_state.students.items()}
    chosen_student_id = st.selectbox(
        "Demonstration Profile",
        options=list(student_options.keys()),
        format_func=lambda x: student_options[x],
        index=list(student_options.keys()).index(st.session_state.active_student_id),
        label_visibility="collapsed"
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

    # Navigation Menu
    NAV_PAGES = [
        "🏠 Welcome Dashboard",
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
        st.session_state.current_page = selected_nav
        st.rerun()

    st.markdown("---")
    st.markdown("""
    <div style="font-size: 0.75rem; color: #64748b; line-height: 1.4;">
        <b>Team Apex (B.Tech CSE - 2nd Year)</b><br>
        • Samiksha Gurung (DSA)<br>
        • Vaibhavi Thapliyal (UI & Streaks)<br>
        • Tanisha Rai (C++ OOP & Engine)<br>
        <span style="color: #4f46e5; font-weight: 600;">Phase-II Evaluation Build</span>
    </div>
    """, unsafe_allow_html=True)


# ==============================================================================
# SECTION A: Welcome / Student Dashboard
# ==============================================================================
if st.session_state.current_page == "🏠 Welcome Dashboard":
    st.markdown("""
    <div class="brand-header">
        <div>
            <h1 class="brand-title">Welcome back, {}! 👋</h1>
            <span style="color: #64748b; font-size: 0.95rem;">Track your progress in C Data Structures and C++ Object-Oriented Programming.</span>
        </div>
        <div style="margin-left: auto;">
            <span class="brand-pill">Phase-II Demo Active</span>
        </div>
    </div>
    """.format(student['name']), unsafe_allow_html=True)

    # Calculation for overall progress
    total_topics_count = len(ALL_TOPICS)
    completed_topics_count = len(student.get("completed_topics", []))
    progress_percentage = int((completed_topics_count / total_topics_count) * 100) if total_topics_count > 0 else 0

    # Top Metric Highlights
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-label">Credit Points</div>
            <div class="metric-val">💎 {student['credits']}</div>
            <div class="metric-sub">Earn points via quizzes & notes</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-label">Active Streak</div>
            <div class="metric-val">🔥 {student['streak_days']} Days</div>
            <div class="metric-sub">Daily practice maintained</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-label">Overall Progress</div>
            <div class="metric-val">{progress_percentage}%</div>
            <div class="metric-sub">{completed_topics_count} of {total_topics_count} topics completed</div>
        </div>
        """, unsafe_allow_html=True)
    with c4:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-label">Earned Badges</div>
            <div class="metric-val">🏆 {len(student.get('badges', []))}</div>
            <div class="metric-sub">Milestones achieved</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)
    st.progress(progress_percentage / 100.0)

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

    col_left, col_right = st.columns([1.6, 1.0])

    with col_left:
        # Continue Learning Callout
        st.markdown("### 🚀 Continue Learning")
        
        # Find next uncompleted topic
        next_topic = None
        for t in ALL_TOPICS:
            if t["id"] not in student.get("completed_topics", []):
                next_topic = t
                break
        
        if next_topic:
            st.info(f"**Recommended Next Step:** Jump into **{next_topic['name']}** ({next_topic['subject']}) — Estimated: {next_topic['time']}.")
            if st.button(f"📖 Study {next_topic['name']} Now", type="primary", use_container_width=True):
                st.session_state.selected_topic = next_topic["id"]
                st.session_state.current_page = "📖 Topic Learning"
                st.rerun()
        else:
            st.success("🎉 Incredible job! You have completed all learning topics in this Phase-II prototype curriculum!")
            if st.button("🗺️ Explore Roadmap & Review Topics", type="primary", use_container_width=True):
                st.session_state.current_page = "🗺️ Learning Roadmap"
                st.rerun()

        st.markdown("---")

        # Topics Overview Split
        st.markdown("#### 📚 Topic Status Overview")
        completed = student.get("completed_topics", [])
        
        tabs_dsa, tabs_oop = st.tabs(["Data Structures (C)", "Object-Oriented Programming (C++)"])
        with tabs_dsa:
            for t in [x for x in ALL_TOPICS if "DSA" in x["subject"]]:
                is_done = t["id"] in completed
                icon = "✅" if is_done else "⏳"
                status_text = "Completed" if is_done else "In Progress"
                col_t1, col_t2 = st.columns([3, 1])
                with col_t1:
                    st.write(f"{icon} **{t['name']}** `[{t['difficulty']}]` — {status_text}")
                with col_t2:
                    if st.button("Open", key=f"dash_open_{t['id']}"):
                        st.session_state.selected_topic = t["id"]
                        st.session_state.current_page = "📖 Topic Learning"
                        st.rerun()

        with tabs_oop:
            for t in [x for x in ALL_TOPICS if "OOP" in x["subject"]]:
                is_done = t["id"] in completed
                icon = "✅" if is_done else "⏳"
                status_text = "Completed" if is_done else "In Progress"
                col_t1, col_t2 = st.columns([3, 1])
                with col_t1:
                    st.write(f"{icon} **{t['name']}** `[{t['difficulty']}]` — {status_text}")
                with col_t2:
                    if st.button("Open", key=f"dash_open_oop_{t['id']}"):
                        st.session_state.selected_topic = t["id"]
                        st.session_state.current_page = "📖 Topic Learning"
                        st.rerun()

    with col_right:
        # Recent Activity Feed
        st.markdown("### ⏱️ Recent Activity")
        activities = student.get("recent_activity", [])
        if activities:
            for act in activities[:5]:
                st.markdown(f"""
                <div style="background: #ffffff; border-left: 3px solid #6366f1; padding: 10px 14px; margin-bottom: 8px; border-radius: 4px; box-shadow: 0 1px 2px rgba(0,0,0,0.03);">
                    <div style="font-weight: 600; color: #1e293b; font-size: 0.88rem;">{act['action']}</div>
                    <div style="font-size: 0.75rem; color: #94a3b8; margin-top: 2px;">{act['time']}</div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.write("No recent activities yet.")

        # Quick Achievements Preview
        st.markdown("### 🏆 Badges Earned")
        unlocked = student.get("badges", [])
        for b_key, b_info in BADGE_CATALOG.items():
            if b_key in unlocked:
                st.markdown(f"""
                <div class="badge-unlocked">
                    <span style="font-size: 1.3rem;">{b_info['icon']}</span>
                    <div>
                        <div style="font-size: 0.85rem; font-weight: 700;">{b_info['name']}</div>
                        <div style="font-size: 0.72rem; color: #6d28d9;">{b_info['desc']}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)


# ==============================================================================
# SECTION B: Learning Roadmap
# ==============================================================================
elif st.session_state.current_page == "🗺️ Learning Roadmap":
    st.markdown("""
    <div class="brand-header">
        <div>
            <h1 class="brand-title">Learning Roadmaps 🗺️</h1>
            <span style="color: #64748b; font-size: 0.95rem;">Structured step-by-step pathways for second-year CSE students.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    completed_set = set(student.get("completed_topics", []))

    # Subject 1: DSA in C
    st.markdown("## 1. Data Structures and Algorithms (C)")
    st.caption("Module Lead: **Samiksha Gurung** — Master core memory layouts, pointers, and linear abstract data types.")

    dsa_topics = [t for t in ALL_TOPICS if "DSA" in t["subject"]]
    cols = st.columns(len(dsa_topics))

    for idx, t in enumerate(dsa_topics):
        with cols[idx]:
            is_done = t["id"] in completed_set
            status_badge = "✅ Completed" if is_done else "⏳ In Progress"
            status_color = "#059669" if is_done else "#d97706"
            
            # Retrieve description from resources if available
            dsa_info = st.session_state.resources.get("DSA", {}).get(t["id"], {})
            desc = dsa_info.get("description", "Fundamental data structure essential for memory layout.")
            
            st.markdown(f"""
            <div class="content-card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <span style="font-size: 0.72rem; font-weight: 700; background: #e0e7ff; color: #3730a3; padding: 2px 8px; border-radius: 4px;">{t['difficulty']}</span>
                    <span style="font-size: 0.78rem; font-weight: 600; color: {status_color};">{status_badge}</span>
                </div>
                <h3 style="margin: 0 0 8px 0; color: #0f172a; font-size: 1.15rem;">{t['name']}</h3>
                <p style="font-size: 0.82rem; color: #475569; min-height: 48px; line-height: 1.35;">{desc[:110]}...</p>
                <div style="font-size: 0.75rem; color: #64748b; margin-bottom: 12px;">⏱️ Est. Time: {t['time']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            c_btn1, c_btn2 = st.columns(2)
            with c_btn1:
                if st.button("📖 Notes", key=f"road_study_{t['id']}", use_container_width=True):
                    st.session_state.selected_topic = t["id"]
                    st.session_state.current_page = "📖 Topic Learning"
                    st.rerun()
            with c_btn2:
                if st.button("📝 Quiz", key=f"road_quiz_{t['id']}", use_container_width=True):
                    st.session_state.selected_topic = t["id"]
                    st.session_state.current_page = "📝 Interactive Quiz"
                    st.session_state.quiz_current_index = 0
                    st.session_state.quiz_submitted = False
                    st.session_state.quiz_user_answers = {}
                    st.rerun()

    st.markdown("---")

    # Subject 2: OOP in C++
    st.markdown("## 2. Object-Oriented Programming (C++)")
    st.caption("Module Lead: **Tanisha Rai** — Understand class blueprints, member functions, inheritance, and dynamic polymorphism.")

    oop_topics = [t for t in ALL_TOPICS if "OOP" in t["subject"]]
    cols2 = st.columns(len(oop_topics))

    for idx, t in enumerate(oop_topics):
        with cols2[idx]:
            is_done = t["id"] in completed_set
            status_badge = "✅ Completed" if is_done else "⏳ In Progress"
            status_color = "#059669" if is_done else "#d97706"
            
            oop_info = st.session_state.resources.get("OOPS", {}).get(t["id"], {})
            desc = oop_info.get("description", "Core C++ object-oriented paradigm.")

            st.markdown(f"""
            <div class="content-card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <span style="font-size: 0.72rem; font-weight: 700; background: #fae8ff; color: #86198f; padding: 2px 8px; border-radius: 4px;">{t['difficulty']}</span>
                    <span style="font-size: 0.78rem; font-weight: 600; color: {status_color};">{status_badge}</span>
                </div>
                <h3 style="margin: 0 0 8px 0; color: #0f172a; font-size: 1.05rem;">{t['name']}</h3>
                <p style="font-size: 0.8rem; color: #475569; min-height: 48px; line-height: 1.35;">{desc[:95]}...</p>
                <div style="font-size: 0.75rem; color: #64748b; margin-bottom: 12px;">⏱️ Est. Time: {t['time']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            c_btn1, c_btn2 = st.columns(2)
            with c_btn1:
                if st.button("📖 Notes", key=f"road_study_oop_{t['id']}", use_container_width=True):
                    st.session_state.selected_topic = t["id"]
                    st.session_state.current_page = "📖 Topic Learning"
                    st.rerun()
            with c_btn2:
                # Quizzes available for Classes_Objects and Inheritance
                quiz_key = "Classes_Objects" if "Classes" in t["id"] or "Constructor" in t["id"] else "Inheritance_Polymorphism"
                if st.button("📝 Quiz", key=f"road_quiz_oop_{t['id']}", use_container_width=True):
                    st.session_state.selected_topic = quiz_key
                    st.session_state.current_page = "📝 Interactive Quiz"
                    st.session_state.quiz_current_index = 0
                    st.session_state.quiz_submitted = False
                    st.session_state.quiz_user_answers = {}
                    st.rerun()


# ==============================================================================
# SECTION C: Topic Learning Page
# ==============================================================================
elif st.session_state.current_page == "📖 Topic Learning":
    st.markdown("""
    <div class="brand-header">
        <div>
            <h1 class="brand-title">Topic Learning Center 📖</h1>
            <span style="color: #64748b; font-size: 0.95rem;">Concept notes, code implementations, and curated video resources.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Topic Selector dropdown
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

    # Header Action Bar (Mark Complete + Start Quiz buttons)
    col_h1, col_h2, col_h3 = st.columns([2, 1, 1])
    with col_h1:
        status_msg = "✅ You have completed this topic!" if is_completed else "⏳ Topic is currently in progress."
        st.markdown(f"### {topic_meta['name']} `[{topic_meta['difficulty']}]`\n{status_msg}")
    
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
                    student["credits"] += 15  # 15 points completion bonus
                    student["recent_activity"].insert(0, {
                        "action": f"Completed topic '{topic_meta['name']}' (+15 pts)",
                        "time": datetime.now().strftime("%I:%M %p")
                    })
                    check_badges(student)
                    persist_state()
                    st.success("🎉 Topic marked completed! +15 Credit Points awarded!")
                    st.rerun()

    with col_h3:
        quiz_target = selected_topic_id
        if selected_topic_id in ["Constructors"]:
            quiz_target = "Classes_Objects"
        elif selected_topic_id in ["Inheritance", "Polymorphism"]:
            quiz_target = "Inheritance_Polymorphism"

        if st.button("📝 Start Quiz", use_container_width=True):
            st.session_state.selected_topic = quiz_target
            st.session_state.current_page = "📝 Interactive Quiz"
            st.session_state.quiz_current_index = 0
            st.session_state.quiz_submitted = False
            st.session_state.quiz_user_answers = {}
            st.rerun()

    st.markdown("---")

    # Load content from Markdown files
    is_dsa = "DSA" in topic_meta["subject"]
    content_dir = (DSA_DIR / selected_topic_id) if is_dsa else (OOPS_DIR / selected_topic_id)
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
# SECTION D: Interactive Quiz
# ==============================================================================
elif st.session_state.current_page == "📝 Interactive Quiz":
    st.markdown("""
    <div class="brand-header">
        <div>
            <h1 class="brand-title">Interactive Skill Quiz 📝</h1>
            <span style="color: #64748b; font-size: 0.95rem;">Test your conceptual understanding and earn Credit Points!</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    available_quiz_keys = list(st.session_state.quizzes.keys())
    
    # Quiz Topic selector
    selected_quiz_key = st.selectbox(
        "Choose Quiz Topic",
        options=available_quiz_keys,
        index=available_quiz_keys.index(st.session_state.selected_topic) if st.session_state.selected_topic in available_quiz_keys else 0
    )

    if selected_quiz_key != st.session_state.selected_topic:
        st.session_state.selected_topic = selected_quiz_key
        st.session_state.quiz_current_index = 0
        st.session_state.quiz_user_answers = {}
        st.session_state.quiz_submitted = False
        st.rerun()

    questions = st.session_state.quizzes.get(selected_quiz_key, [])

    if not questions:
        st.warning(f"No questions currently available for {selected_quiz_key}.")
    else:
        total_questions = len(questions)
        q_idx = st.session_state.quiz_current_index

        # Check if already submitted
        if st.session_state.quiz_submitted:
            st.markdown("### 🏆 Quiz Results & Scorecard")
            
            # Score Calculation
            correct_count = 0
            points_gained = 0
            
            for i, q in enumerate(questions):
                user_choice = st.session_state.quiz_user_answers.get(i)
                if user_choice == q["correct"]:
                    correct_count += 1
                    points_gained += q.get("points", 10)
            
            accuracy_pct = round((correct_count / total_questions) * 100, 1)

            # Prevent Repeated Abuse: Check if this quiz was already taken
            existing_record = student.get("quiz_history", {}).get(selected_quiz_key)
            first_time_taking = existing_record is None
            
            # Display Score Box
            sc1, sc2, sc3 = st.columns(3)
            with sc1:
                st.metric("Total Score", f"{correct_count} / {total_questions}")
            with sc2:
                st.metric("Accuracy", f"{accuracy_pct}%")
            with sc3:
                st.metric("Credits Earned", f"+{points_gained} pts" if first_time_taking else "0 pts (Already Claimed)")

            if not first_time_taking:
                st.info("ℹ️ Note: Credit Points are awarded once per topic to prevent repeated submissions. Your initial score remains in your profile.")

            # Detailed Question-by-Question Review
            st.markdown("#### Detailed Breakdown & Explanations")
            for i, q in enumerate(questions):
                user_choice = st.session_state.quiz_user_answers.get(i)
                is_correct = (user_choice == q["correct"])
                
                with st.expander(f"Question {i+1}: {q['question']}", expanded=True):
                    if is_correct:
                        st.success(f"**Your Answer:** {q['options'][user_choice]} ✅ (Correct!)")
                    else:
                        chosen_text = q['options'][user_choice] if user_choice is not None else "No answer selected"
                        st.error(f"**Your Answer:** {chosen_text} ❌")
                        st.info(f"**Correct Answer:** {q['options'][q['correct']]}")
                    
                    st.markdown(f"**Explanation:** {q.get('explanation', 'Review concept notes for details.')}")

            col_btn1, col_btn2 = st.columns(2)
            with col_btn1:
                if st.button("🔄 Retake Quiz", use_container_width=True):
                    st.session_state.quiz_submitted = False
                    st.session_state.quiz_user_answers = {}
                    st.session_state.quiz_current_index = 0
                    st.rerun()
            with col_btn2:
                if st.button("🏠 Return to Dashboard", type="primary", use_container_width=True):
                    st.session_state.current_page = "🏠 Welcome Dashboard"
                    st.rerun()

        else:
            # Active Quiz View
            current_q = questions[q_idx]

            # Progress Indicator
            st.markdown(f"""
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                <span style="font-weight: 700; color: #1e293b;">Question {q_idx + 1} of {total_questions}</span>
                <span style="font-size: 0.8rem; color: #6366f1; font-weight: 600;">Worth: {current_q.get('points', 10)} Credit Points</span>
            </div>
            """, unsafe_allow_html=True)
            st.progress((q_idx + 1) / total_questions)

            # Question Card
            st.markdown(f"""
            <div class="content-card" style="margin-top: 14px;">
                <h3 style="color: #0f172a; margin-top: 0; font-size: 1.25rem;">{current_q['question']}</h3>
            </div>
            """, unsafe_allow_html=True)

            # Answer Options (Radio button with pre-selected previous answer if any)
            previous_ans = st.session_state.quiz_user_answers.get(q_idx, None)
            
            selected_option = st.radio(
                "Select one option:",
                options=list(range(len(current_q["options"]))),
                format_func=lambda x: f"{['A', 'B', 'C', 'D'][x]}. {current_q['options'][x]}",
                index=previous_ans if previous_ans is not None else 0,
                key=f"q_{selected_quiz_key}_{q_idx}"
            )
            # Store student answer in state
            st.session_state.quiz_user_answers[q_idx] = selected_option

            st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

            # Navigation Buttons: Previous, Next, Submit
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
                # Submit button (enabled on all questions once answered or at end)
                if st.button("🚀 Submit Quiz", type="primary", use_container_width=True):
                    # Calculate results and update points
                    correct_count = 0
                    points_gained = 0
                    for i, q in enumerate(questions):
                        if st.session_state.quiz_user_answers.get(i) == q["correct"]:
                            correct_count += 1
                            points_gained += q.get("points", 10)
                    
                    accuracy_pct = round((correct_count / total_questions) * 100, 1)

                    # Check anti-abuse rule
                    if selected_quiz_key not in student.get("quiz_history", {}):
                        student["credits"] += points_gained
                        student.setdefault("quiz_history", {})[selected_quiz_key] = {
                            "score": correct_count,
                            "total": total_questions,
                            "percentage": accuracy_pct,
                            "points_awarded": points_gained,
                            "attempted_at": datetime.now().strftime("%Y-%m-%d %H:%M")
                        }
                        student["recent_activity"].insert(0, {
                            "action": f"Scored {accuracy_pct}% on {selected_quiz_key} Quiz (+{points_gained} pts)",
                            "time": datetime.now().strftime("%I:%M %p")
                        })
                    
                    check_badges(student)
                    persist_state()
                    st.session_state.quiz_submitted = True
                    st.rerun()


# ==============================================================================
# SECTION E: Gamification & Achievements
# ==============================================================================
# Badges and Points are visible on Dashboard, Leaderboard, and here
elif st.session_state.current_page == "🏆 Leaderboard":
    st.markdown("""
    <div class="brand-header">
        <div>
            <h1 class="brand-title">Student Leaderboard 🏆</h1>
            <span style="color: #64748b; font-size: 0.95rem;">Celebrate learning consistency, credit points, and active streaks.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="demo-tag">
        <b>💡 Live Demonstration Leaderboard:</b> Rankings reflect demo student credit balances and automatically update as you complete quizzes and modules!
    </div>
    """, unsafe_allow_html=True)

    # Compile current live rankings with active student
    leaderboard_data = list(st.session_state.leaderboard)
    
    # Update active student's live points in the leaderboard
    updated = False
    for item in leaderboard_data:
        if item.get("id") == student["id"]:
            item["credits"] = student["credits"]
            item["streak"] = student["streak_days"]
            item["badges"] = len(student.get("badges", []))
            item["name"] = student["name"]
            updated = True
            break
    if not updated:
        leaderboard_data.append({
            "name": student["name"],
            "id": student["id"],
            "credits": student["credits"],
            "streak": student["streak_days"],
            "badges": len(student.get("badges", [])),
            "is_team": True
        })

    # Sort descending by credits
    leaderboard_data = sorted(leaderboard_data, key=lambda x: x["credits"], reverse=True)
    for idx, item in enumerate(leaderboard_data):
        item["rank"] = idx + 1

    # Find logged in student rank
    my_rank = next((item["rank"] for item in leaderboard_data if item.get("id") == student["id"]), 1)

    # Highlight box for logged-in user
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #4f46e5, #3730a3); color: #ffffff; border-radius: 12px; padding: 16px 20px; margin-bottom: 20px; display: flex; justify-content: space-between; align-items: center;">
        <div>
            <span style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.5px; opacity: 0.85;">Your Current Standings</span>
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

    # Leaderboard Table
    for row in leaderboard_data:
        is_me = (row.get("id") == student["id"])
        bg_color = "#eef2ff" if is_me else "#ffffff"
        border_color = "#818cf8" if is_me else "#e2e8f0"
        rank_icon = "🥇" if row["rank"] == 1 else "🥈" if row["rank"] == 2 else "🥉" if row["rank"] == 3 else f"#{row['rank']}"
        me_badge = "<span style='background: #4338ca; color: white; padding: 2px 6px; border-radius: 4px; font-size: 0.7rem; font-weight: 700; margin-left: 8px;'>YOU</span>" if is_me else ""

        st.markdown(f"""
        <div style="background: {bg_color}; border: 1.5px solid {border_color}; border-radius: 10px; padding: 12px 18px; margin-bottom: 8px; display: flex; justify-content: space-between; align-items: center;">
            <div style="display: flex; align-items: center; gap: 14px;">
                <span style="font-size: 1.3rem; font-weight: 800; min-width: 32px;">{rank_icon}</span>
                <div>
                    <span style="font-weight: 700; color: #0f172a; font-size: 1.02rem;">{row['name']}</span>{me_badge}
                    <div style="font-size: 0.75rem; color: #64748b;">Roll ID: {row.get('id', 'N/A')}</div>
                </div>
            </div>
            <div style="display: flex; gap: 28px; align-items: center;">
                <div style="text-align: center;">
                    <div style="font-size: 0.72rem; color: #64748b;">Streak</div>
                    <div style="font-weight: 700; color: #0f172a;">{row['streak']} 🔥</div>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 0.72rem; color: #64748b;">Badges</div>
                    <div style="font-weight: 700; color: #0f172a;">{row['badges']} 🏆</div>
                </div>
                <div style="text-align: right; min-width: 90px;">
                    <div style="font-size: 0.72rem; color: #4f46e5; font-weight: 700;">CREDITS</div>
                    <div style="font-size: 1.25rem; font-weight: 800; color: #1e1b4b;">{row['credits']} pts</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ==============================================================================
# SECTION F: Student Rewards Store
# ==============================================================================
elif st.session_state.current_page == "🎁 Student Rewards":
    st.markdown("""
    <div class="brand-header">
        <div>
            <h1 class="brand-title">Campus Rewards & Incentives 🎁</h1>
            <span style="color: #64748b; font-size: 0.95rem;">Exchange your hard-earned Credit Points for student perks.</span>
        </div>
        <div style="margin-left: auto;">
            <span style="font-size: 1.1rem; font-weight: 800; color: #4338ca; background: #e0e7ff; padding: 6px 14px; border-radius: 8px;">
                Wallet: {0} pts
            </span>
        </div>
    </div>
    """.format(student['credits']), unsafe_allow_html=True)

    st.markdown("""
    <div class="demo-tag">
        <b>ℹ️ Phase-II Demonstration Notice:</b> Points are deducted from your active student wallet upon redemption. Voucher codes are generated for demonstration purposes.
    </div>
    """, unsafe_allow_html=True)

    # Grid of rewards
    rewards = st.session_state.rewards
    cols = st.columns(3)

    for i, rw in enumerate(rewards):
        with cols[i % 3]:
            can_afford = student["credits"] >= rw["cost"]
            afford_tag = "✅ Affordable" if can_afford else f"🔒 Needs {rw['cost'] - student['credits']} more pts"
            afford_color = "#059669" if can_afford else "#94a3b8"

            st.markdown(f"""
            <div class="content-card" style="height: 270px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="font-size: 1.6rem;">{rw['icon']}</span>
                        <span style="font-size: 0.75rem; font-weight: 700; color: {afford_color};">{afford_tag}</span>
                    </div>
                    <h4 style="margin: 4px 0 6px 0; color: #0f172a; font-size: 1.05rem;">{rw['title']}</h4>
                    <p style="font-size: 0.8rem; color: #475569; line-height: 1.35; margin-bottom: 8px;">{rw['description']}</p>
                </div>
                <div>
                    <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
                        <span style="font-size: 0.72rem; color: #64748b; font-weight: 600;">{rw['category']}</span>
                        <span style="font-size: 1.2rem; font-weight: 800; color: #4f46e5;">{rw['cost']} pts</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            if can_afford:
                if st.button(f"Redeem for {rw['cost']} pts", key=f"rw_btn_{rw['id']}", type="primary", use_container_width=True):
                    # Deduct points
                    student["credits"] -= rw["cost"]
                    voucher_code = f"ARC-{rw['id'].upper()}-{datetime.now().strftime('%M%S')}"
                    
                    student.setdefault("redemptions", []).insert(0, {
                        "reward_id": rw["id"],
                        "title": rw["title"],
                        "cost": rw["cost"],
                        "voucher": voucher_code,
                        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
                    })
                    student["recent_activity"].insert(0, {
                        "action": f"Redeemed '{rw['title']}' (-{rw['cost']} pts)",
                        "time": datetime.now().strftime("%I:%M %p")
                    })
                    persist_state()
                    st.success(f"🎉 Voucher Redeemed! Code: `{voucher_code}`")
                    st.rerun()
            else:
                st.button(f"Requires {rw['cost']} pts", key=f"rw_btn_dis_{rw['id']}", disabled=True, use_container_width=True)

    # Redemption History
    st.markdown("---")
    st.markdown("### 📜 Your Redemption History")
    history = student.get("redemptions", [])
    if history:
        for item in history:
            voucher = item.get("voucher", "ARC-DEMO-SAMPLE")
            st.markdown(f"""
            <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px 16px; margin-bottom: 8px; display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <b>{item['title']}</b>
                    <div style="font-size: 0.75rem; color: #64748b;">Redeemed on: {item['date']} | Voucher: <code>{voucher}</code></div>
                </div>
                <div style="font-weight: 700; color: #b91c1c;">-{item['cost']} pts</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.write("You haven't redeemed any rewards yet. Complete quizzes to earn more points!")


# ==============================================================================
# SECTION G: Notes & Resources
# ==============================================================================
elif st.session_state.current_page == "📚 Notes & Resources":
    st.markdown("""
    <div class="brand-header">
        <div>
            <h1 class="brand-title">Community Notes & Resources 📚</h1>
            <span style="color: #64748b; font-size: 0.95rem;">Peer-to-peer knowledge sharing and curated revision summaries.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    tab_browse, tab_share = st.tabs(["📖 Browse Community Notes", "✍️ Share a Personal Note"])

    with tab_browse:
        notes_list = st.session_state.shared_notes
        
        # Filter by topic
        all_topics_keys = ["All Topics"] + [t["id"] for t in ALL_TOPICS]
        filter_topic = st.selectbox("Filter Notes by Topic", all_topics_keys)

        filtered = [n for n in notes_list if filter_topic == "All Topics" or n["topic"] == filter_topic]

        st.markdown(f"Displaying **{len(filtered)}** shared notes:")
        for n in filtered:
            is_sample = n.get("is_sample", False)
            author_tag = f"Sample Student • {n.get('student_id', '')}" if is_sample else f"Student Contributor • {n.get('student_id', '')}"
            badge_color = "#f1f5f9" if is_sample else "#ede9fe"
            badge_text = "Verified Note" if is_sample else "Student Post"

            st.markdown(f"""
            <div class="content-card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <span style="font-size: 0.75rem; font-weight: 700; background: {badge_color}; color: #334155; padding: 2px 8px; border-radius: 4px;">{n['topic']} • {badge_text}</span>
                    <span style="font-size: 0.75rem; color: #94a3b8;">{n['timestamp']}</span>
                </div>
                <h4 style="margin: 4px 0 8px 0; color: #0f172a;">{n['title']}</h4>
                <p style="font-size: 0.88rem; color: #334155; line-height: 1.5; white-space: pre-line;">{n['content']}</p>
                <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #f1f5f9; padding-top: 8px; margin-top: 8px;">
                    <span style="font-size: 0.78rem; color: #64748b; font-weight: 600;">By {n['author']} ({author_tag})</span>
                    <span style="font-size: 0.78rem; color: #6366f1; font-weight: 600;">❤️ {n.get('likes', 0)} likes</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with tab_share:
        st.markdown("### ✍️ Contribute a Study Note")
        st.info("💡 Sharing your peer learning notes helps fellow students and earns you **+10 Credit Points**!")

        with st.form("share_note_form"):
            note_topic = st.selectbox("Topic", [t["id"] for t in ALL_TOPICS])
            note_title = st.text_input("Note Headline / Trick", placeholder="e.g. Easy way to remember Stack Underflow")
            note_content = st.text_area("Your Notes or Code Snippet", placeholder="Write your explanation or revision trick in plain words or code...")
            submitted = st.form_submit_button("🚀 Publish Note to Community", type="primary")

            if submitted:
                if not note_title.strip() or not note_content.strip():
                    st.error("Please provide both a headline and content for your note.")
                else:
                    new_note = {
                        "id": f"note-{len(st.session_state.shared_notes) + 1}",
                        "topic": note_topic,
                        "author": student["name"],
                        "student_id": student["id"],
                        "title": note_title.strip(),
                        "content": note_content.strip(),
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
                        "likes": 1,
                        "is_sample": False
                    }
                    st.session_state.shared_notes.insert(0, new_note)
                    # Award 10 points
                    student["credits"] += 10
                    student["recent_activity"].insert(0, {
                        "action": f"Shared note on '{note_topic}' (+10 pts)",
                        "time": datetime.now().strftime("%I:%M %p")
                    })
                    # Unlock Knowledge Sharer badge
                    if "knowledge_sharer" not in student.get("badges", []):
                        student.setdefault("badges", []).append("knowledge_sharer")

                    persist_state()
                    st.success("🎉 Note published successfully! +10 Credit Points added to your wallet!")
                    st.rerun()


# ==============================================================================
# SECTION H: Progress Report
# ==============================================================================
elif st.session_state.current_page == "📊 Progress Report":
    st.markdown("""
    <div class="brand-header">
        <div>
            <h1 class="brand-title">Academic Progress & Analytics 📊</h1>
            <span style="color: #64748b; font-size: 0.95rem;">Detailed breakdown of your learning milestones and performance.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    completed_list = student.get("completed_topics", [])
    total_count = len(ALL_TOPICS)
    progress_pct = round((len(completed_list) / total_count) * 100, 1)

    # High level statistics cards
    r1, r2, r3, r4 = st.columns(4)
    with r1:
        st.metric("Total Credits", f"{student['credits']} pts")
    with r2:
        st.metric("Curriculum Done", f"{progress_pct}%")
    with r3:
        st.metric("Topics Finished", f"{len(completed_list)} of {total_count}")
    with r4:
        st.metric("Learning Streak", f"{student['streak_days']} Days 🔥")

    st.markdown("---")

    col_rep1, col_rep2 = st.columns([1.2, 1.0])

    with col_rep1:
        st.markdown("### 📝 Topic-by-Topic Completion Matrix")
        for t in ALL_TOPICS:
            is_done = t["id"] in completed_list
            status_text = "Completed ✅" if is_done else "In Progress ⏳"
            bar_val = 1.0 if is_done else 0.25
            
            st.write(f"**{t['name']}** ({t['subject']}) — `{status_text}`")
            st.progress(bar_val)

        st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
        st.markdown("### 🎯 Quiz History Log")
        quiz_hist = student.get("quiz_history", {})
        if quiz_hist:
            for q_topic, q_data in quiz_hist.items():
                st.markdown(f"""
                <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 10px 14px; margin-bottom: 8px;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <b>{q_topic} Quiz</b>
                        <span style="color: #4f46e5; font-weight: 700;">Score: {q_data['score']}/{q_data['total']} ({q_data['percentage']}%)</span>
                    </div>
                    <div style="font-size: 0.75rem; color: #64748b; margin-top: 4px;">
                        Date: {q_data.get('attempted_at', 'Recent')} | Earned: +{q_data.get('points_awarded', 0)} pts
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No quizzes logged yet. Take your first quiz from the Interactive Quiz section!")

    with col_rep2:
        st.markdown("### 🏆 Badges Earned")
        earned_badges = student.get("badges", [])
        for b_key, b_info in BADGE_CATALOG.items():
            if b_key in earned_badges:
                st.markdown(f"""
                <div class="badge-unlocked">
                    <span style="font-size: 1.4rem;">{b_info['icon']}</span>
                    <div>
                        <div style="font-size: 0.9rem; font-weight: 700;">{b_info['name']}</div>
                        <div style="font-size: 0.75rem; color: #5b21b6;">{b_info['desc']}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="badge-locked">
                    <span style="font-size: 1.4rem;">🔒</span>
                    <div>
                        <div style="font-size: 0.9rem; font-weight: 600;">{b_info['name']}</div>
                        <div style="font-size: 0.75rem; color: #94a3b8;">{b_info['desc']}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)


# ==============================================================================
# SECTION I: C++ OOP Engine Showcase (Tanisha's Deliverable)
# ==============================================================================
elif st.session_state.current_page == "⚙️ C++ Engine Showcase":
    st.markdown("""
    <div class="brand-header">
        <div>
            <h1 class="brand-title">C++ OOP Quiz Engine Showcase ⚙️</h1>
            <span style="color: #64748b; font-size: 0.95rem;">Demonstrates backend C++ Student & Question classes compiled with GCC/G++.</span>
        </div>
        <div style="margin-left: auto;">
            <span class="brand-pill">Module Lead: Tanisha Rai</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="demo-tag">
        <b>⭐ Real C++ Integration:</b> As specified in the Phase-II PBL report, the backend quiz logic was designed using native C++ Object-Oriented Programming (Classes, Encapsulation, Constructors). Below, you can inspect the C++ source code and run the compiled binary directly!
    </div>
    """, unsafe_allow_html=True)

    col_cpp1, col_cpp2 = st.columns([1.2, 1.0])

    cpp_src_path = OOPS_DIR / "quiz_engine.cpp"
    cpp_exe_path = OOPS_DIR / "quiz_engine.exe"

    with col_cpp1:
        st.markdown("### 📄 C++ Source Code (`quiz_engine.cpp`)")
        if cpp_src_path.exists():
            with open(cpp_src_path, "r", encoding="utf-8") as f:
                cpp_code = f.read()
            st.code(cpp_code, language="cpp", line_numbers=True)
        else:
            st.error("C++ source file not found.")

    with col_cpp2:
        st.markdown("### 🖥️ Live Terminal Execution")
        st.caption("Execute `quiz_engine.exe` through Python's subprocess pipeline:")

        if st.button("▶️ Execute C++ Quiz Engine Binary", type="primary", use_container_width=True):
            if cpp_exe_path.exists():
                try:
                    # Run binary and provide demonstration answers 1, 2, 2
                    proc = subprocess.run(
                        [str(cpp_exe_path)],
                        input="1\n2\n2\n",
                        capture_output=True,
                        text=True,
                        timeout=5
                    )
                    st.success("Execution Successful! Terminal Output below:")
                    st.text_area("C++ stdout:", proc.stdout, height=350)
                except Exception as e:
                    st.error(f"Execution failed: {e}")
            else:
                st.warning("`quiz_engine.exe` binary not found. Compile using `g++ -std=c++17 quiz_engine.cpp -o quiz_engine.exe`.")

        st.markdown("---")
        st.markdown("### 🏗️ Architecture & OOP Features Explained")
        st.markdown("""
        1. **`Class Question`**:
           - **Private Attributes:** `id`, `topic`, `prompt`, `options`, `correctIndex`, `points`, `explanation`.
           - **Encapsulation:** Protects internal question state from outside modification.
           - **Member Methods:** `display()`, `validateAnswer()`, `getPoints()`.

        2. **`Class Student`**:
           - **Private Attributes:** `studentId`, `fullName`, `creditPoints`, `currentStreak`.
           - **Encapsulation:** Credit points can only be updated via validated member methods like `addCredits()`.
           - **Constructors:** Parameterized constructor initializes default credits and streak days.
        """)

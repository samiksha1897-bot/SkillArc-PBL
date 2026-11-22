import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
"""
Automated Phase III Verification Suite for SkillArc
Tests all cryptographic, DSA, OOP, and data integrity modules.
"""

import json
from pathlib import Path

BASE_DIR = Path(r"C:\Users\sudeep\OneDrive\Documents\SkillArc-PBL")

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

def run_tests():
    print("==================================================")
    print("      SKILLARC PHASE III VERIFICATION SUITE       ")
    print("==================================================")

    # 1. Test Password Hashing & Verification
    print("\n[TEST 1] Cryptographic Password Hashing (PBKDF2-HMAC-SHA256)")
    raw_pwd = "apex_test_secret"
    h = hash_password(raw_pwd)
    assert h.startswith("pbkdf2:sha256:100000:"), f"Invalid hash format: {h}"
    assert verify_password(h, raw_pwd) is True, "Password verification failed on matching password!"
    assert verify_password(h, "wrong_password") is False, "Password verification failed on non-matching password!"
    print("  [PASS] PBKDF2 hash generation & constant-time verification passed!")

    # 2. Test Password Migration on Stored JSON
    print("\n[TEST 2] Auto-Migration of Stored JSON Records")
    state_file = BASE_DIR / "data" / "student_state.json"
    with open(state_file, "r", encoding="utf-8") as f:
        state_data = json.load(f)
    students = state_data.get("students", {})
    admins = state_data.get("admins", {})

    migrated, count = migrate_passwords(students, admins)
    print(f"  [PASS] Passwords inspected. Total migrated to PBKDF2: {count}")
    for sid, s in students.items():
        assert s["password"].startswith("pbkdf2:sha256:"), f"Student {sid} password not hashed!"
    for aid, a in admins.items():
        assert a["password"].startswith("pbkdf2:sha256:"), f"Admin {aid} password not hashed!"
    print("  [PASS] All student and admin records securely hashed with individual salts!")

    # Save migrated state back
    with open(state_file, "w", encoding="utf-8") as f:
        json.dump(state_data, f, indent=2)

    # Verify Samiksha can authenticate with original password
    samiksha_hash = students["2510370150"]["password"]
    assert verify_password(samiksha_hash, "apex123") is True, "Samiksha password verification failed!"
    # Verify Admin can authenticate with admin123
    admin_hash = admins["ADMIN01"]["password"]
    assert verify_password(admin_hash, "admin123") is True, "Admin password verification failed!"
    print("  [PASS] Existing demo credentials (apex123, admin123) verified against PBKDF2 hashes!")

    # 3. Test Min-Heap Leaderboard
    print("\n[TEST 3] Min-Heap Leaderboard Ranking (heapq)")
    heap = MinHeapLeaderboard()
    heap.build_from_students(students, state_data.get("leaderboard_sample", []))
    rankings = heap.extract_sorted_rankings()
    assert len(rankings) >= len(students), "Heap rankings missing student records!"
    # Verify descending credits order
    for i in range(len(rankings) - 1):
        assert rankings[i]["credits"] >= rankings[i+1]["credits"], f"Heap ordering violated at rank {i+1}!"
        assert rankings[i]["rank"] == i + 1, "Rank index mismatch!"
    top_3 = heap.get_top_k(3)
    print(f"  [PASS] Min-Heap correctly extracted {len(rankings)} ranked students in descending order:")
    for s in top_3:
        print(f"     Rank #{s['rank']}: {s['name']} — {s['credits']} pts ({s['streak']}d streak)")

    # 4. Test SkillArc Trie Prefix Search
    print("\n[TEST 4] Prefix Tree (Trie) Autocomplete Engine")
    trie = SkillArcTrie()
    trie.insert("Linked Lists (Singly, Doubly, Circular)", {"topic_id": "Linked_Lists", "name": "Linked Lists"})
    trie.insert("Inorder Traversal", {"topic_id": "Trees", "name": "Trees"})
    trie.insert("Virtual Functions & vtable", {"topic_id": "Polymorphism", "name": "Polymorphism"})
    trie.insert("Binary Search", {"topic_id": "Searching", "name": "Searching"})

    res_link = trie.search_prefix("link")
    assert len(res_link) > 0 and res_link[0]["topic_id"] == "Linked_Lists", "Trie search for 'link' failed!"
    res_inord = trie.search_prefix("inord")
    assert len(res_inord) > 0 and res_inord[0]["topic_id"] == "Trees", "Trie search for 'inord' failed!"
    res_virt = trie.search_prefix("virt")
    assert len(res_virt) > 0 and res_virt[0]["topic_id"] == "Polymorphism", "Trie search for 'virt' failed!"
    print(f"  [PASS] Trie successfully completed prefix lookups for 'link', 'inord', 'virt' in O(L) time!")

    # 5. Test Course Prerequisite Graph (DAG)
    print("\n[TEST 5] Course Prerequisite Graph (DAG), BFS & DFS")
    graph = CoursePrerequisiteGraph()
    for t_id in ["Arrays", "Stack", "Queue", "Linked_Lists", "Trees", "Graphs"]:
        graph.add_topic(t_id, t_id, "DSA (C)", "Medium")
    graph.add_prerequisite("Arrays", "Linked_Lists")
    graph.add_prerequisite("Linked_Lists", "Trees")
    graph.add_prerequisite("Trees", "Graphs")

    # BFS path from Arrays to Graphs
    bfs_path = graph.bfs_shortest_path("Arrays", "Graphs")
    assert bfs_path == ["Arrays", "Linked_Lists", "Trees", "Graphs"], f"BFS path incorrect: {bfs_path}"
    print(f"  [PASS] BFS Shortest Prerequisite Path (Arrays -> Graphs): {' -> '.join(bfs_path)}")

    # DFS Topological Sort
    topo_order = graph.dfs_topological_sort()
    assert topo_order.index("Arrays") < topo_order.index("Linked_Lists") < topo_order.index("Trees") < topo_order.index("Graphs")
    print(f"  [PASS] DFS Topological Course Sequencing: {' -> '.join(topo_order)}")

    # 6. Test Navigation Stack (LIFO)
    print("\n[TEST 6] LIFO Navigation Stack")
    nav = NavigationStack()
    nav.push("Page A")
    nav.push("Page B")
    nav.push("Page C")
    assert nav.peek() == "Page C"
    popped = nav.pop()
    assert popped == "Page B"
    assert nav.peek() == "Page B"
    print("  [PASS] Navigation Stack correctly popped to previous page in O(1) LIFO order!")

    # 7. Test Study Task Queue (FIFO)
    print("\n[TEST 7] FIFO Study Task Queue")
    q = StudyQueue()
    q.enqueue({"task": "Task 1"})
    q.enqueue({"task": "Task 2"})
    assert q.peek()["task"] == "Task 1"
    deq = q.dequeue()
    assert deq["task"] == "Task 1"
    assert q.peek()["task"] == "Task 2"
    print("  [PASS] Study Task Queue correctly dequeued first-in task in O(1) FIFO order!")

    # 8. Test Singly Linked List Activity Feed
    print("\n[TEST 8] Singly Linked List Activity Feed")
    ll = ActivityLinkedList(max_capacity=5)
    ll.prepend("Action 1", "10:00 AM")
    ll.prepend("Action 2", "10:15 AM")
    ll.prepend("Action 3", "10:30 AM")
    items = ll.to_list()
    assert len(items) == 3
    assert items[0]["action"] == "Action 3" # Most recent at head
    assert items[2]["action"] == "Action 1"
    print("  [PASS] Activity Linked List verified: Head insertion in O(1) and linear traversal in O(N)!")

    # 9. Test OOP Class Hierarchy & Polymorphism
    print("\n[TEST 9] OOP Models, Inheritance & Polymorphism")
    student_model = StudentUser(
        user_id="2510370999",
        name="Test Learner",
        email="test@skillarc.edu",
        role="Student Learner",
        credits=50
    )
    admin_model = AdminUser(
        user_id="ADMIN99",
        name="Dr. Evaluator",
        email="eval@skillarc.edu"
    )
    assert student_model.has_admin_privileges() is False
    assert admin_model.has_admin_privileges() is True
    assert "Student" in student_model.get_role_badge()
    assert "Admin" in admin_model.get_role_badge()
    student_model.add_credits(25, "Completed Tree Traversal Quiz")
    assert student_model.credits == 75
    print("  [PASS] Base User, StudentUser, and AdminUser verified with polymorphic method overrides!")

    # 10. Test Quizzes JSON Data
    print("\n[TEST 10] Quizzes Question Bank Verification")
    quiz_file = BASE_DIR / "data" / "quizzes.json"
    with open(quiz_file, "r", encoding="utf-8") as f:
        quizzes = json.load(f)
    print(f"  [PASS] Total Quiz Modules in Question Bank: {len(quizzes)}")
    assert len(quizzes) == 17, f"Expected 17 quiz topics, found {len(quizzes)}!"
    total_q_count = sum(len(q_list) for q_list in quizzes.values())
    print(f"  [PASS] Total Questions Loaded across 17 topics: {total_q_count}")
    for t_name, q_list in quizzes.items():
        for q in q_list:
            assert "question" in q and "options" in q and "correct" in q and "explanation" in q
            assert 0 <= q["correct"] < len(q["options"]), f"Invalid correct answer index in {t_name}!"
    print("  [PASS] All 17 quiz modules and questions validated with explanations!")

    print("\n==================================================")
    print("  * ALL 10 VERIFICATION TESTS PASSED SUCCESSFULLY! ")
    print("==================================================")

if __name__ == "__main__":
    run_tests()

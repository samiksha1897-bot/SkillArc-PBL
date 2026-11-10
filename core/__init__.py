"""
SkillArc Core Architecture Package — Phase III
Contains genuine DSA and OOP foundational engines powering the SkillArc platform:
- Security & Password Hashing (PBKDF2-HMAC-SHA256 with individual salts)
- DSA Engine (Min-Heap Leaderboard, Trie Autocomplete, Keyword Inverted Index, Course Graph DAG, Navigation Stack, FIFO Task Queue, Singly Linked List Activity Feed)
- OOP Models (User base class, StudentUser & AdminUser inheritance, ProgressTracker composition, LearningModule abstraction)
"""

from .security import hash_password, verify_password, migrate_passwords
from .dsa_engine import (
    MinHeapLeaderboard,
    SkillArcTrie,
    KeywordInvertedIndex,
    CoursePrerequisiteGraph,
    NavigationStack,
    StudyQueue,
    ActivityLinkedList,
    ActivityNode
)
from .oop_models import (
    User,
    StudentUser,
    AdminUser,
    LearningModule,
    DSAModule,
    OOPModule
)

__all__ = [
    "hash_password",
    "verify_password",
    "migrate_passwords",
    "MinHeapLeaderboard",
    "SkillArcTrie",
    "KeywordInvertedIndex",
    "CoursePrerequisiteGraph",
    "NavigationStack",
    "StudyQueue",
    "ActivityLinkedList",
    "ActivityNode",
    "User",
    "StudentUser",
    "AdminUser",
    "LearningModule",
    "DSAModule",
    "OOPModule"
]

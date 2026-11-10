"""
SkillArc OOP Architecture Models — Phase III
Implements core Object-Oriented Programming principles:
1. Encapsulation: Sensitive student metrics (credits, streak, quiz results) are private
   and modifiable only through validated member methods.
2. Inheritance: Base User class derived into specialized StudentUser and AdminUser subclasses.
3. Polymorphism: Virtual-style method overrides for role badges, permissions, and dashboards.
4. Abstraction: Abstract Base Classes (ABC) User and LearningModule define mandatory interfaces.
5. Composition: StudentUser encapsulates ProgressTracker, ActivityLinkedList, and BadgeWallet.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from datetime import datetime
from .dsa_engine import ActivityLinkedList


# ==============================================================================
# 1. BASE USER CLASS (ABSTRACTION & ENCAPSULATION)
# ==============================================================================
class User(ABC):
    """
    Abstract Base Class for all authenticated entities in SkillArc.
    Demonstrates Abstraction and Encapsulation.
    """
    def __init__(self, user_id: str, name: str, email: str, role: str, department: str, avatar: str, password_hash: str):
        self._user_id = user_id
        self._name = name
        self._email = email
        self._role = role
        self._department = department
        self._avatar = avatar
        self._password_hash = password_hash

    # Encapsulation: Public Read-Only Properties
    @property
    def user_id(self) -> str:
        return self._user_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

    @property
    def role(self) -> str:
        return self._role

    @property
    def department(self) -> str:
        return self._department

    @property
    def avatar(self) -> str:
        return self._avatar

    @property
    def password_hash(self) -> str:
        return self._password_hash

    # Polymorphic Abstract Methods
    @abstractmethod
    def get_role_badge(self) -> str:
        """Returns the HTML badge appropriate for the role."""
        pass

    @abstractmethod
    def has_admin_privileges(self) -> bool:
        """Returns boolean indicating supervisor access."""
        pass

    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """Serializes user model to dictionary for JSON persistence."""
        pass


# ==============================================================================
# 2. STUDENT USER (INHERITANCE & COMPOSITION)
# ==============================================================================
class StudentUser(User):
    """
    Represents an undergraduate student learner.
    Inherits from User. Composes ActivityLinkedList and progress metrics.
    """
    def __init__(
        self,
        user_id: str,
        name: str,
        email: str,
        role: str = "Student Learner",
        department: str = "B.Tech CSE",
        avatar: str = "🎓",
        password_hash: str = "",
        credits: int = 50,
        streak_days: int = 1,
        completed_topics: Optional[List[str]] = None,
        in_progress_topics: Optional[List[str]] = None,
        quiz_history: Optional[Dict[str, Any]] = None,
        badges: Optional[List[str]] = None,
        redemptions: Optional[List[Dict[str, Any]]] = None,
        recent_activity: Optional[List[Dict[str, str]]] = None
    ):
        super().__init__(user_id, name, email, role, department, avatar, password_hash)
        
        # Encapsulated progress state
        self._credits = max(0, credits)
        self._streak_days = max(1, streak_days)
        self._completed_topics = list(completed_topics) if completed_topics else []
        self._in_progress_topics = list(in_progress_topics) if in_progress_topics else ["Arrays"]
        self._quiz_history = dict(quiz_history) if quiz_history else {}
        self._badges = list(badges) if badges else ["first_step"]
        self._redemptions = list(redemptions) if redemptions else []
        
        # Composition: Encapsulates dynamic Singly Linked List for activity telemetry
        self._activity_feed = ActivityLinkedList.from_list(recent_activity if recent_activity else [])

    # Polymorphic Implementations
    def get_role_badge(self) -> str:
        return f"<span style='background: #e0e7ff; color: #4338ca; padding: 2px 8px; border-radius: 4px; font-size: 0.75rem; font-weight: 700;'>🎓 {self._role}</span>"

    def has_admin_privileges(self) -> bool:
        return False

    # Encapsulated Progress Methods
    @property
    def credits(self) -> int:
        return self._credits

    @property
    def streak_days(self) -> int:
        return self._streak_days

    @property
    def completed_topics(self) -> List[str]:
        return list(self._completed_topics)

    @property
    def in_progress_topics(self) -> List[str]:
        return list(self._in_progress_topics)

    @property
    def quiz_history(self) -> Dict[str, Any]:
        return dict(self._quiz_history)

    @property
    def badges(self) -> List[str]:
        return list(self._badges)

    @property
    def redemptions(self) -> List[Dict[str, Any]]:
        return list(self._redemptions)

    def add_credits(self, points: int, reason: str = "") -> None:
        """Safely awards credit points and logs the transaction."""
        if points > 0:
            self._credits += points
            if reason:
                self.log_activity(f"{reason} (+{points} pts)")

    def deduct_credits(self, cost: int, item_title: str) -> bool:
        """Safely deducts credits for reward store redemption."""
        if self._credits >= cost:
            self._credits -= cost
            self.log_activity(f"Redeemed reward: '{item_title}' (-{cost} pts)")
            return True
        return False

    def mark_topic_completed(self, topic_id: str, topic_name: str) -> None:
        """Updates syllabus completion state and awards +15 milestone credits."""
        if topic_id not in self._completed_topics:
            self._completed_topics.append(topic_id)
            if topic_id in self._in_progress_topics:
                self._in_progress_topics.remove(topic_id)
            self.add_credits(15, f"Completed syllabus topic '{topic_name}'")

    def record_quiz_attempt(
        self,
        topic_id: str,
        score: int,
        total: int,
        points: int,
        difficulty: str = "Medium"
    ) -> bool:
        """
        Records a quiz submission.
        Guarantees anti-abuse: repeat attempts update score and retake count,
        but only the first successful attempt awards credit points.
        """
        accuracy = round((score / total * 100), 1) if total > 0 else 0.0
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        is_first_attempt = (topic_id not in self._quiz_history)
        
        if is_first_attempt:
            self._quiz_history[topic_id] = {
                "score": score,
                "total": total,
                "percentage": accuracy,
                "points_awarded": points,
                "attempts_count": 1,
                "difficulty": difficulty,
                "attempted_at": now_str
            }
            self.add_credits(points, f"Scored {accuracy}% on {topic_id} Quiz")
            return True
        else:
            existing = self._quiz_history[topic_id]
            existing["attempts_count"] = existing.get("attempts_count", 1) + 1
            existing["score"] = score
            existing["percentage"] = accuracy
            existing["last_retake_at"] = now_str
            self.log_activity(f"Retook {topic_id} Quiz: {accuracy}% (Attempt #{existing['attempts_count']})")
            return False

    def log_activity(self, action: str) -> None:
        """Prepends a new action node to the ActivityLinkedList in O(1) time."""
        now_time = datetime.now().strftime("%I:%M %p")
        self._activity_feed.prepend(action, now_time)

    def get_recent_activities(self) -> List[Dict[str, str]]:
        return self._activity_feed.to_list()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self._user_id,
            "name": self._name,
            "email": self._email,
            "password": self._password_hash,
            "role": self._role,
            "department": self._department,
            "avatar": self._avatar,
            "credits": self._credits,
            "streak_days": self._streak_days,
            "completed_topics": self._completed_topics,
            "in_progress_topics": self._in_progress_topics,
            "quiz_history": self._quiz_history,
            "badges": self._badges,
            "redemptions": self._redemptions,
            "recent_activity": self._activity_feed.to_list()
        }


# ==============================================================================
# 3. ADMIN USER (INHERITANCE & POLYMORPHISM)
# ==============================================================================
class AdminUser(User):
    """
    Represents an authorized faculty evaluator / course administrator.
    Inherits from User. Implements supervisory audit capabilities.
    """
    def __init__(
        self,
        user_id: str,
        name: str,
        email: str,
        role: str = "Administrator",
        department: str = "Faculty of Computer Science & Engineering",
        avatar: str = "🛡️",
        password_hash: str = ""
    ):
        super().__init__(user_id, name, email, role, department, avatar, password_hash)

    def get_role_badge(self) -> str:
        return f"<span style='background: #fee2e2; color: #991b1b; padding: 2px 8px; border-radius: 4px; font-size: 0.75rem; font-weight: 700;'>🛡️ {self._role}</span>"

    def has_admin_privileges(self) -> bool:
        return True

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self._user_id,
            "name": self._name,
            "email": self._email,
            "role": self._role,
            "department": self._department,
            "avatar": self._avatar,
            "password": self._password_hash
        }


# ==============================================================================
# 4. LEARNING MODULE ABSTRACTION (ABSTRACTION & INHERITANCE)
# ==============================================================================
class LearningModule(ABC):
    """
    Abstract Base Class for all pedagogical course modules in SkillArc.
    """
    def __init__(self, topic_id: str, name: str, subject: str, difficulty: str, estimated_time: str):
        self.topic_id = topic_id
        self.name = name
        self.subject = subject
        self.difficulty = difficulty
        self.estimated_time = estimated_time

    @abstractmethod
    def get_code_language(self) -> str:
        pass

    @abstractmethod
    def get_curriculum_track(self) -> str:
        pass


class DSAModule(LearningModule):
    """Data Structures and Algorithms module implemented in C."""
    def __init__(self, topic_id: str, name: str, difficulty: str, estimated_time: str):
        super().__init__(topic_id, name, "DSA (C)", difficulty, estimated_time)

    def get_code_language(self) -> str:
        return "c"

    def get_curriculum_track(self) -> str:
        return "Data Structures in C (Procedural & Memory Management)"


class OOPModule(LearningModule):
    """Object-Oriented Programming module implemented in C++."""
    def __init__(self, topic_id: str, name: str, difficulty: str, estimated_time: str):
        super().__init__(topic_id, name, "OOP (C++)", difficulty, estimated_time)

    def get_code_language(self) -> str:
        return "cpp"

    def get_curriculum_track(self) -> str:
        return "Object-Oriented Programming in C++ (Classes, Virtuals & STL)"

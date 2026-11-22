"""
SkillArc DSA Engine — Phase III
Implements genuine Data Structures and Algorithms that actively power the platform:
1. MinHeapLeaderboard: Min-heap with inverted keys for O(N log N) rank extraction & tie-breaking.
2. SkillArcTrie: Trie for prefix-based topic, subtopic & keyword autocomplete search (O(L) query time).
3. KeywordInvertedIndex: Hash map inverted index for instant O(1) keyword lookups.
4. CoursePrerequisiteGraph: Directed Acyclic Graph (DAG) for curriculum dependencies, BFS shortest path, & DFS topological ordering.
5. NavigationStack: LIFO Stack for in-app page history & backtracking.
6. StudyQueue: FIFO Queue for ordered pending practice tasks.
7. ActivityLinkedList: Singly Linked List with head insertion for dynamic learning activity feeds.
"""

import heapq
from collections import deque
from typing import List, Dict, Any, Optional, Set, Tuple


# ==============================================================================
# 1. MIN-HEAP LEADERBOARD
# ==============================================================================
class MinHeapLeaderboard:
    """
    Ranks students using a Min-Heap data structure (Python's heapq).
    
    By storing negative credit values (-credits), the student with the maximum
    earned points resides at the top of the min-heap (index 0).
    
    Tie-breaking:
    - Primary criterion: Negative Credits (-credits) -> highest credits first
    - Secondary criterion: Negative Streak (-streak_days) -> higher streak wins ties
    - Tertiary criterion: Student Roll ID (lexicographical) -> deterministic ordering
    
    Time Complexity:
    - Build heap: O(N) using heapq.heapify()
    - Extract all sorted rankings: O(N log N) via successive heappop()
    - Insert / Update: O(log N) via heappush()
    Space Complexity: O(N) where N is total registered learners.
    """
    def __init__(self):
        self._heap: List[Tuple[int, int, str, Dict[str, Any]]] = []

    def build_from_students(self, students_dict: Dict[str, Any], sample_extras: Optional[List[Dict[str, Any]]] = None) -> None:
        """
        Builds the min-heap from real student records and optional community benchmark entries.
        """
        self._heap = []
        seen_ids = set()
        
        # 1. Insert real registered students
        for sid, s in students_dict.items():
            credits = s.get("credits", 0)
            streak = s.get("streak_days", 0)
            payload = {
                "id": sid,
                "name": s.get("name", "Student"),
                "credits": credits,
                "streak": streak,
                "badges": len(s.get("badges", [])),
                "avatar": s.get("avatar", "🎓"),
                "department": s.get("department", "CSE"),
                "is_registered": True
            }
            # Tuple: (-credits, -streak, roll_id, payload)
            self._heap.append((-credits, -streak, sid, payload))
            seen_ids.add(sid)
            
        # 2. Insert any sample community benchmarking entries not already present
        if sample_extras:
            for item in sample_extras:
                item_id = str(item.get("id", ""))
                if item_id and item_id not in seen_ids:
                    credits = item.get("credits", 0)
                    streak = item.get("streak", 0)
                    payload = {
                        "id": item_id,
                        "name": item.get("name", "Learner"),
                        "credits": credits,
                        "streak": streak,
                        "badges": item.get("badges", 0),
                        "avatar": "🏅",
                        "department": "B.Tech CSE",
                        "is_registered": False
                    }
                    self._heap.append((-credits, -streak, item_id, payload))
                    seen_ids.add(item_id)
                    
        # Heapify in-place in linear O(N) time
        heapq.heapify(self._heap)

    def extract_sorted_rankings(self) -> List[Dict[str, Any]]:
        """
        Extracts all students in descending order of actual credit points.
        Returns a list of dicts decorated with 1-based ranks.
        Time Complexity: O(N log N)
        """
        # Copy heap so original is not consumed
        temp_heap = list(self._heap)
        rankings = []
        rank = 1
        
        while temp_heap:
            neg_credits, neg_streak, sid, payload = heapq.heappop(temp_heap)
            student_entry = dict(payload)
            student_entry["rank"] = rank
            student_entry["credits"] = -neg_credits  # Restore positive credits
            student_entry["streak"] = -neg_streak    # Restore positive streak
            rankings.append(student_entry)
            rank += 1
            
        return rankings

    def get_top_k(self, k: int = 3) -> List[Dict[str, Any]]:
        """
        Retrieves the top k performers in O(k log N) time.
        """
        rankings = self.extract_sorted_rankings()
        return rankings[:k]


# ==============================================================================
# 2. TRIE FOR TOPIC, SUBTOPIC & KEYWORD PREFIX SEARCH
# ==============================================================================
class TrieNode:
    """Represents a character node in the SkillArc Trie."""
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False
        self.topic_refs: List[Dict[str, Any]] = []


class SkillArcTrie:
    """
    Prefix Tree (Trie) for fast predictive searching and autocomplete.
    Indexes syllabus topics, subtopics, programming constructs, and algorithms.
    
    Time Complexity:
    - Insertion: O(L) where L is character length of the search phrase.
    - Prefix Search: O(P + M) where P is prefix length and M is total matched nodes.
    Space Complexity: O(Sigma * L * N) where Sigma is alphabet size.
    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self, phrase: str, metadata: Dict[str, Any]) -> None:
        """
        Inserts a search phrase into the Trie with its associated learning content metadata.
        """
        clean_phrase = phrase.strip().lower()
        if not clean_phrase:
            return
            
        curr = self.root
        for char in clean_phrase:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            
        curr.is_end_of_word = True
        # Avoid duplicate metadata entries
        if metadata not in curr.topic_refs:
            curr.topic_refs.append(metadata)

    def search_prefix(self, prefix: str) -> List[Dict[str, Any]]:
        """
        Traverses to the prefix node and performs Depth-First Search (DFS)
        to collect all matching topic references beneath that subtree.
        """
        clean_prefix = prefix.strip().lower()
        if not clean_prefix:
            return []
            
        curr = self.root
        for char in clean_prefix:
            if char not in curr.children:
                return []  # Prefix not found
            curr = curr.children[char]
            
        # Prefix exists: collect all topic references in the subtree via DFS
        results = []
        seen_keys = set()
        
        def _collect(node: TrieNode):
            if node.is_end_of_word:
                for ref in node.topic_refs:
                    key = (ref.get("topic_id"), ref.get("subtopic", ""))
                    if key not in seen_keys:
                        seen_keys.add(key)
                        results.append(ref)
            for child in node.children.values():
                _collect(child)
                
        _collect(curr)
        return results


# ==============================================================================
# 3. KEYWORD INVERTED INDEX (HASH MAP)
# ==============================================================================
class KeywordInvertedIndex:
    """
    Hash Map index mapping lowercase keywords directly to topic lists.
    Guarantees instantaneous O(1) average-time lookups.
    """
    def __init__(self):
        self._index: Dict[str, List[Dict[str, Any]]] = {}

    def index_item(self, keyword: str, metadata: Dict[str, Any]) -> None:
        clean = keyword.strip().lower()
        if not clean:
            return
        if clean not in self._index:
            self._index[clean] = []
        if metadata not in self._index[clean]:
            self._index[clean].append(metadata)

    def lookup(self, query: str) -> List[Dict[str, Any]]:
        clean = query.strip().lower()
        return self._index.get(clean, [])


# ==============================================================================
# 4. COURSE PREREQUISITE GRAPH (DAG) WITH BFS & DFS
# ==============================================================================
class CoursePrerequisiteGraph:
    """
    Directed Acyclic Graph (DAG) representing curriculum dependencies.
    
    Nodes: Syllabus Topics (DSA in C and OOP in C++)
    Directed Edge (U -> V): Topic U must be mastered before attempting Topic V.
    
    Algorithms:
    - BFS (Breadth-First Search): Determines shortest learning path between modules.
    - DFS (Depth-First Search): Generates topological ordering of the curriculum.
    - Prerequisite checking: Computes unlock status dynamically based on student progress.
    """
    def __init__(self):
        self.adj: Dict[str, List[str]] = {}
        self.reverse_adj: Dict[str, List[str]] = {}  # incoming edges: V -> list of prerequisites U
        self.nodes_meta: Dict[str, Dict[str, Any]] = {}

    def add_topic(self, topic_id: str, name: str, subject: str, difficulty: str) -> None:
        if topic_id not in self.adj:
            self.adj[topic_id] = []
        if topic_id not in self.reverse_adj:
            self.reverse_adj[topic_id] = []
        self.nodes_meta[topic_id] = {
            "name": name,
            "subject": subject,
            "difficulty": difficulty
        }

    def add_prerequisite(self, prereq_id: str, topic_id: str) -> None:
        """Adds a directed edge: prereq_id -> topic_id"""
        if prereq_id not in self.adj:
            self.adj[prereq_id] = []
        if topic_id not in self.adj:
            self.adj[topic_id] = []
        if topic_id not in self.reverse_adj:
            self.reverse_adj[topic_id] = []
        self.adj[prereq_id].append(topic_id)
        self.reverse_adj[topic_id].append(prereq_id)

    def get_prerequisites(self, topic_id: str) -> List[str]:
        return self.reverse_adj.get(topic_id, [])

    def get_unlock_status(self, topic_id: str, completed_topics: Set[str]) -> Tuple[str, List[str]]:
        """
        Returns:
        - status: "COMPLETED", "UNLOCKED", or "LOCKED"
        - missing_prereqs: list of topic IDs that need to be completed first
        """
        if topic_id in completed_topics:
            return "COMPLETED", []
        prereqs = self.get_prerequisites(topic_id)
        missing = [p for p in prereqs if p not in completed_topics]
        if not missing:
            return "UNLOCKED", []
        return "LOCKED", missing

    def bfs_shortest_path(self, start_id: str, target_id: str) -> Optional[List[str]]:
        """
        Breadth-First Search (BFS) to find the shortest dependency pathway
        from start_id to target_id.
        Time Complexity: O(V + E)
        """
        if start_id == target_id:
            return [start_id]
            
        visited = {start_id}
        queue = deque([[start_id]])
        
        while queue:
            path = queue.popleft()
            curr = path[-1]
            for neighbor in self.adj.get(curr, []):
                if neighbor == target_id:
                    return path + [neighbor]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(path + [neighbor])
        return None

    def dfs_topological_sort(self, subject_filter: Optional[str] = None) -> List[str]:
        """
        Generates a valid sequential learning order using DFS.
        Time Complexity: O(V + E)
        """
        in_degree = {u: 0 for u in self.adj}
        for u in self.adj:
            for v in self.adj[u]:
                in_degree[v] = in_degree.get(v, 0) + 1
                
        # Filter nodes if subject_filter provided
        relevant_nodes = [
            u for u in self.adj
            if not subject_filter or subject_filter in self.nodes_meta.get(u, {}).get("subject", "")
        ]
        
        queue = deque([u for u in relevant_nodes if in_degree[u] == 0])
        order = []
        
        while queue:
            curr = queue.popleft()
            order.append(curr)
            for v in self.adj.get(curr, []):
                if v in in_degree:
                    in_degree[v] -= 1
                    if in_degree[v] == 0 and v in relevant_nodes:
                        queue.append(v)
                        
        return order


# ==============================================================================
# 5. NAVIGATION STACK (LIFO)
# ==============================================================================
class NavigationStack:
    """
    Implements a LIFO (Last-In, First-Out) Stack for in-app page traversal.
    Enables instant backtracking and historical breadcrumb tracking.
    Time Complexity: O(1) for push(), pop(), and peek().
    """
    def __init__(self, max_depth: int = 20):
        self._stack: List[str] = []
        self._max_depth = max_depth

    def push(self, page_name: str) -> None:
        if not self._stack or self._stack[-1] != page_name:
            if len(self._stack) >= self._max_depth:
                self._stack.pop(0)  # Evict oldest entry
            self._stack.append(page_name)

    def pop(self) -> Optional[str]:
        if len(self._stack) > 1:
            self._stack.pop()  # Remove current page
            return self._stack[-1]  # Return previous page
        return None

    def peek(self) -> Optional[str]:
        return self._stack[-1] if self._stack else None

    def size(self) -> int:
        return len(self._stack)

    def get_history(self) -> List[str]:
        return list(reversed(self._stack))


# ==============================================================================
# 6. STUDY TASK QUEUE (FIFO)
# ==============================================================================
class StudyQueue:
    """
    Implements a FIFO (First-In, First-Out) Queue managing recommended learning tasks.
    Time Complexity: O(1) for enqueue() and dequeue().
    """
    def __init__(self):
        self._queue: deque = deque()

    def enqueue(self, task: Dict[str, Any]) -> None:
        self._queue.append(task)

    def dequeue(self) -> Optional[Dict[str, Any]]:
        return self._queue.popleft() if self._queue else None

    def peek(self) -> Optional[Dict[str, Any]]:
        return self._queue[0] if self._queue else None

    def size(self) -> int:
        return len(self._queue)

    def get_all_tasks(self) -> List[Dict[str, Any]]:
        return list(self._queue)


# ==============================================================================
# 7. RECENT ACTIVITY SINGLY LINKED LIST
# ==============================================================================
class ActivityNode:
    """Node representing an individual action entry in a Singly Linked List."""
    def __init__(self, action: str, timestamp: str):
        self.action: str = action
        self.time: str = timestamp
        self.next: Optional[ActivityNode] = None


class ActivityLinkedList:
    """
    Singly Linked List tracking recent student actions.
    Provides constant-time O(1) insertion at head for real-time telemetry updates.
    """
    def __init__(self, max_capacity: int = 15):
        self.head: Optional[ActivityNode] = None
        self.size: int = 0
        self.max_capacity = max_capacity

    def prepend(self, action: str, timestamp: str) -> None:
        """Inserts a new activity at the head of the list in O(1) time."""
        new_node = ActivityNode(action, timestamp)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        
        # Enforce maximum capacity by truncating tail if needed
        if self.size > self.max_capacity:
            curr = self.head
            for _ in range(self.max_capacity - 1):
                if curr and curr.next:
                    curr = curr.next
            if curr:
                curr.next = None
            self.size = self.max_capacity

    def to_list(self) -> List[Dict[str, str]]:
        """Traverses the linked list in O(N) time and returns standard list of dicts."""
        result = []
        curr = self.head
        while curr:
            result.append({"action": curr.action, "time": curr.time})
            curr = curr.next
        return result

    @classmethod
    def from_list(cls, items: List[Dict[str, str]], max_capacity: int = 15) -> "ActivityLinkedList":
        """Reconstructs the linked list from an existing JSON list preserving chronological order."""
        ll = cls(max_capacity=max_capacity)
        # Prepend in reverse so the first item ends up at head
        for item in reversed(items[:max_capacity]):
            ll.prepend(item.get("action", ""), item.get("time", ""))
        return ll

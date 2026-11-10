"""
Update Phase-2/DSA/resources.json with curated video tutorials and practice problems
for all 17 topics across DSA (C) and OOP (C++).
"""

import json
from pathlib import Path

res_path = Path(r"C:\Users\sudeep\OneDrive\Documents\SkillArc-PBL\Phase-2\DSA\resources.json")

with open(res_path, "r", encoding="utf-8") as f:
    resources = json.load(f)

# Ensure DSA section
dsa = resources.setdefault("DSA", {})

dsa["Linked_Lists"] = {
    "title": "Linked Lists in C (Singly, Doubly, Circular)",
    "difficulty": "Medium",
    "estimated_time": "60 mins",
    "description": "Dynamic node-based linear structure eliminating fixed-size limitations through pointer linking.",
    "youtube": [
        {"title": "Linked List Data Structure (C Implementation) - Neso Academy", "url": "https://www.youtube.com/watch?v=R9PTBwOzceo"},
        {"title": "Reverse a Linked List - NeetCode", "url": "https://www.youtube.com/watch?v=G0_I-ZF0S38"}
    ],
    "practice": [
        {"platform": "LeetCode #206", "title": "Reverse Linked List", "url": "https://leetcode.com/problems/reverse-linked-list/"},
        {"platform": "LeetCode #141", "title": "Linked List Cycle Detection", "url": "https://leetcode.com/problems/linked-list-cycle/"},
        {"platform": "GeeksforGeeks", "title": "Singly Linked List Implementation & Operations", "url": "https://www.geeksforgeeks.org/data-structures/linked-list/"}
    ]
}

dsa["Trees"] = {
    "title": "Trees & Binary Search Trees (BST) in C",
    "difficulty": "Hard",
    "estimated_time": "75 mins",
    "description": "Hierarchical data structure with recursive ordering property enabling O(log n) average search and insertion.",
    "youtube": [
        {"title": "Binary Search Tree (BST) Complete Guide - Abdul Bari", "url": "https://www.youtube.com/watch?v=pYT9F8_LFTM"},
        {"title": "Binary Tree Inorder, Preorder, Postorder Traversals - Jenny's Lectures", "url": "https://www.youtube.com/watch?v=4_UDUj1j1GQ"}
    ],
    "practice": [
        {"platform": "LeetCode #94", "title": "Binary Tree Inorder Traversal", "url": "https://leetcode.com/problems/binary-tree-inorder-traversal/"},
        {"platform": "LeetCode #700", "title": "Search in a Binary Search Tree", "url": "https://leetcode.com/problems/search-in-a-binary-search-tree/"},
        {"platform": "GeeksforGeeks", "title": "Binary Search Tree (BST) Guide", "url": "https://www.geeksforgeeks.org/binary-search-tree-data-structure/"}
    ]
}

dsa["Graphs"] = {
    "title": "Graphs & Graph Traversals (BFS & DFS) in C",
    "difficulty": "Hard",
    "estimated_time": "80 mins",
    "description": "Non-linear network model representing pairwise relations using Adjacency Matrices and Adjacency Lists.",
    "youtube": [
        {"title": "Graph Data Structure Introduction - Abdul Bari", "url": "https://www.youtube.com/watch?v=pcKY4hjDrxk"},
        {"title": "Breadth First Search (BFS) and Depth First Search (DFS) - FreeCodeCamp", "url": "https://www.youtube.com/watch?v=tWVWeAqZ0WU"}
    ],
    "practice": [
        {"platform": "LeetCode #200", "title": "Number of Islands (Graph DFS/BFS)", "url": "https://leetcode.com/problems/number-of-islands/"},
        {"platform": "LeetCode #133", "title": "Clone Graph", "url": "https://leetcode.com/problems/clone-graph/"},
        {"platform": "GeeksforGeeks", "title": "Graph Data Structure Tutorial", "url": "https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/"}
    ]
}

dsa["Searching"] = {
    "title": "Searching Algorithms (Linear & Binary Search) in C",
    "difficulty": "Easy",
    "estimated_time": "40 mins",
    "description": "Algorithmic methods for key retrieval comparing linear sequential scans with divide-and-conquer binary search.",
    "youtube": [
        {"title": "Binary Search Algorithm in 5 Minutes - Bro Code", "url": "https://www.youtube.com/watch?v=fOMG1q36UuA"},
        {"title": "Linear and Binary Search Analysis - Neso Academy", "url": "https://www.youtube.com/watch?v=jXZfbeYdKmM"}
    ],
    "practice": [
        {"platform": "LeetCode #704", "title": "Binary Search", "url": "https://leetcode.com/problems/binary-search/"},
        {"platform": "LeetCode #35", "title": "Search Insert Position", "url": "https://leetcode.com/problems/search-insert-position/"},
        {"platform": "GeeksforGeeks", "title": "Searching Algorithms Complete Guide", "url": "https://www.geeksforgeeks.org/searching-algorithms/"}
    ]
}

dsa["Sorting"] = {
    "title": "Sorting Algorithms (Bubble, Selection, Insertion, Merge, Quick) in C",
    "difficulty": "Medium",
    "estimated_time": "70 mins",
    "description": "Comparative exploration of quadratic O(n^2) and log-linear O(n log n) sorting algorithms.",
    "youtube": [
        {"title": "Quick Sort Algorithm - Abdul Bari", "url": "https://www.youtube.com/watch?v=7h1s2SojIRw"},
        {"title": "Merge Sort Algorithm - Jenny's Lectures", "url": "https://www.youtube.com/watch?v=jlHkDBEumP0"}
    ],
    "practice": [
        {"platform": "LeetCode #912", "title": "Sort an Array", "url": "https://leetcode.com/problems/sort-an-array/"},
        {"platform": "LeetCode #75", "title": "Sort Colors (Dutch National Flag)", "url": "https://leetcode.com/problems/sort-colors/"},
        {"platform": "GeeksforGeeks", "title": "Sorting Algorithms Practice", "url": "https://www.geeksforgeeks.org/sorting-algorithms/"}
    ]
}

dsa["Hashing"] = {
    "title": "Hashing & Collision Handling in C",
    "difficulty": "Medium",
    "estimated_time": "55 mins",
    "description": "Direct memory mapping via hash functions with Open Addressing (Linear Probing) and Separate Chaining.",
    "youtube": [
        {"title": "Hashing Technique and Collision Resolution - Abdul Bari", "url": "https://www.youtube.com/watch?v=mFY0J5W8Udk"},
        {"title": "Hash Table Explained with Code - CS Dojo", "url": "https://www.youtube.com/watch?v=ea8BRGxGmlA"}
    ],
    "practice": [
        {"platform": "LeetCode #1", "title": "Two Sum (Hash Map Solution)", "url": "https://leetcode.com/problems/two-sum/"},
        {"platform": "LeetCode #217", "title": "Contains Duplicate", "url": "https://leetcode.com/problems/contains-duplicate/"},
        {"platform": "GeeksforGeeks", "title": "Hashing Data Structure Guide", "url": "https://www.geeksforgeeks.org/hashing-data-structure/"}
    ]
}

dsa["Advanced_DSA"] = {
    "title": "Advanced DSA Concepts (Pointers, DMA, Recursion, Sparse Matrices)",
    "difficulty": "Hard",
    "estimated_time": "65 mins",
    "description": "Low-level heap management using malloc/free, pointer arithmetic, recursion, and stack expression parsing.",
    "youtube": [
        {"title": "Pointers and Dynamic Memory in C - Harvard CS50", "url": "https://www.youtube.com/watch?v=2wAm3zCjW0Q"},
        {"title": "Infix to Postfix Conversion using Stack - Neso Academy", "url": "https://www.youtube.com/watch?v=vq-nUFGoG4Q"}
    ],
    "practice": [
        {"platform": "LeetCode #150", "title": "Evaluate Reverse Polish Notation", "url": "https://leetcode.com/problems/evaluate-reverse-polish-notation/"},
        {"platform": "LeetCode #50", "title": "Pow(x, n) using Recursion", "url": "https://leetcode.com/problems/powx-n/"},
        {"platform": "GeeksforGeeks", "title": "Sparse Matrix and Representation", "url": "https://www.geeksforgeeks.org/sparse-matrix-representation/"}
    ]
}

# Ensure OOPS section
oops = resources.setdefault("OOPS", {})

oops["CPP_Fundamentals"] = {
    "title": "C++ Fundamentals, Namespaces & Functions",
    "difficulty": "Easy",
    "estimated_time": "40 mins",
    "description": "Foundational modern C++ features: standard I/O streams, namespaces, function overloading, default arguments, and inline functions.",
    "youtube": [
        {"title": "C++ Programming Course - Beginner to Advanced (FreeCodeCamp)", "url": "https://www.youtube.com/watch?v=vLnPwxZdW4Y"},
        {"title": "Function Overloading and Inline Functions in C++ - The Cherno", "url": "https://www.youtube.com/watch?v=mQeR_91Wl5M"}
    ],
    "practice": [
        {"platform": "HackerRank", "title": "Functions in C++", "url": "https://www.hackerrank.com/challenges/c-tutorial-functions/problem"},
        {"platform": "GeeksforGeeks", "title": "Function Overloading in C++ Practice", "url": "https://www.geeksforgeeks.org/function-overloading-c/"}
    ]
}

oops["Exception_FileIO"] = {
    "title": "Exception Handling & File Streams in C++",
    "difficulty": "Medium",
    "estimated_time": "50 mins",
    "description": "Robust runtime error handling via try/catch/throw blocks and persistent file stream I/O using ifstream/ofstream.",
    "youtube": [
        {"title": "Exception Handling in C++ - The Cherno", "url": "https://www.youtube.com/watch?v=s5tN4hTfP_k"},
        {"title": "File Handling in C++ (fstream, ifstream, ofstream) - Jenny's Lectures", "url": "https://www.youtube.com/watch?v=8V4aQ0V_8xI"}
    ],
    "practice": [
        {"platform": "HackerRank", "title": "C++ Exception Handling", "url": "https://www.hackerrank.com/challenges/exceptional-server/problem"},
        {"platform": "GeeksforGeeks", "title": "File Handling in C++ Tutorial", "url": "https://www.geeksforgeeks.org/file-handling-c-classes/"}
    ]
}

oops["Templates_STL"] = {
    "title": "Templates & Standard Template Library (STL) in C++",
    "difficulty": "Hard",
    "estimated_time": "70 mins",
    "description": "Generic programming with function and class templates alongside industry-standard STL containers (vector, map, set, stack, queue).",
    "youtube": [
        {"title": "C++ STL Full Tutorial - Luv", "url": "https://www.youtube.com/watch?v=zGoQUz3gGmM"},
        {"title": "Templates in C++ Explained - The Cherno", "url": "https://www.youtube.com/watch?v=I-hZkUa9mIs"}
    ],
    "practice": [
        {"platform": "LeetCode #347", "title": "Top K Frequent Elements (using STL Map/Priority Queue)", "url": "https://leetcode.com/problems/top-k-frequent-elements/"},
        {"platform": "HackerRank", "title": "C++ Class Template Specialization", "url": "https://www.hackerrank.com/challenges/cpp-class-template-specialization/problem"},
        {"platform": "GeeksforGeeks", "title": "The C++ Standard Template Library (STL)", "url": "https://www.geeksforgeeks.org/the-c-standard-template-library-stl/"}
    ]
}

with open(res_path, "w", encoding="utf-8") as f:
    json.dump(resources, f, indent=2)

print("Updated Phase-2/DSA/resources.json with all 17 topics!")

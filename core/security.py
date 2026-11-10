"""
SkillArc Security & Authentication Engine — Phase III
Implements secure cryptographic password hashing using PBKDF2-HMAC-SHA256
with individual 128-bit random salts and 100,000 iterations.
Adheres to OWASP password storage recommendations with zero external dependencies.
"""

import os
import hashlib
import hmac
from typing import Dict, Any, Tuple


PBKDF2_ALGORITHM = "sha256"
PBKDF2_ITERATIONS = 100000
SALT_BYTES = 16


def hash_password(password: str) -> str:
    """
    Generate a cryptographically secure PBKDF2-HMAC-SHA256 salted hash.
    Format: pbkdf2:sha256:<iterations>:<salt_hex>:<hash_hex>
    Time Complexity: O(iterations) to deter brute-force and dictionary attacks.
    Space Complexity: O(1)
    """
    if not isinstance(password, str):
        password = str(password)
    
    salt = os.urandom(SALT_BYTES).hex()
    derived = hashlib.pbkdf2_hmac(
        PBKDF2_ALGORITHM,
        password.encode("utf-8"),
        salt.encode("utf-8"),
        PBKDF2_ITERATIONS
    ).hex()
    return f"pbkdf2:{PBKDF2_ALGORITHM}:{PBKDF2_ITERATIONS}:{salt}:{derived}"


def verify_password(stored_hash: str, candidate_password: str) -> bool:
    """
    Verify a candidate password against the stored password hash.
    Uses constant-time string comparison (hmac.compare_digest) to prevent timing attacks.
    Supports seamless fallback verification for unmigrated legacy plaintext entries.
    """
    if not stored_hash or not candidate_password:
        return False
        
    # Check if format is PBKDF2
    if stored_hash.startswith("pbkdf2:sha256:"):
        try:
            parts = stored_hash.split(":")
            if len(parts) != 5:
                return False
            _, algorithm, iterations_str, salt, target_hash = parts
            iterations = int(iterations_str)
            test_derived = hashlib.pbkdf2_hmac(
                algorithm,
                candidate_password.encode("utf-8"),
                salt.encode("utf-8"),
                iterations
            ).hex()
            return hmac.compare_digest(target_hash, test_derived)
        except Exception:
            return False
            
    # Legacy plaintext backward compatibility check
    return hmac.compare_digest(stored_hash, candidate_password)


def migrate_passwords(students_dict: Dict[str, Any], admins_dict: Dict[str, Any]) -> Tuple[bool, int]:
    """
    Inspects all student and admin records in storage.
    If any record stores a plain-text password, it is converted to a secure PBKDF2 hash.
    Returns: (was_modified, count_migrated)
    """
    migrated_count = 0
    
    # Migrate student passwords
    for sid, student in students_dict.items():
        pwd = student.get("password", "")
        if pwd and not pwd.startswith("pbkdf2:sha256:"):
            student["password"] = hash_password(pwd)
            migrated_count += 1
            
    # Migrate admin passwords
    for aid, admin in admins_dict.items():
        pwd = admin.get("password", "")
        if pwd and not pwd.startswith("pbkdf2:sha256:"):
            admin["password"] = hash_password(pwd)
            migrated_count += 1
            
    return (migrated_count > 0), migrated_count

with open(r"C:\Users\sudeep\OneDrive\Documents\SkillArc-PBL\tools\build_phase3_app.py", "r", encoding="utf-8") as f:
    code = f.read()

# Fix input="1\n2\n2\n"
code = code.replace('input="1\\n2\\n2\\n"', 'input="1\\\\n2\\\\n2\\\\n"')
# Fix any regex escapes
code = code.replace(r're.match(r"^[A-Za-z\s\.]+$"', r're.match(r"^[A-Za-z\\s\\.]+$"')
code = code.replace(r're.match(r"^[\w\.-]+@[\w\.-]+\.(com|in|ac\.in|edu|org)$"', r're.match(r"^[\\w\\.-]+@[\\w\\.-]+\\.(com|in|ac\\.in|edu|org)$"')

with open(r"C:\Users\sudeep\OneDrive\Documents\SkillArc-PBL\tools\build_phase3_app.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Escapes fixed!")

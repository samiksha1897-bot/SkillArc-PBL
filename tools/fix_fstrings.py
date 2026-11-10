with open(r"C:\Users\sudeep\OneDrive\Documents\SkillArc-PBL\tools\build_phase3_app.py", "r", encoding="utf-8") as f:
    code = f.read()

# Replace any unescaped \n inside f-strings that shouldn't be newlines in target
code = code.replace(
    'st.markdown(f"### {topic_meta[\'name\']} `[{topic_meta[\'difficulty\']}]`\\n{status_msg}")',
    'st.markdown(f"### {topic_meta[\'name\']} `[{topic_meta[\'difficulty\']}]`\\\\n{status_msg}")'
)

with open(r"C:\Users\sudeep\OneDrive\Documents\SkillArc-PBL\tools\build_phase3_app.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Updated build_phase3_app.py!")

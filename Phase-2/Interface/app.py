
import streamlit as st

st.set_page_config(
    page_title="SkillArc",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 SkillArc")
st.subheader("Your journey to mastering programming starts here!")

st.write(
    "Learn DSA and C++, practise questions, "
    "track your progress, and earn Credit Points."
)

st.divider()

st.header("Your Learning Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Credit Points", 0)

with col2:
    st.metric("Current Streak", "0 days")

with col3:
    st.metric("Topics Completed", "0")

st.divider()

st.subheader("Choose Your Learning Path")

topic = st.selectbox(
    "Select a topic",
    ["Arrays", "Linked Lists", "Stacks", "Queues", "C++ OOP"]
)

st.write("Your selected topic is:", topic)

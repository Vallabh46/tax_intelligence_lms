import streamlit as st
from streamlit_option_menu import option_menu
from gpt_engine import grade_answer
from irs_reference_engine import map_topic_to_irs

st.set_page_config(layout="wide")

# SESSION STATE
if "completed" not in st.session_state:
    st.session_state.completed = []
if "score" not in st.session_state:
    st.session_state.score = 0

selected = option_menu(
    None,
    ["Knowledge Studio", "Assessment", "Progress Intelligence"],
    orientation="horizontal"
)

# ==========================
# KNOWLEDGE STUDIO
# ==========================
if selected == "Knowledge Studio":

    st.title("Income Recognition & Form 1040 Architecture")

    st.header("Chapter 1: Form 1040 Structural Overview")

    st.write("""
Form 1040 is a summary return.
Schedules feed into it:
Schedule 1 (Additional Income)
Schedule B (Interest & Dividends)
Schedule C (Business)
Schedule D (Capital Gains)
Schedule E (Rental & K-1)
""")

    if st.button("Mark Chapter Complete"):
        st.session_state.completed.append("Ch1")

# ==========================
# ASSESSMENT
# ==========================
elif selected == "Assessment":

    question = "Explain constructive receipt doctrine."

    st.subheader(question)
    answer = st.text_area("Your Answer")

    if st.button("Submit for GPT Evaluation"):
        feedback = grade_answer(question, answer)
        st.subheader("Personalised Feedback")
        st.write(feedback)

# ==========================
# PROGRESS INTELLIGENCE
# ==========================
elif selected == "Progress Intelligence":

    st.title("Performance Dashboard")
    st.metric("Chapters Completed", len(st.session_state.completed))

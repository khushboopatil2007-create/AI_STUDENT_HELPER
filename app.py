import streamlit as st

from recommendation import get_recommendation
from data import add_student, get_students


# Page settings
st.set_page_config(
    page_title="AI Student Helper",
    page_icon="🎓"
)

st.title("🎓 AI Student Help Expert System")
st.write("Get study recommendations based on your subject and problem.")


# Student information
st.header("Student Information")

name = st.text_input("Enter your name")


# Subject selection
subject = st.selectbox(
    "Select Subject",
    ["Python", "C++", "AI", "Machine Learning"]
)


# Problem selection
problem = st.selectbox(
    "Select Your Problem",
    ["basics", "functions", "errors", "OOP", "search", "classification"]
)


# Generate recommendation
if st.button("Get Recommendation"):

    if name.strip() == "":
        st.warning("Please enter your name.")

    else:
        recommendation = get_recommendation(subject, problem)

        add_student(name, subject, problem)

        st.success("Recommendation generated!")

        st.subheader("Your Recommendation")
        st.info(recommendation)


# Query history
st.header("Student Query History")

students = get_students()

if len(students) > 0:

    for student in students:
        st.write(
            f"**{student['name']}** → "
            f"{student['subject']} → "
            f"{student['problem']}"
        )

else:
    st.write("No queries recorded yet.")
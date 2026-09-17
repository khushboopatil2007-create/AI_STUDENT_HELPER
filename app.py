import streamlit as st

from recommendation import get_recommendation
from data import add_student, get_students


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="AI Student Helper",
    page_icon="🎓",
    layout="wide"
)


# ==================================================
# CUSTOM CSS
# ==================================================

st.html("""
<style>

    /* Main background */
    .stApp {
        background: #f7f8fc;
    }

    /* Hero section */
    .hero {
        padding: 35px 25px;
        border-radius: 22px;
        text-align: center;
        background: linear-gradient(
            135deg,
            #667eea,
            #764ba2
        );
        color: white;
        margin-bottom: 30px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.10);
    }

    .hero-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .hero-subtitle {
        font-size: 18px;
        opacity: 0.95;
    }

    /* Feature cards */
    .feature-card {
        background: white;
        padding: 22px;
        border-radius: 16px;
        text-align: center;
        border: 1px solid #e5e7eb;
        min-height: 125px;
        box-shadow: 0 3px 12px rgba(0,0,0,0.05);
    }

    .feature-icon {
        font-size: 30px;
    }

    .feature-title {
        font-weight: 700;
        font-size: 17px;
        margin-top: 8px;
    }

    .feature-text {
        color: #666;
        font-size: 14px;
    }

    /* Recommendation */
    .recommendation {
        background: white;
        padding: 28px;
        border-radius: 18px;
        border-left: 7px solid #667eea;
        box-shadow: 0 5px 18px rgba(0,0,0,0.07);
        margin-top: 20px;
    }

    .recommendation-title {
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 10px;
    }

    .recommendation-text {
        font-size: 17px;
        line-height: 1.6;
    }

    /* History */
    .history-card {
        background: white;
        padding: 15px 20px;
        border-radius: 12px;
        margin-bottom: 10px;
        border: 1px solid #e5e7eb;
    }

    /* About card */
    .about-card {
        background: white;
        padding: 25px;
        border-radius: 18px;
        border: 1px solid #e5e7eb;
        line-height: 1.7;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #777;
        padding: 30px 0 10px 0;
        font-size: 14px;
    }

</style>
""")


# ==================================================
# HERO
# ==================================================

st.html("""
<div class="hero">

    <div class="hero-title">
        🎓 AI Student Helper
    </div>

    <div class="hero-subtitle">
        Your intelligent study recommendation assistant
    </div>

</div>
""")


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.title("🎓 AI Student Helper")

    st.write("")

    st.markdown("### 📌 About")

    st.write(
        "This system provides study recommendations "
        "using a rule-based Artificial Intelligence approach."
    )

    st.divider()

    st.markdown("### 🤖 AI Approach")

    st.write("Knowledge Base + Rule-Based Reasoning")

    st.divider()

    st.markdown("### 📚 Subjects")

    st.write("🐍 Python")
    st.write("⚙️ C++")
    st.write("🤖 AI")
    st.write("🧠 Machine Learning")


# ==================================================
# FEATURE CARDS
# ==================================================

st.subheader("✨ What can you do?")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.html("""
    <div class="feature-card">
        <div class="feature-icon">📚</div>
        <div class="feature-title">Choose Subject</div>
        <div class="feature-text">
            Select the subject you are studying.
        </div>
    </div>
    """)

with col2:
    st.html("""
    <div class="feature-card">
        <div class="feature-icon">🔍</div>
        <div class="feature-title">Select Problem</div>
        <div class="feature-text">
            Identify the topic where you need help.
        </div>
    </div>
    """)

with col3:
    st.html("""
    <div class="feature-card">
        <div class="feature-icon">🤖</div>
        <div class="feature-title">AI Reasoning</div>
        <div class="feature-text">
            Rules match your problem with knowledge.
        </div>
    </div>
    """)

with col4:
    st.html("""
    <div class="feature-card">
        <div class="feature-icon">💡</div>
        <div class="feature-title">Get Guidance</div>
        <div class="feature-text">
            Receive a suitable study recommendation.
        </div>
    </div>
    """)


st.write("")
st.divider()


# ==================================================
# TABS
# ==================================================

tab1, tab2, tab3 = st.tabs(
    ["🏠 Get Help", "📋 Query History", "ℹ️ About Project"]
)


# ==================================================
# TAB 1 — GET HELP
# ==================================================

with tab1:

    st.subheader("👋 Get Personalized Study Help")

    st.write(
        "Enter your name and select the subject and problem "
        "you want help with."
    )

    st.write("")

    # Student name
    name = st.text_input(
        "👤 Student Name",
        placeholder="Enter your name..."
    )

    col1, col2 = st.columns(2)

    with col1:

        subject = st.selectbox(
            "📚 Select Subject",
            [
                "Python",
                "C++",
                "AI",
                "Machine Learning"
            ]
        )

    with col2:

        problem = st.selectbox(
            "🔍 Select Your Problem",
            [
                "basics",
                "functions",
                "errors",
                "OOP",
                "search",
                "classification"
            ]
        )

    st.write("")

    # Recommendation button
    if st.button(
        "✨ Generate Recommendation",
        use_container_width=True
    ):

        if name.strip() == "":

            st.warning(
                "Please enter your name before generating a recommendation."
            )

        else:

            recommendation = get_recommendation(
                subject,
                problem
            )

            add_student(
                name,
                subject,
                problem
            )

            st.success(
                "Your recommendation has been generated!"
            )

            st.html(f"""
            <div class="recommendation">

                <div class="recommendation-title">
                    💡 Your Study Recommendation
                </div>

                <p>
                    <b>Subject:</b> {subject}
                </p>

                <p>
                    <b>Area:</b> {problem}
                </p>

                <div class="recommendation-text">
                    {recommendation}
                </div>

            </div>
            """)


# ==================================================
# TAB 2 — QUERY HISTORY
# ==================================================

with tab2:

    st.subheader("📋 Student Query History")

    students = get_students()

    if len(students) > 0:

        st.write(
            f"Total queries in this session: **{len(students)}**"
        )

        st.write("")

        for student in students:

            st.html(f"""
            <div class="history-card">

                👤 <b>{student['name']}</b>

                &nbsp;&nbsp;→&nbsp;&nbsp;

                📚 <b>{student['subject']}</b>

                &nbsp;&nbsp;→&nbsp;&nbsp;

                🔍 <b>{student['problem']}</b>

            </div>
            """)

    else:

        st.info(
            "📝 No study queries yet. "
            "Your previous queries will appear here."
        )


# ==================================================
# TAB 3 — ABOUT
# ==================================================

with tab3:

    st.subheader("ℹ️ About the Project")

    st.html("""
    <div class="about-card">

        <h3>🎓 AI Student Help Expert System</h3>

        <p>
        The AI Student Help Expert System is a simple
        rule-based Artificial Intelligence application
        designed to provide study recommendations to students.
        </p>

        <h4>🤖 How does it work?</h4>

        <p>
        The system accepts the student's subject and
        problem area. It then searches the predefined
        knowledge base and returns a matching recommendation.
        </p>

        <h4>🧠 AI Technique</h4>

        <p>
        Rule-Based Reasoning and Knowledge Representation
        are used to connect student problems with suitable
        study recommendations.
        </p>

        <h4>🛠 Technologies</h4>

        <p>
        Python • Streamlit • Rule-Based AI
        </p>

    </div>
    """)


# ==================================================
# PROJECT STATISTICS
# ==================================================

st.write("")
st.divider()

st.subheader("📊 Project Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📚 Subjects",
        "4",
        border=True
    )

with col2:
    st.metric(
        "🧩 Problem Areas",
        "6",
        border=True
    )

with col3:
    st.metric(
        "🤖 AI Method",
        "Rules",
        border=True
    )

with col4:
    st.metric(
        "💻 Technology",
        "Python",
        border=True
    )


# ==================================================
# FOOTER
# ==================================================

st.html("""
<div class="footer">

    🎓 <b>AI Student Help Expert System</b>

    <br><br>

    Built with Python • Streamlit • Rule-Based AI

    <br>

    AI & ML Academic Project

</div>
""")
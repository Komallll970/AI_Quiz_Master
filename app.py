import streamlit as st

from quiz_chain import generate_quiz
from evaluation_chain import generate_analysis


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Quiz Master",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* =====================================================
       APP BACKGROUND
       ===================================================== */

    .stApp {
        background-color: #0f172a;
    }

    .main .block-container {
        max-width: 1150px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }


    /* =====================================================
       SIDEBAR
       ===================================================== */

    section[data-testid="stSidebar"] {
        background-color: #111827;
        border-right: 1px solid #263244;
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #f8fafc;
    }


    /* =====================================================
       NORMAL TEXT
       ===================================================== */

    p {
        color: #cbd5e1;
        font-size: 15px !important;
    }


    /* =====================================================
       HEADINGS
       ===================================================== */

    h1 {
        color: #f8fafc !important;
        font-size: 32px !important;
        font-weight: 750 !important;
    }

    h2 {
        color: #f8fafc !important;
        font-size: 28px !important;
        font-weight: 700 !important;
    }

    h3 {
        color: #e2e8f0 !important;
        font-size: 21px !important;
        font-weight: 650 !important;
    }


    /* =====================================================
       SIDEBAR TEXT SIZE
       ===================================================== */

    section[data-testid="stSidebar"] p {
        font-size: 14px !important;
    }

    section[data-testid="stSidebar"] label {
        font-size: 14px !important;
    }


    /* =====================================================
       BUTTONS
       ===================================================== */

    .stButton > button {
        width: 100%;
        border-radius: 11px;
        border: none;

        background-color: #4f46e5;
        color: white;

        font-size: 15px;
        font-weight: 700;

        padding: 0.6rem 1rem;

        transition: 0.2s;
    }

    .stButton > button:hover {
        background-color: #6366f1;
        color: white;
        transform: translateY(-1px);
    }


    .stFormSubmitButton > button {
        width: 100%;
        border-radius: 11px;
        border: none;

        background-color: #4f46e5;
        color: white;

        font-size: 15px;
        font-weight: 700;

        padding: 0.7rem 1rem;
    }

    .stFormSubmitButton > button:hover {
        background-color: #6366f1;
        color: white;
    }


    /* =====================================================
       INPUT BOX
       ===================================================== */

    .stTextInput input {
        background-color: #1e293b;
        color: #f8fafc;

        border: 1px solid #334155;

        border-radius: 10px;

        font-size: 14px;
    }

    .stTextInput input:focus {
        border-color: #6366f1;
    }


    /* =====================================================
       SELECT BOX
       ===================================================== */

    div[data-baseweb="select"] > div {
        background-color: #1e293b;
        border-color: #334155;
        border-radius: 10px;
    }


    /* =====================================================
       SLIDER
       ===================================================== */

    .stSlider {
        padding-top: 5px;
    }


    /* =====================================================
       RADIO BUTTONS
       ===================================================== */

    div[role="radiogroup"] {
        gap: 0.5rem;
    }

    div[role="radiogroup"] label {
        background-color: #1e293b;

        border: 1px solid #334155;

        border-radius: 10px;

        padding: 0.6rem 0.9rem;

        transition: 0.2s;
    }

    div[role="radiogroup"] label:hover {
        border-color: #6366f1;
        background-color: #243047;
    }


    /* =====================================================
       METRICS
       ===================================================== */

    div[data-testid="stMetric"] {
        background-color: #1e293b;

        border: 1px solid #334155;

        padding: 1rem;

        border-radius: 14px;
    }

    div[data-testid="stMetricLabel"] {
        color: #94a3b8;
        font-size: 13px !important;
    }

    div[data-testid="stMetricValue"] {
        color: #f8fafc;
        font-size: 24px !important;
    }


    /* =====================================================
       ALERTS
       ===================================================== */

    div[data-testid="stAlert"] {
        border-radius: 11px;
    }


    /* =====================================================
       DIVIDERS
       ===================================================== */

    hr {
        border-color: #263244;
    }


    /* =====================================================
       EXPANDER
       ===================================================== */

    details {
        background-color: #1e293b;

        border: 1px solid #334155;

        border-radius: 11px;
    }


    /* =====================================================
       PROGRESS BAR
       ===================================================== */

    div[data-testid="stProgressBar"] {
        margin-top: 8px;
        margin-bottom: 18px;
    }


    /* =====================================================
       CAPTION
       ===================================================== */

    .stCaption {
        font-size: 14px !important;
    }


    /* =====================================================
       HIDE STREAMLIT DEFAULT ELEMENTS
       ===================================================== */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header[data-testid="stHeader"] {
        background-color: transparent;
    }


    /* =====================================================
       MOBILE
       ===================================================== */

    @media (max-width: 768px) {

        h1 {
            font-size: 30px !important;
        }

        h2 {
            font-size: 24px !important;
        }

        h3 {
            font-size: 19px !important;
        }

        p {
            font-size: 14px !important;
        }

    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SESSION STATE
# ============================================================

if "quiz" not in st.session_state:
    st.session_state.quiz = None

if "submitted" not in st.session_state:
    st.session_state.submitted = False

if "score" not in st.session_state:
    st.session_state.score = 0

if "results" not in st.session_state:
    st.session_state.results = []

if "analysis" not in st.session_state:
    st.session_state.analysis = None


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("⚙️ Quiz Settings")

    st.caption(
        "Customize your quiz before you begin."
    )

    st.divider()


    # ========================================================
    # TOPIC
    # ========================================================

    topic = st.text_input(
        "📚 Topic",
        placeholder="e.g. Machine Learning"
    )


    # ========================================================
    # DIFFICULTY
    # ========================================================

    difficulty = st.selectbox(
        "🎯 Difficulty",
        [
            "Easy",
            "Medium",
            "Hard"
        ]
    )


    # ========================================================
    # NUMBER OF QUESTIONS
    # ========================================================

    num_questions = st.slider(
        "🔢 Number of Questions",
        min_value=1,
        max_value=15,
        value=5
    )


    st.divider()


    # ========================================================
    # GENERATE BUTTON
    # ========================================================

    generate_button = st.button(
        "🚀 Generate Quiz",
        use_container_width=True
    )


    st.divider()


    # ========================================================
    # HOW IT WORKS
    # ========================================================

    st.subheader("💡 How it works")

    st.write("1️⃣ Choose a topic")

    st.write("2️⃣ Select difficulty")

    st.write("3️⃣ Generate your quiz")

    st.write("4️⃣ Answer the questions")

    st.write("5️⃣ Get AI feedback")


# ============================================================
# MAIN HEADER
# ============================================================

st.title("🧠 AI Quiz Master")

st.caption(
    "Test your knowledge. Challenge yourself. "
    "Learn with AI-powered feedback."
)

st.divider()


# ============================================================
# GENERATE QUIZ
# ============================================================

if generate_button:

    if not topic.strip():

        st.warning(
            "⚠️ Please enter a topic first."
        )

    else:

        with st.spinner(
            "🤖 AI is creating your quiz..."
        ):

            try:

                quiz = generate_quiz(
                    topic,
                    difficulty,
                    num_questions
                )


                st.session_state.quiz = quiz

                st.session_state.submitted = False

                st.session_state.score = 0

                st.session_state.results = []

                st.session_state.analysis = None


                st.success(
                    "🎉 Quiz generated successfully!"
                )


            except Exception as e:

                st.error(
                    "Something went wrong while "
                    "generating the quiz."
                )

                st.exception(e)


# ============================================================
# HOME PAGE
# ============================================================

if not st.session_state.quiz:

    st.header(
        "🚀 Start Your Learning Journey"
    )

    st.write(
        "Create a personalized AI-generated quiz "
        "on any topic."
    )

    st.write("")


    # ========================================================
    # FEATURE COLUMNS
    # ========================================================

    col1, col2, col3 = st.columns(3)


    with col1:

        st.subheader(
            "🎯 Choose Your Topic"
        )

        st.write(
            "Practice any subject you want, "
            "such as Python, SQL, Machine Learning "
            "or Data Science."
        )


    with col2:

        st.subheader(
            "🧠 AI Questions"
        )

        st.write(
            "Generate fresh multiple-choice "
            "questions using a Hugging Face LLM."
        )


    with col3:

        st.subheader(
            "🤖 AI Feedback"
        )

        st.write(
            "Get personalized feedback and "
            "recommendations based on your performance."
        )


    st.divider()


    st.info(
        "👈 Configure your quiz from the sidebar "
        "and click **Generate Quiz** to begin."
    )


# ============================================================
# QUIZ PAGE
# ============================================================

else:

    quiz = st.session_state.quiz

    questions = quiz.questions


    # ========================================================
    # QUIZ HEADER
    # ========================================================

    st.header(
        f"📚 {topic}"
    )

    st.caption(
        f"{difficulty} difficulty • "
        f"{len(questions)} questions"
    )

    st.divider()


    # ========================================================
    # QUIZ INFORMATION
    # ========================================================

    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "📖 Topic",
            topic
        )


    with col2:

        st.metric(
            "🎯 Difficulty",
            difficulty
        )


    with col3:

        st.metric(
            "🔢 Questions",
            len(questions)
        )


    st.write("")


    st.progress(
        0,
        text="Answer all questions and submit when you're ready."
    )


    # ========================================================
    # QUIZ FORM
    # ========================================================

    with st.form("quiz_form"):

        user_answers = []


        for i, question in enumerate(questions):

            st.subheader(
                f"Question {i + 1} of {len(questions)}"
            )


            st.write(
                f"**{question.question}**"
            )


            answer = st.radio(
                "Choose your answer:",
                question.options,
                key=f"question_{i}"
            )


            user_answers.append(answer)


            st.divider()


        submitted = st.form_submit_button(
            "🎯 Submit Quiz"
        )


    # ========================================================
    # EVALUATION
    # ========================================================

    if submitted:

        score = 0

        results = []

        incorrect_questions = []


        # ====================================================
        # CHECK ANSWERS
        # ====================================================

        for i, question in enumerate(questions):

            user_answer = user_answers[i]

            correct_answer = question.correct_answer


            if user_answer == correct_answer:

                score += 1


                results.append({

                    "question": question.question,

                    "user_answer": user_answer,

                    "correct_answer": correct_answer,

                    "is_correct": True,

                    "explanation": question.explanation

                })


            else:

                results.append({

                    "question": question.question,

                    "user_answer": user_answer,

                    "correct_answer": correct_answer,

                    "is_correct": False,

                    "explanation": question.explanation

                })


                incorrect_questions.append(

                    f"""
Question: {question.question}

Your answer: {user_answer}

Correct answer: {correct_answer}
"""
                )


        # ====================================================
        # CALCULATE SCORE
        # ====================================================

        total = len(questions)

        percentage = (
            score / total
        ) * 100


        # Save state

        st.session_state.score = score

        st.session_state.results = results

        st.session_state.submitted = True


        # ====================================================
        # RESULT
        # ====================================================

        st.divider()

        st.header(
            "🎉 Quiz Completed!"
        )


        # ====================================================
        # SCORE METRICS
        # ====================================================

        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "🎯 Score",
                f"{score}/{total}"
            )


        with col2:

            st.metric(
                "📊 Percentage",
                f"{percentage:.1f}%"
            )


        with col3:

            st.metric(
                "❌ Incorrect",
                total - score
            )


        # ====================================================
        # PERFORMANCE BAR
        # ====================================================

        st.progress(
            int(percentage),
            text=f"Overall Performance: {percentage:.1f}%"
        )


        # ====================================================
        # QUESTION REVIEW
        # ====================================================

        st.divider()

        st.header(
            "📝 Question Review"
        )

        st.caption(
            "Review your answers and learn from the explanations."
        )


        for i, result in enumerate(results):

            if result["is_correct"]:

                st.success(
                    f"Question {i + 1} — Correct ✅"
                )

            else:

                st.error(
                    f"Question {i + 1} — Incorrect ❌"
                )


            with st.expander(
                f"Question {i + 1}: "
                f"{result['question']}"
            ):

                st.write(
                    f"**Your answer:** "
                    f"{result['user_answer']}"
                )


                if not result["is_correct"]:

                    st.write(
                        f"**Correct answer:** "
                        f"{result['correct_answer']}"
                    )


                st.info(
                    f"💡 {result['explanation']}"
                )


        # ====================================================
        # AI PERFORMANCE ANALYSIS
        # ====================================================

        st.divider()

        st.header(
            "🤖 AI Performance Analysis"
        )

        st.caption(
            "Your AI learning coach analyzes your performance "
            "and suggests areas to improve."
        )


        incorrect_text = "\n".join(
            incorrect_questions
        )


        if not incorrect_text:

            incorrect_text = (
                "The student answered "
                "every question correctly."
            )


        # ====================================================
        # AI CALL
        # ====================================================

        with st.spinner(
            "🤖 AI is analyzing your performance..."
        ):

            try:

                analysis = generate_analysis(

                    topic=topic,

                    score=score,

                    total=total,

                    percentage=percentage,

                    incorrect_questions=incorrect_text

                )


                st.session_state.analysis = analysis


            except Exception as e:

                st.error(
                    "Could not generate AI analysis."
                )

                st.exception(e)


        # ====================================================
        # DISPLAY AI ANALYSIS
        # ====================================================

        if st.session_state.analysis:

            st.success(
                "🤖 AI Learning Coach"
            )

            st.write(
                st.session_state.analysis
            )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🧠 AI Quiz Master • Built with Python, "
    "LangChain, Hugging Face & Streamlit"
)
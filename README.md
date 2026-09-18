<h1 align="center">🧠 AI Quiz Master</h1>

<p align="center">
  <strong>AI-Powered Interactive Quiz Application</strong>
</p>

<p align="center">
  Generate quizzes dynamically using LangChain and Hugging Face,
  evaluate your performance, and receive personalized AI-powered feedback.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/LangChain-Framework-1C3C3C?style=for-the-badge">
  <img src="https://img.shields.io/badge/Hugging%20Face-LLM-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black">
  <img src="https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/Pydantic-Validation-E92063?style=for-the-badge">
</p>

<br>

<p align="center">
  <img src="https://img.shields.io/github/stars/YOUR_USERNAME/AI-Quiz-Master?style=social">
  <img src="https://img.shields.io/github/forks/YOUR_USERNAME/AI-Quiz-Master?style=social">
</p>

---

<h2>📌 Overview</h2>

<p>
<strong>AI Quiz Master</strong> is a Generative AI-powered quiz application built using
<strong>Python, LangChain, Hugging Face, Pydantic, and Streamlit</strong>.
</p>

<p>
The application allows users to select a topic, difficulty level, and number of questions.
An LLM then dynamically generates multiple-choice questions. After the user completes
the quiz, the application evaluates the answers using Python and provides detailed
question-wise explanations along with AI-generated performance feedback.
</p>

---

<h2>✨ Features</h2>

<table>
<tr>
<td width="50%">

<h3>🎯 Custom Quiz Generation</h3>

<p>
Choose any topic and customize the quiz according to your learning requirements.
</p>

<ul>
<li>📚 Custom topic</li>
<li>🎯 Easy / Medium / Hard difficulty</li>
<li>🔢 1–10 questions</li>
</ul>

</td>

<td width="50%">

<h3>🧠 AI-Generated Questions</h3>

<p>
Questions are dynamically generated using a Hugging Face language model through LangChain.
</p>

<ul>
<li>Multiple-choice questions</li>
<li>Correct answers</li>
<li>Explanations</li>
<li>Dynamic generation</li>
</ul>

</td>
</tr>

<tr>
<td>

<h3>📝 Interactive Quiz</h3>

<p>
Users can answer the generated questions directly through the Streamlit interface.
</p>

<ul>
<li>Interactive options</li>
<li>Question numbering</li>
<li>Easy-to-use interface</li>
<li>Submit quiz functionality</li>
</ul>

</td>

<td>

<h3>📊 Automatic Evaluation</h3>

<p>
The application evaluates answers using deterministic Python logic.
</p>

<ul>
<li>Score calculation</li>
<li>Percentage calculation</li>
<li>Correct / incorrect tracking</li>
<li>Question-wise review</li>
</ul>

</td>
</tr>

<tr>
<td>

<h3>💡 Detailed Explanations</h3>

<p>
Each generated question contains an explanation that helps the learner understand
why an answer is correct.
</p>

</td>

<td>

<h3>🤖 AI Performance Analysis</h3>

<p>
After completing the quiz, an AI analysis chain evaluates the learner's performance
and generates personalized learning feedback.
</p>

</td>
</tr>
</table>

---

<h2>🏗️ System Architecture</h2>

<p align="center">

<pre>
                         👤 USER
                           │
                           ▼
                  ┌─────────────────┐
                  │   Streamlit UI  │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │  Quiz Settings  │
                  │                 │
                  │ • Topic         │
                  │ • Difficulty    │
                  │ • Questions     │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ ChatPromptTemplate
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Hugging Face LLM│
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Pydantic Output │
                  │     Parser      │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │  Generated Quiz │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │  User Answers   │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Python Evaluation│
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Score & Feedback│
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Analysis Prompt │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Hugging Face LLM│
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ AI Learning     │
                  │ Feedback        │
                  └─────────────────┘
</pre>

</p>

---

<h2>🔄 Application Workflow</h2>

<table>
<tr>
<th>Step</th>
<th>Process</th>
</tr>

<tr>
<td>1️⃣</td>
<td>User enters a topic.</td>
</tr>

<tr>
<td>2️⃣</td>
<td>User selects the difficulty level.</td>
</tr>

<tr>
<td>3️⃣</td>
<td>User selects the number of questions.</td>
</tr>

<tr>
<td>4️⃣</td>
<td>LangChain constructs the quiz prompt.</td>
</tr>

<tr>
<td>5️⃣</td>
<td>The prompt is sent to the Hugging Face language model.</td>
</tr>

<tr>
<td>6️⃣</td>
<td>The generated response is parsed into structured quiz data using Pydantic.</td>
</tr>

<tr>
<td>7️⃣</td>
<td>The questions are displayed through Streamlit.</td>
</tr>

<tr>
<td>8️⃣</td>
<td>The user selects answers and submits the quiz.</td>
</tr>

<tr>
<td>9️⃣</td>
<td>Python compares user answers with the correct answers.</td>
</tr>

<tr>
<td>🔟</td>
<td>The application calculates the score and percentage.</td>
</tr>

<tr>
<td>1️⃣1️⃣</td>
<td>Question-wise feedback and explanations are displayed.</td>
</tr>

<tr>
<td>1️⃣2️⃣</td>
<td>The performance information is sent to a second AI analysis chain.</td>
</tr>

<tr>
<td>1️⃣3️⃣</td>
<td>The AI generates personalized learning feedback.</td>
</tr>

</table>

---

<h2>🧩 LangChain Implementation</h2>

<h3>1. Prompt Template</h3>

<p>
The application uses LangChain prompt templates to dynamically construct prompts
based on the user's selected topic, difficulty, and number of questions.
</p>

<pre>
User Input
    ↓
Topic + Difficulty + Number of Questions
    ↓
ChatPromptTemplate
    ↓
Generated Prompt
</pre>

<h3>2. Hugging Face Integration</h3>

<p>
Hugging Face is used as the language model provider. LangChain handles the
interaction between the application and the model.
</p>

<pre>
Streamlit
    ↓
LangChain
    ↓
Hugging Face
    ↓
Language Model
    ↓
Generated Response
</pre>

<h3>3. Structured Output</h3>

<p>
The generated quiz needs a predictable structure so that the application can
access individual fields such as the question, options, correct answer, and explanation.
Pydantic is used to define and validate this structure.
</p>

<pre>
Quiz
│
├── questions
│
├── question
├── options
├── correct_answer
└── explanation
</pre>

<h3>4. LangChain Pipeline</h3>

<pre>
Prompt
   │
   ▼
Hugging Face Model
   │
   ▼
Pydantic Output Parser
   │
   ▼
Structured Quiz Object
</pre>

---

<h2>📊 Evaluation Architecture</h2>

<p>
The project separates <strong>LLM-based tasks</strong> from
<strong>deterministic application logic</strong>.
</p>

<table>
<tr>
<th>Task</th>
<th>Handled By</th>
</tr>

<tr>
<td>Question generation</td>
<td>🤖 LLM</td>
</tr>

<tr>
<td>Question explanations</td>
<td>🤖 LLM</td>
</tr>

<tr>
<td>Answer comparison</td>
<td>🐍 Python</td>
</tr>

<tr>
<td>Score calculation</td>
<td>🐍 Python</td>
</tr>

<tr>
<td>Percentage calculation</td>
<td>🐍 Python</td>
</tr>

<tr>
<td>Performance analysis</td>
<td>🤖 LLM</td>
</tr>

<tr>
<td>Learning recommendations</td>
<td>🤖 LLM</td>
</tr>

</table>

<p>
Keeping score calculation in Python makes the evaluation deterministic rather than
depending on an LLM to perform arithmetic or answer matching.
</p>

---

<h2>🛠️ Tech Stack</h2>

<table>
<tr>
<th>Technology</th>
<th>Purpose</th>
</tr>

<tr>
<td>🐍 Python</td>
<td>Application logic and evaluation</td>
</tr>

<tr>
<td>🦜 LangChain</td>
<td>LLM application orchestration</td>
</tr>

<tr>
<td>🤗 Hugging Face</td>
<td>Language model provider</td>
</tr>

<tr>
<td>🎈 Streamlit</td>
<td>Interactive web interface</td>
</tr>

<tr>
<td>🔷 Pydantic</td>
<td>Structured data validation</td>
</tr>

<tr>
<td>🔐 python-dotenv</td>
<td>Environment variable management</td>
</tr>

</table>

---

<h2>📁 Project Structure</h2>

<pre>
AI_QUIZ_MASTER/
│
├── app.py
│
├── quiz_chain.py
│
├── evaluation_chain.py
│
├── requirements.txt
│
├── .env
│
├── .gitignore
│
├── README.md
│
└── screenshots/
    ├── home.png
    ├── quiz.png
    └── results.png
</pre>

<h3>📄 app.py</h3>

<p>
Contains the Streamlit interface, user inputs, quiz display,
answer collection, scoring, results, and AI feedback display.
</p>

<h3>📄 quiz_chain.py</h3>

<p>
Contains the LangChain quiz-generation pipeline, prompt construction,
Hugging Face model integration, and structured output parsing.
</p>

<h3>📄 evaluation_chain.py</h3>

<p>
Contains the LangChain pipeline responsible for generating
AI-based performance analysis and learning feedback.
</p>

---

<h2>⚙️ Installation & Setup</h2>

<h3>1️⃣ Clone the Repository</h3>

<pre>
git clone https://github.com/YOUR_USERNAME/AI-Quiz-Master.git

cd AI-Quiz-Master
</pre>

<h3>2️⃣ Create a Virtual Environment</h3>

<pre>
python -m venv venv
</pre>

<p>Activate the environment on Windows:</p>

<pre>
venv\Scripts\activate
</pre>

<p>On macOS/Linux:</p>

<pre>
source venv/bin/activate
</pre>

<h3>3️⃣ Install Dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

---

<h2>🔐 Environment Variables</h2>

<p>
Create a <code>.env</code> file in the root directory:
</p>

<pre>
HUGGINGFACEHUB_API_TOKEN=your_hugging_face_token
</pre>

<p>
<strong>Important:</strong> Never upload your API token to GitHub.
</p>

<p>
Add the following to <code>.gitignore</code>:
</p>

<pre>
.env
venv/
__pycache__/
*.pyc
</pre>

---

<h2>🚀 Run the Application</h2>

<p>Run the following command from the project directory:</p>

<pre>
python -m streamlit run app.py
</pre>

<p>
The application will open at:
</p>

<pre>
http://localhost:8501
</pre>

---

<h2>🎮 How to Use</h2>

<ol>
<li>Enter a topic such as <strong>Machine Learning</strong>.</li>
<li>Select the desired difficulty.</li>
<li>Select the number of questions.</li>
<li>Click <strong>🚀 Generate Quiz</strong>.</li>
<li>Answer each multiple-choice question.</li>
<li>Click <strong>🎯 Submit Quiz</strong>.</li>
<li>View your score and percentage.</li>
<li>Review incorrect answers and explanations.</li>
<li>Read your personalized AI performance analysis.</li>
</ol>

---

<h2>🖥️ Application Screenshots</h2>

<h3>🏠 Home Page</h3>

<p align="center">
  <img src="screenshots/home.png" width="850">
</p>

<h3>📝 Quiz Interface</h3>

<p align="center">
  <img src="screenshots/quiz.png" width="850">
</p>

<h3>📊 Results & AI Feedback</h3>

<p align="center">
  <img src="screenshots/results.png" width="850">
</p>

---

<h2>💡 Example</h2>

<table>
<tr>
<td><strong>Topic</strong></td>
<td>Machine Learning</td>
</tr>

<tr>
<td><strong>Difficulty</strong></td>
<td>Medium</td>
</tr>

<tr>
<td><strong>Questions</strong></td>
<td>5</td>
</tr>

<tr>
<td><strong>Result</strong></td>
<td>4 / 5</td>
</tr>

<tr>
<td><strong>Percentage</strong></td>
<td>80%</td>
</tr>

</table>

<p>
After evaluation, the AI Learning Coach analyzes the incorrect answers
and provides areas for improvement and learning recommendations.
</p>

---

<h2>🎯 Project Objectives</h2>

<ul>
<li>Build a practical Generative AI application.</li>
<li>Integrate Hugging Face models with LangChain.</li>
<li>Practice prompt engineering.</li>
<li>Implement structured LLM output.</li>
<li>Use Pydantic for data validation.</li>
<li>Build an interactive Streamlit application.</li>
<li>Combine LLM capabilities with deterministic Python logic.</li>
<li>Generate personalized AI-based learning feedback.</li>
</ul>

---

<h2>🚧 Future Enhancements</h2>

<ul>
<li>⏱️ Add a quiz timer.</li>
<li>➡️ Display one question at a time.</li>
<li>📈 Add performance history.</li>
<li>👤 Add user accounts.</li>
<li>🏆 Add a leaderboard.</li>
<li>📚 Add more question types.</li>
<li>🎚️ Implement adaptive difficulty.</li>
<li>📊 Add topic-wise performance tracking.</li>
<li>📄 Generate downloadable performance reports.</li>
<li>💾 Add persistent database storage.</li>
<li>🌐 Deploy the application publicly.</li>
</ul>

---

<h2>🧠 Key Learning Outcomes</h2>

<pre>
Python
  ↓
Streamlit
  ↓
LangChain
  ↓
Prompt Engineering
  ↓
Hugging Face LLM
  ↓
Structured Output
  ↓
Pydantic
  ↓
Python Evaluation
  ↓
AI Performance Analysis
</pre>

<p>
This project demonstrates how LangChain and LLMs can be integrated with
traditional Python application logic to build a practical Generative AI application.
</p>

---

<h2>🔮 Future Vision</h2>

<p>
The long-term goal of <strong>AI Quiz Master</strong> is to evolve into a
personalized AI learning assistant that can dynamically assess a learner's
knowledge, identify knowledge gaps, and continuously adapt quizzes and
learning recommendations based on performance.
</p>

---

<h2>👩‍💻 Author</h2>

<p>
<strong>Komal Verma</strong>
</p>

<p>
Data Science • Machine Learning • Generative AI
</p>

<p>
Interested in building practical AI and Machine Learning applications
using Python, LLMs, and modern AI frameworks.
</p>

---

<p align="center">
  <strong>⭐ If you find this project useful, consider giving the repository a star!</strong>
</p>

<p align="center">
  Built with ❤️ using Python, LangChain, Hugging Face & Streamlit
</p>

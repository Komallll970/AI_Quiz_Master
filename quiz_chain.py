from dotenv import load_dotenv

from langchain_huggingface import (
    HuggingFaceEndpoint,
    ChatHuggingFace
)

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from quiz_schema import Quiz


load_dotenv()


# -----------------------------
# Hugging Face model
# -----------------------------

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation",
    max_new_tokens=2048,
    temperature=0.2
)

model = ChatHuggingFace(llm=llm)


# -----------------------------
# Pydantic Output Parser
# -----------------------------

parser = PydanticOutputParser(
    pydantic_object=Quiz
)


# -----------------------------
# Prompt
# -----------------------------

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a quiz generation system.

Create a multiple-choice quiz about:
Topic: {topic}
Difficulty: {difficulty}

You MUST generate exactly {num_questions} complete questions.

Each question MUST contain:
- question
- options
- correct_answer
- explanation

Each question MUST contain exactly 4 options.

The correct_answer MUST be exactly one of those 4 options.

IMPORTANT:
- Never create an empty question object.
- Never use {{}}
- Never stop before completing all questions.
- Do not add extra questions.
- Do not repeat questions.

Return ONLY valid JSON.
Do not use markdown.
Do not use ```json.
Do not add any explanation outside the JSON.

The JSON must follow this structure:

{{
    "questions": [
        {{
            "question": "Example question",
            "options": [
                "Option A",
                "Option B",
                "Option C",
                "Option D"
            ],
            "correct_answer": "Option A",
            "explanation": "Explanation of the answer"
        }}
    ]
}}

Generate exactly {num_questions} questions.
"""
    ),
    (
        "human",
        "Generate the complete quiz now."
    )
])

# -----------------------------
# Add parser instructions
# -----------------------------

prompt = prompt.partial(
    format_instructions=parser.get_format_instructions()
)


# -----------------------------
# Chain
# -----------------------------

quiz_chain = prompt | model | parser


# -----------------------------
# Function
# -----------------------------

def generate_quiz(
    topic,
    difficulty,
    num_questions
):

    result = quiz_chain.invoke({
        "topic": topic,
        "difficulty": difficulty,
        "num_questions": num_questions
    })

    return result
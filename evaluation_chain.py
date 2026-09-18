from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()


# -----------------------------
# Hugging Face Model
# -----------------------------

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)


# -----------------------------
# Analysis Prompt
# -----------------------------

analysis_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an AI learning assistant.

Analyze a student's quiz performance.

Give useful and encouraging feedback.

Include:

1. Overall performance
2. Strengths
3. Weak areas
4. Topics the student should revise
5. A short recommendation for further learning

Keep the response clear and concise.
"""
    ),
    (
        "human",
        """
Topic: {topic}

Score: {score}/{total}

Percentage: {percentage}%

Incorrect questions:
{incorrect_questions}

Generate the student's performance analysis.
"""
    )
])


# -----------------------------
# Chain
# -----------------------------

analysis_chain = (
    analysis_prompt
    | model
    | StrOutputParser()
)


def generate_analysis(
    topic,
    score,
    total,
    percentage,
    incorrect_questions
):

    result = analysis_chain.invoke({
        "topic": topic,
        "score": score,
        "total": total,
        "percentage": percentage,
        "incorrect_questions": incorrect_questions
    })

    return result
from pydantic import BaseModel, Field
from typing import List


class Question(BaseModel):
    question: str = Field(description="The quiz question")

    options: List[str] = Field(
        description="Exactly four multiple-choice options"
    )

    correct_answer: str = Field(
        description="The correct answer. It must exactly match one of the options."
    )

    explanation: str = Field(
        description="A short explanation of why the correct answer is correct"
    )


class Quiz(BaseModel):
    questions: List[Question]
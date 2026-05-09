from pydantic import BaseModel, Field


class StudentResponse(BaseModel):
    """A student's response to an assessment question."""

    answer: str = Field(description="The student's answer text")
    question_id: int = Field(description="Index of the question being answered")


class Evaluation(BaseModel):
    """Evaluation of a student's response."""

    score: int = Field(ge=0, le=10, description="Score from 0-10")
    feedback: str = Field(description="Constructive feedback for the student")
    concepts_demonstrated: list[str] = Field(
        default_factory=list,
        description="Concepts the student demonstrated understanding of",
    )
    concepts_missing: list[str] = Field(
        default_factory=list,
        description="Concepts the student failed to demonstrate",
    )

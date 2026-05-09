from crewai import Agent

from config.settings import settings


def create_difficulty_adjuster() -> Agent:
    """Create the Difficulty Adjuster agent.

    This agent analyses student performance and adjusts
    the difficulty level for subsequent questions.
    """
    return Agent(
        role="Difficulty Adjuster",
        goal=(
            "Analyse student performance across responses and determine the optimal "
            "difficulty level for the next question. Increase difficulty when the student "
            "demonstrates strong understanding, decrease when they struggle."
        ),
        backstory=(
            "You are an adaptive learning specialist who understands how to keep students "
            "in their zone of proximal development. You make data-driven decisions about "
            "difficulty adjustments based on scores and demonstrated concepts."
        ),
        verbose=True,
        allow_delegation=False,
        llm=f"ollama/{settings.ollama_model}",
    )

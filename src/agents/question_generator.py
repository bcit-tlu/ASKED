from crewai import Agent

from config.settings import settings


def create_question_generator() -> Agent:
    """Create the Question Generator agent.

    This agent is responsible for generating assessment questions
    at the appropriate difficulty level for the given subject.
    """
    return Agent(
        role="Question Generator",
        goal=(
            "Generate clear, educational assessment questions based on the provided "
            "study material summary at the specified difficulty level that test "
            "genuine understanding of the material."
        ),
        backstory=(
            "You are an experienced educator who specialises in crafting questions that "
            "reveal depth of understanding. You create questions grounded in specific "
            "course materials — never fabricating content beyond what the materials cover. "
            "Your questions are clear, unambiguous, and appropriately challenging for "
            "the given difficulty level."
        ),
        verbose=True,
        allow_delegation=False,
        llm=f"ollama/{settings.ollama_model}",
    )

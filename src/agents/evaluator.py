from crewai import Agent

from config.settings import settings


def create_evaluator() -> Agent:
    """Create the Evaluator agent.

    This agent assesses student responses, providing scores
    and constructive feedback.
    """
    return Agent(
        role="Response Evaluator",
        goal=(
            "Accurately evaluate student responses against the provided study material "
            "by identifying demonstrated knowledge, misconceptions, and gaps in "
            "understanding. Provide constructive feedback."
        ),
        backstory=(
            "You are a fair and thorough assessor. You evaluate responses based on "
            "the source study material — checking accuracy, depth of understanding, "
            "and clarity of explanation. You never penalise students for omitting "
            "content that is not in the material. You always provide helpful feedback "
            "that guides the student toward better understanding."
        ),
        verbose=True,
        allow_delegation=False,
        llm=f"ollama/{settings.ollama_model}",
    )

from crewai import Agent
from crewai_tools import DirectoryReadTool, FileReadTool

from config.settings import settings


def create_study_agent() -> Agent:
    """Create the Study Agent.

    This agent reads all files in the configured materials directory
    and produces a structured knowledge summary (key topics, concepts,
    facts) for downstream agents to use as context.
    """
    directory_tool = DirectoryReadTool(directory=settings.materials_dir)
    file_tool = FileReadTool()

    return Agent(
        role="Study Material Analyst",
        goal=(
            "Read and analyse all course materials in the provided directory. "
            "Produce a comprehensive, structured knowledge summary that includes "
            "key topics, core concepts, important facts, and relationships between ideas."
        ),
        backstory=(
            "You are a meticulous academic researcher who excels at distilling "
            "large volumes of educational content into clear, well-organised summaries. "
            "You never fabricate information — you only summarise what is explicitly "
            "present in the source materials."
        ),
        tools=[directory_tool, file_tool],
        verbose=True,
        allow_delegation=False,
        llm=f"ollama/{settings.ollama_model}",
    )

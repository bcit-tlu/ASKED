"""
Integration tests for agents.
These require Ollama to be running with a model available.
Run with: pytest tests/test_agents.py -m integration
"""
import pytest

from agents.question_generator import create_question_generator
from agents.evaluator import create_evaluator
from agents.difficulty_adjuster import create_difficulty_adjuster
from agents.study_agent import create_study_agent


@pytest.mark.integration
def test_question_generator_creates_agent():
    agent = create_question_generator()
    assert agent.role == "Question Generator"


@pytest.mark.integration
def test_question_generator_references_material_context():
    agent = create_question_generator()
    assert "study material" in agent.goal.lower()


@pytest.mark.integration
def test_evaluator_creates_agent():
    agent = create_evaluator()
    assert agent.role == "Response Evaluator"


@pytest.mark.integration
def test_evaluator_references_material_context():
    agent = create_evaluator()
    assert "study material" in agent.goal.lower()


@pytest.mark.integration
def test_difficulty_adjuster_creates_agent():
    agent = create_difficulty_adjuster()
    assert agent.role == "Difficulty Adjuster"


@pytest.mark.integration
def test_study_agent_creates_agent():
    agent = create_study_agent()
    assert agent.role == "Study Material Analyst"


@pytest.mark.integration
def test_study_agent_has_tools():
    agent = create_study_agent()
    tool_names = [t.name for t in agent.tools]
    assert any("directory" in name.lower() or "list" in name.lower() for name in tool_names)
    assert any("read" in name.lower() or "file" in name.lower() for name in tool_names)

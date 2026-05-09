"""
Integration tests for agents.
These require Ollama to be running with a model available.
Run with: pytest tests/test_agents.py -m integration
"""
import pytest

from agents.question_generator import create_question_generator
from agents.evaluator import create_evaluator
from agents.difficulty_adjuster import create_difficulty_adjuster


@pytest.mark.integration
def test_question_generator_creates_agent():
    agent = create_question_generator()
    assert agent.role == "Question Generator"


@pytest.mark.integration
def test_evaluator_creates_agent():
    agent = create_evaluator()
    assert agent.role == "Response Evaluator"


@pytest.mark.integration
def test_difficulty_adjuster_creates_agent():
    agent = create_difficulty_adjuster()
    assert agent.role == "Difficulty Adjuster"

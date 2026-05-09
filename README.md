# ASKED

Assessment of Student Knowledge through Evaluative Dialogue

A proof-of-concept prototype that uses multiple AI agents to conduct conversational knowledge assessments with students.

## Architecture

```
┌─────────────────────────────────────────────┐
│              Streamlit Frontend              │
├─────────────────────────────────────────────┤
│              CrewAI Orchestrator             │
├──────────┬──────────┬──────────┬────────────┤
│  Study   │ Question │ Evaluator│ Difficulty │
│  Agent   │ Generator│  Agent   │ Adjuster   │
├──────────┴──────────┴──────────┴────────────┤
│         Ollama (Local LLM)                  │
├─────────────────────────────────────────────┤
│         materials/ (course content)         │
└─────────────────────────────────────────────┘
```

## Tech Stack

- **LLM**: Ollama (local inference)
- **Backend**: CrewAI 0.108 + Pydantic 2
- **Frontend**: Streamlit
- **Deployment**: Rancher, Flux
- **Version Control**: GitHub

## Getting Started

### Prerequisites

- Python 3.11 or 3.12 (CrewAI does not support Python 3.13+)
- [Ollama](https://ollama.ai/) installed and running
- A model pulled (e.g., `ollama pull qwen3.5:cloud`)

### Installation

```bash
# Clone the repository
git clone <repo-url>
cd ASKED

# Create virtual environment (use python3.11 or python3.12)
python3.11 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Copy the example environment variables into a `.env` file at the project root:

```bash
# .env
ASSESS_OLLAMA_BASE_URL=http://localhost:11434
ASSESS_OLLAMA_MODEL=qwen3.5:cloud
ASSESS_SUBJECT_DOMAIN=computer science
ASSESS_MAX_QUESTIONS_PER_SESSION=10
ASSESS_INITIAL_DIFFICULTY=3
ASSESS_MATERIALS_DIR=materials
```

### Running the App

```bash
# Make sure Ollama is running
ollama serve

# Start the Streamlit frontend
streamlit run src/app.py
```

### Running Tests

```bash
pytest
```

## Project Structure

```
ASKED/
├── src/
│   ├── __init__.py
│   ├── app.py                  # Streamlit frontend
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── study_agent.py
│   │   ├── question_generator.py
│   │   ├── evaluator.py
│   │   └── difficulty_adjuster.py
│   ├── crew/
│   │   ├── __init__.py
│   │   └── assessment_crew.py  # CrewAI orchestration
│   ├── models/
│   │   ├── __init__.py
│   │   ├── question.py
│   │   ├── response.py
│   │   └── session.py
│   └── config/
│       ├── __init__.py
│       └── settings.py
├── tests/
│   ├── __init__.py
│   ├── test_agents.py
│   └── test_models.py
├── materials/              # Drop course content here
│   └── sample.md
├── docs/
│   └── design.md
├── conftest.py             # Adds src/ to sys.path for pytest
├── requirements.txt
├── proposal.md
├── README.md
├── LICENSE
└── .gitignore
```

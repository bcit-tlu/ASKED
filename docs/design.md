# System Design

## Agent Roles

### 1. Question Generator
- **Responsibility**: Generates assessment questions at the appropriate difficulty level
- **Input**: Subject domain, difficulty level, session history
- **Output**: A clear, targeted question

### 2. Response Evaluator
- **Responsibility**: Evaluates student answers for correctness and depth
- **Input**: The question asked and the student's response
- **Output**: Score (0-10), feedback, concepts demonstrated/missing

### 3. Difficulty Adjuster
- **Responsibility**: Adjusts difficulty based on student performance
- **Input**: Recent scores and session state
- **Output**: New difficulty level (1-5)

## Communication Flow

```
[Student] → answer → [Evaluator] → score → [Difficulty Adjuster] → level → [Question Generator] → question → [Student]
```

## Session Lifecycle

1. Session starts at configured initial difficulty
2. Question Generator creates first question
3. Student provides answer
4. Evaluator scores and provides feedback
5. After 2+ questions, Difficulty Adjuster recalibrates
6. Loop until max questions reached
7. Final summary presented

## Data Models

All inter-agent communication uses Pydantic models for type safety and validation.
See `src/models/` for schema definitions.

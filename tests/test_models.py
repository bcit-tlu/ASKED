from models.question import Question
from models.response import StudentResponse, Evaluation
from models.session import AssessmentSession, QuestionRecord


def test_question_creation():
    q = Question(
        content="What is polymorphism in OOP?",
        topic="object-oriented programming",
        difficulty=3,
        expected_concepts=["inheritance", "method overriding"],
    )
    assert q.difficulty == 3
    assert len(q.expected_concepts) == 2


def test_evaluation_score_bounds():
    e = Evaluation(score=8, feedback="Good answer")
    assert 0 <= e.score <= 10


def test_session_average_score():
    session = AssessmentSession(subject="computer science")
    record = QuestionRecord(
        question=Question(content="Test?", topic="test", difficulty=1),
        response=StudentResponse(answer="answer", question_id=0),
        evaluation=Evaluation(score=7, feedback="Good"),
    )
    session.history.append(record)
    assert session.average_score == 7.0
    assert session.questions_asked == 1


def test_empty_session():
    session = AssessmentSession(subject="computer science")
    assert session.questions_asked == 0
    assert session.average_score == 0.0
    assert session.is_complete is False


def test_session_material_summary_default_empty():
    session = AssessmentSession(subject="computer science")
    assert session.material_summary == ""


def test_session_material_summary_stored():
    session = AssessmentSession(subject="computer science")
    session.material_summary = "Key topics: OOP, recursion, data structures"
    assert "OOP" in session.material_summary

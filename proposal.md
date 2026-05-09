Design and Evaluation of a Conversational Assessment System for Student Knowledge Testing  


Background / Context

Traditional assessment methods such as written exams and standardised quizzes provide only a static snapshot of student understanding, offering limited adaptability to individual learner needs. Recent advances in large language models (LLMs) and multi-agent architectures have opened new possibilities for creating intelligent, conversational systems that can dynamically assess knowledge through dialogue. By combining adaptive questioning with real-time difficulty adjustment, such systems have the potential to deliver more personalised and engaging assessments. However, research into practical, multi-agent approaches for educational assessment remains in its early stages, and there is a need for proof-of-concept prototypes that explore this design space.

Proposed aim 

This project aims to design and evaluate a basic prototype of a multi-agent conversational assessment system that tests student knowledge through interactive questioning. The prototype will serve as proof of concept that can be expanded in future work. 

Objectives

1. Design a multi-agent architecture where specialised agents collaborate to generate and deliver assessment questions.
2. Implement a working prototype that conducts conversational knowledge assessments with students.

Scope

The project will focus on building a proof-of-concept prototype targeting a single subject domain. It will cover the design of the multi-agent system, implementation of a basic conversational interface, and a small-scale user evaluation. Production-level deployment, scalability, and integration with institutional learning management systems are outside the scope of this work.

Methodology

1. **Research** – Review existing literature on multi-agent systems and conversational AI in education.
2. **Design** – Define agent roles, communication protocols, and the overall system architecture.
3. **Implementation** – Build the prototype using an LLM API and a multi-agent framework.
4. **Evaluation** – Demonstrate and assess the prototype against the defined objectives to validate the proof of concept.

Deliverables

- A working prototype application demonstrating multi-agent conversational assessment.
- Supporting documentation including system design and a final project report.

Tools and Technologies

- **Language Model** – Ollama (local LLM inference)
- **Backend** – Pydantic, CrewAI or LangGraph
- **Frontend** – Streamlit or Gradio
- **Deployment** – Rancher, Flux
- **Version Control** – GitHub
- **Documentation** – Markdown

Expected Learning Outcomes

- Practical understanding of multi-agent system design and orchestration.
- Experience building conversational AI applications using LLMs.
- Familiarity with deployment tools such as Rancher and Flux.
- Ability to evaluate a proof-of-concept prototype and identify areas for improvement.


Future Work

- Extend the system to support multiple subject domains.
- Introduce adaptive difficulty adjustment based on student responses.
- Integrate with institutional learning management systems (D2L).
- Conduct formal user studies to evaluate assessment effectiveness at scale.
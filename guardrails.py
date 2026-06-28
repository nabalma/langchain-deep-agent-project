ALLOWED_KEYWORDS = [
    "langchain",
    "langgraph",
    "deep agents",
    "deepagents",
    "agent",
    "agents",
    "tool",
    "tools",
    "skill",
    "skills",
    "memory",
    "state",
    "checkpoint",
    "checkpointer",
    "backend",
    "rag",
    "retriever",
    "vector store",
    "llm",
]


REFUSAL_MESSAGE = """
Je suis spécialisé dans LangChain, LangGraph et Deep Agents.
Je ne peux donc pas répondre à cette demande hors périmètre.
Pose-moi une question liée aux agents IA, LangChain, LangGraph, Tools, Skills, Memory, RAG ou Deep Agents.
"""


def is_question_allowed(question: str) -> bool:
    question_lower = question.lower()

    return any(keyword in question_lower for keyword in ALLOWED_KEYWORDS)
from dotenv import load_dotenv
from deepagents import create_deep_agent
from deepagents.backends import FilesystemBackend
from langgraph.checkpoint.memory import InMemorySaver

from tools.search_tool import internet_search
from tools.file_tool import save_text_file
from tools.email_tool import send_email

load_dotenv()

backend = FilesystemBackend(
    root_dir=".",
    virtual_mode=True,
)

checkpointer = InMemorySaver()

agent = create_deep_agent(
    model="openai:gpt-4o-mini",
    tools=[
        internet_search,
        save_text_file,
        send_email,
    ],
    backend=backend,
    checkpointer=checkpointer,
    memory=[
        "/AGENTS.md",
    ],
    skills=[
        "/skills/research-report",
        "/skills/email-sender",
        "/skills/save-report",
    ],
    interrupt_on={
        "send_email": {
            "allowed_decisions": ["approve", "edit", "reject"]
        }
    },
    system_prompt="""
Tu es un assistant IA de recherche.

Utilise les Skills disponibles lorsque la demande correspond à une compétence.
Utilise les Tools uniquement lorsqu'une action externe est nécessaire.

Avant tout envoi d'email, attendre une validation humaine.
Réponds en français simple.
""",
)
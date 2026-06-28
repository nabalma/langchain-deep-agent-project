import pprint
from uuid import uuid4
from langgraph.types import Command

from agent import agent
from guardrails import is_question_allowed, REFUSAL_MESSAGE


thread_id = str(uuid4())

config = {
    "configurable": {
        "thread_id": thread_id,
    }
}

question = input("Pose ta question : ")

if not is_question_allowed(question):
    print(REFUSAL_MESSAGE)
    exit()

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": question,
            }
        ]
    },
    config=config,
)

print(result["messages"][-1].content)
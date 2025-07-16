import uvicorn

from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import AgentCapabilities, AgentCard, AgentSkill, AgentExtension

from hello_world.agent import HelloWorldAgentExecutor


def run():
    agent_card = AgentCard(
        name="Hello World Agent",
        description="Just a hello world agent",
        url="http://localhost:8000/",
        version="1.0.0",
        defaultInputModes=["text"],
        defaultOutputModes=["text"],
        capabilities=AgentCapabilities(
            extensions=[
                AgentExtension(uri="beeai_ui", params={"ui_type": "chat"}),
                AgentExtension(uri="required_env", params={"env": [{"name": "HELLO_TEMPLATE", "required": False}]}),
            ]
        ),
        skills=[AgentSkill(id="hello_world", name="hello_world", description="returns hello world", tags=["hello"])],
    )

    request_handler = DefaultRequestHandler(agent_executor=HelloWorldAgentExecutor(), task_store=InMemoryTaskStore())
    server = A2AStarletteApplication(agent_card=agent_card, http_handler=request_handler)
    uvicorn.run(server.build(), host="0.0.0.0", port=8000)


if __name__ == "__main__":
    run()

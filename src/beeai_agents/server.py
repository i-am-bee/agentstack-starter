from acp.server.highlevel import Context
from beeai_sdk.providers.agent import Server
from beeai_sdk.schemas.text import TextInput, TextOutput

from beeai_agents.configuration import Configuration

server = Server("beeai-agents")

@server.agent()
async def example_agent(input: TextInput, ctx: Context) -> TextOutput:
    """TODO: Your implementation goes here."""
    return TextOutput(text=Configuration().hello_template % input.text)

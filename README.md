> 🚧 **Disclaimer**
>
> The current MCP based implementation should be treated as temporary and exploratory. It's main purpose is to enable
> integration of various agents into the platform and to explore underlying protocols, transports and possible
> multi-agent
> patterns. In Q2 2025, we expect to rebuild the SDK from the ground up.

# Agent template

This is an example template for a python agent that can be used in the beeai platform.

To get started, click **Use this template** or fork this repository.

## Pre-requisites

- Python 3.11 or higher
- UV package manager: https://docs.astral.sh/uv/

## Implementing agent

1. Install dependencies using `uv sync`

2. Modify the source code in [src/beeai_agents/server.py](src/beeai_agents/server.py) to add your agent implementation
   in any agentic framework you like. You can add as many agents as you like.

## Running agents locally

You can experiment with the agents locally by running it directly:

```sh
uv run server
```

You'll get an output similar to:

```
INFO:     Started server process [86448]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Your agents should now be started on http://localhost:8000, you can now list agents using the beeai CLI:

```sh
beeai list
```

And run your agent:

```sh
beeai run example-agent "Your Name"
```

## Adding agents to the beeai platform

Now you may want to add your agents to your collection in beeai. You can do that locally or from GitHub.
Let's break it down.

### Locally

The agents are automatically registered to the platform when you run them locally using `uv run server`. In this
setup, the beeai platform will not manage the agent lifecycle (start / stop the agent) and it cannot provide
environment variables from `beeai env list`. To supply environment variables, provide them on the command line when
starting server:

```shell
env MY_VAR=VALUE uv run server
```

#### Add managed agent from GitHub

If you want to share your agent with others using the beeai platform, the easiest way is to use a GitHub link to
your repository you created with the template:

1. Create [agent.yaml](agent.yaml) manifest with the agent name and metadata
2. Add agent:
   ```sh
   beeai add https://github.com/i-am-bee/beeai-agent-starter-py
   ```

> Note: To manage versions properly and prevent automatic updates or breaking changes we recommend creating a tag
> (for example `agents-v0.0.1`)
>   - Specify tag when adding agent: `beeai add https://github.com/org/repo@agents-v0.0.1`
>   - To release new version - create a new tag
>   - To update the agent in beeai you'll need to `beeai remove <agent-name>` and add it again.

## Troubleshooting

**How do I know the status of the agent?**

You can use `beeai list` to see whether the provider is initializing / ready or in an error state.
For local provider you can see agent logs directly in the terminal after `uv run server`, for managed use
`beeai logs <ID>`.

You can also inspect the beeai server logs for further details (typically in `/opt/homebrew/var/log/beeai-server.log`)
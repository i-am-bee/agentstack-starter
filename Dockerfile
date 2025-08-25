FROM python:3.13-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:0.7.15 /uv /bin/

ENV UV_LINK_MODE=copy \
    PRODUCTION_MODE=true

ADD . /app
WORKDIR /app

RUN uv sync --no-cache --locked --link-mode copy

ENV PRODUCTION_MODE=True \
    PATH="/app/.venv/bin:$PATH" \
    HOME=/tmp

CMD ["uv", "run", "--no-sync", "server"]

FROM python:3.13-slim
WORKDIR /app
COPY . .
RUN --mount=type=cache,target=/tmp/.cache/uv \
    --mount=type=bind,from=ghcr.io/astral-sh/uv:0.9.5,source=/uv,target=/bin/uv \
    UV_COMPILE_BYTECODE=1 HOME=/tmp uv sync --no-cache --link-mode copy
ENV PRODUCTION_MODE=True
CMD ["/app/.venv/bin/server"]

FROM python:3.13-slim
COPY --from=ghcr.io/astral-sh/uv:0.9.5 /uv /bin/uv
WORKDIR /app
COPY . .
RUN UV_COMPILE_BYTECODE=1 HOME=/tmp uv sync --no-cache --link-mode copy
ENV PRODUCTION_MODE=True
CMD ["/app/.venv/bin/server"]

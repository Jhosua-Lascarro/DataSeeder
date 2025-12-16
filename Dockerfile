FROM ghcr.io/astral-sh/uv:python3.14-trixie

WORKDIR /app
COPY . /app

# Skip dev dependencies in final image
RUN uv sync --locked --no-dev

CMD ["uv", "run", "src/dataseeder/pipeline.py"]

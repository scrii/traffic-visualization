FROM ghcr.io/astral-sh/uv:bookworm-slim

WORKDIR /app/
COPY ./ ./

RUN uv sync --frozen

CMD ["uv", "run", "--", "waitress-serve", "--call", "src.main:main"]

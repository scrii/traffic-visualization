# Project Setup Guide

You should be able to access the services with these URLs:

- Back end: http://localhost:8080
- Website: http://localhost:4713

## Docker (Recommended)

This command will launch the services from [`compose.yaml`](`/compose.yaml`):

```shell
docker compose up --build
```

## Manual Setup (Fallback)

### Requirements

- [uv](https://github.com/astral-sh/uv) (Python package manager)
- [pnpm](https://github.com/pnpm/pnpm) (Node.js package manager)

### Back End Server

You will need to run this command from the `server/` directory:

```shell
uv run -- waitress-serve --call src.main:main
```

### CSV Parser

After you&CloseCurlyQuote;ve launched the back end, you need to launch the CSV
parser.

Run this command from the `csv-parser/` directory:

```shell
uv run src/main.py
```

### Front End

Now, you can execute these commands from the `visualization/` directory:

```shell
pnpm install
pnpm run build
pnpm run preview
```

# Project Setup

This guide covers environment setup for **Gen Ai Python** on Windows, macOS, and Linux.

## Prerequisites

- **Python 3.10+** — verify with:

```bash
python --version
```

- **Git** (optional) — for cloning the repo

---

## Quick Start (Windows)

```cmd
cd "D:\projects\Gen Ai Python"
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Quick Start (macOS / Linux)

```bash
cd /path/to/Gen-Ai-Python
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## What is uv?

[uv](https://docs.astral.sh/uv/) is a fast Python package and project manager from Astral. It can replace **pip** and **venv** for day-to-day work:

| Tool | uv equivalent |
|------|---------------|
| `python -m venv` | `uv venv` |
| `pip install` | `uv pip install` |
| `pip install -r requirements.txt` | `uv pip install -r requirements.txt` |

uv is optional but recommended — installs are typically much faster.

---

## Install uv

### macOS / Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows (PowerShell)

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

uv installs to:

- **Windows:** `%USERPROFILE%\.local\bin\uv.exe`
- **macOS / Linux:** `~/.local/bin/uv`

### Verify installation

**Important:** After installing uv, **close and reopen your terminal** (or restart Cursor). The installer updates PATH, but existing sessions keep the old PATH.

```bash
uv --version
# Example output: uv 0.11.17
```

If `uv` is still not found in the current session:

**Windows (CMD — temporary fix for this session):**

```cmd
set PATH=%USERPROFILE%\.local\bin;%PATH%
uv --version
```

**Windows (run directly without PATH):**

```cmd
"%USERPROFILE%\.local\bin\uv.exe" --version
```

**macOS / Linux (temporary fix for this session):**

```bash
export PATH="$HOME/.local/bin:$PATH"
uv --version
```

---

## Create a Virtual Environment

### With Python (standard)

**Windows:**

```cmd
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
python -m venv .venv
source .venv/bin/activate
```

When active, your prompt shows `(.venv)`.

### With uv

**Windows:**

```cmd
uv venv .venv
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
uv venv .venv
source .venv/bin/activate
```

---

## Install Dependencies

Activate `.venv` first, then choose one method.

### Using pip

```bash
pip install -r requirements.txt
```

### Using uv (recommended)

```bash
uv pip install -r requirements.txt
```

### Add a new package

This project uses `requirements.txt` (not `pyproject.toml`), so use **pip** or **uv pip** — not `uv add`.

```bash
# pip
pip install langchain

# uv
uv pip install langchain
```

Then save locked versions to `requirements.txt`:

```bash
# pip
pip freeze > requirements.txt

# uv
uv pip freeze > requirements.txt
```

> **Note:** `uv add <package>` only works in uv-managed projects that have a `pyproject.toml`. This repo uses `requirements.txt` instead.

---

## Installed Packages (example)

After running `uv pip install langchain`, these packages were installed into `.venv`:

| Package | Version |
|---------|---------|
| langchain | 1.3.2 |
| langchain-core | 1.4.0 |
| langgraph | 1.2.2 |
| pydantic | 2.13.4 |
| httpx | 0.28.1 |
| pyyaml | 6.0.3 |
| ... | (+ 28 more dependencies) |

To see everything installed in your venv:

```bash
uv pip list
# or
pip list
```

---

## Common Issues

### `'uv' is not recognized`

uv is not installed, or your terminal was open **before** uv was installed.

1. Install uv (see [Install uv](#install-uv))
2. Close and reopen the terminal
3. Run `uv --version`

### `source .venv/bin/activate` fails on Windows

That command is for macOS/Linux. On Windows use:

```cmd
.venv\Scripts\activate
```

### uv hardlink warning on Windows

```
warning: Failed to hardlink files; falling back to full copy.
```

This is harmless — it happens when uv's cache and your project are on different drives or filesystems. Install still succeeds. To suppress the warning:

**Windows (CMD):**

```cmd
set UV_LINK_MODE=copy
uv pip install langchain
```

**macOS / Linux:**

```bash
export UV_LINK_MODE=copy
uv pip install langchain
```

Or pass the flag per command:

```bash
uv pip install --link-mode=copy langchain
```

### Deactivate the virtual environment

```bash
deactivate
```

---

## Recommended Workflow

1. Clone or open the project
2. Install uv (optional but recommended)
3. Create and activate `.venv`
4. Install from `requirements.txt`
5. Add packages with `uv pip install <package>` or `pip install <package>`
6. Update `requirements.txt` with `uv pip freeze > requirements.txt`

---

## Project Structure

```
Gen Ai Python/
├── .venv/              # Virtual environment (created locally, not committed)
├── docs/
│   └── setup.md        # This file
└── requirements.txt    # Python dependencies
```

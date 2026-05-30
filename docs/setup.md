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
pip install python-dotenv
REM Create .env in the project root and add your API keys (see Environment Variables section)
```

## Quick Start (macOS / Linux)

```bash
cd /path/to/Gen-Ai-Python
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install python-dotenv
# Create .env in the project root and add your API keys (see Environment Variables section)
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

### Load environment variables in Python

Install `python-dotenv` to read `.env` from your scripts:

```bash
pip install python-dotenv
# or
uv pip install python-dotenv
```

At the top of your Python files:

```python
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env into os.environ
```

---

## Environment Variables

This project uses a `.env` file in the project root for API keys and local configuration. The file is listed in `.gitignore` and must **never** be committed to git.

### Create your `.env` file

1. Create a file named `.env` in the project root (same folder as `requirements.txt`).
2. Add your keys using `KEY=value` format — one variable per line.
3. Do not wrap values in quotes unless the value itself contains spaces.

**Example `.env` (use your own keys, not these placeholders):**

```env
OPENAI_API_KEY=sk-proj-your-openai-key-here
ANTHROPIC_API_KEY=sk-ant-your-anthropic-key-here
GOOGLE_API_KEY=your-google-api-key-here
GROQ_API_KEY=gsk_your-groq-key-here
```

### Required variables

| Variable | Provider | Used for | Where to get a key |
|----------|----------|----------|-------------------|
| `OPENAI_API_KEY` | OpenAI | GPT models via LangChain | [platform.openai.com/api-keys](https://platform.openai.com/api-keys) |
| `ANTHROPIC_API_KEY` | Anthropic | Claude models via LangChain | [console.anthropic.com](https://console.anthropic.com/) |
| `GOOGLE_API_KEY` | Google | Gemini models via LangChain | [aistudio.google.com/apikey](https://aistudio.google.com/apikey) |
| `GROQ_API_KEY` | Groq | Fast inference (Llama, Mixtral, etc.) | [console.groq.com/keys](https://console.groq.com/keys) |

You only need the keys for the providers you actually use. Leave unused entries out of `.env`, or comment them out:

```env
OPENAI_API_KEY=sk-proj-...
# ANTHROPIC_API_KEY=sk-ant-...
```

### How LangChain reads keys

Most LangChain integrations read the matching environment variable automatically — no need to pass the key in code if `.env` is loaded:

```python
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")  # uses OPENAI_API_KEY from .env
```

Install provider packages as needed:

```bash
uv pip install langchain-openai langchain-anthropic langchain-google-genai langchain-groq
```

### Verify variables are loaded

**Python check:**

```python
import os
from dotenv import load_dotenv

load_dotenv()

for key in ("OPENAI_API_KEY", "ANTHROPIC_API_KEY", "GOOGLE_API_KEY", "GROQ_API_KEY"):
    value = os.getenv(key)
    print(f"{key}: {'set' if value else 'missing'}")
```

**Quick one-liner (after activating `.venv`):**

```bash
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('OPENAI_API_KEY:', 'set' if os.getenv('OPENAI_API_KEY') else 'missing')"
```

### Set variables without a `.env` file (optional)

You can set variables in the shell instead of using `.env`. Useful for CI or temporary testing.

**Windows (CMD — current session only):**

```cmd
set OPENAI_API_KEY=sk-proj-your-key-here
```

**Windows (PowerShell — current session only):**

```powershell
$env:OPENAI_API_KEY = "sk-proj-your-key-here"
```

**macOS / Linux (current session only):**

```bash
export OPENAI_API_KEY=sk-proj-your-key-here
```

For permanent system-wide variables on Windows: **Settings → System → About → Advanced system settings → Environment Variables**.

### uv-related environment variables

These are optional tuning flags for uv, not required for normal use:

| Variable | Purpose | Example |
|----------|---------|---------|
| `UV_LINK_MODE` | How uv links/copies packages into `.venv` | `copy` (suppresses hardlink warnings on Windows) |
| `UV_CACHE_DIR` | Custom cache directory for downloaded packages | `C:\Users\You\.uv-cache` |
| `UV_PYTHON` | Pin the Python interpreter uv uses | `3.12` |

**Windows (suppress hardlink warning):**

```cmd
set UV_LINK_MODE=copy
```

**macOS / Linux:**

```bash
export UV_LINK_MODE=copy
```

### Security rules

- **Never commit `.env`** — it is already in `.gitignore`.
- **Never paste real API keys** into chat, issues, or pull requests.
- **Rotate keys immediately** if one is accidentally exposed.
- Prefer `.env` for local dev; use your OS or CI secret store (GitHub Secrets, etc.) in production.
- Do not share `.env` files between teammates — each person creates their own from the template above.

### Common env variable issues

**`KeyError` or authentication errors from LangChain**

- Confirm `.env` is in the project root (same directory you run scripts from).
- Call `load_dotenv()` before importing or instantiating models.
- Check the variable name matches exactly (e.g. `OPENAI_API_KEY`, not `OPENAI_KEY`).

**Variables work in terminal but not in Python**

- Shell `set` / `export` and `.env` are separate. If using `.env`, you must call `load_dotenv()`.
- Restart the terminal or IDE after editing `.env`.

**Quotes in `.env` values**

- Prefer unquoted values: `GOOGLE_API_KEY=AIza...`
- If you use quotes, they become part of the value unless your loader strips them. Stick to no quotes when possible.

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
5. Create `.env` and add your API keys (see [Environment Variables](#environment-variables))
6. Install `python-dotenv` and any LangChain provider packages you need
7. Verify keys load correctly before running scripts
8. Add packages with `uv pip install <package>` or `pip install <package>`
9. Update `requirements.txt` with `uv pip freeze > requirements.txt`

---

## Project Structure

```
Gen Ai Python/
├── .env                # Local API keys (create yourself, never commit)
├── .gitignore          # Ignores .env, .venv, __pycache__
├── .venv/              # Virtual environment (created locally, not committed)
├── docs/
│   └── setup.md        # This file
├── install-test.py     # Quick check that langchain is installed
└── requirements.txt    # Python dependencies
```

# Chat Scripts

This guide covers the scripts in `chats/` — simple LangChain examples that call **Groq** using a free API key.

For project setup (venv, dependencies, `.env`), see [setup.md](./setup.md).

---

## Overview

| File | Approach | Best for |
|------|----------|----------|
| [`chats/index.py`](../chats/index.py) | `init_chat_model()` — provider-agnostic | Switching models/providers with one API |
| [`chats/modal-chat.py`](../chats/modal-chat.py) | `ChatGroq()` — Groq-specific | Groq-only apps, full Groq SDK options |

Both scripts do the same thing: send `"Hello, how are you?"` to **Llama 3.1 8B Instant** on Groq and print the reply.

---

## Free API key (Groq)

Groq offers a **free tier** with rate limits — enough for learning and small projects.

1. Sign up at [console.groq.com](https://console.groq.com/)
2. Create an API key at [console.groq.com/keys](https://console.groq.com/keys)
3. Add it to your `.env` in the project root:

```env
GROQ_API_KEY=gsk_your-key-here
```

No quotes around the value. Restart your terminal or IDE after editing `.env`.

---

## Prerequisites

From the project root, with `.venv` activated:

```cmd
pip install -r requirements.txt
```

Required packages (already in `requirements.txt`):

- `langchain`
- `langchain-groq`
- `python-dotenv`

---

## Run the scripts

**Windows:**

```cmd
cd "D:\projects\Gen Ai Python"
.venv\Scripts\activate
python chats\index.py
python chats/modal-chat.py
```

**macOS / Linux:**

```bash
cd /path/to/Gen-Ai-Python
source .venv/bin/activate
python chats/index.py
python chats/modal-chat.py
```

Expected output: a short text reply from the model (content varies each run).

---

## `chats/index.py` — universal init

Uses LangChain’s `init_chat_model()` so you can swap providers later by changing `model` and `model_provider`.

```python
from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
import os

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY is missing. Add it to your .env file.")

model = init_chat_model(
    "llama-3.1-8b-instant",
    model_provider="groq",  # required for Groq model names
    api_key=api_key,
)

response = model.invoke("Hello, how are you?")
print(response.content)
```

### Why `model_provider="groq"` is required

LangChain cannot guess the provider from `llama-3.1-8b-instant` alone. Without it you get:

```
ValueError: Unable to infer model provider for model='llama-3.1-8b-instant'.
Please specify 'model_provider' directly.
```

Always pass `model_provider="groq"` when using Groq models with `init_chat_model`.

### Switching to another free provider

If you use a different key from `.env`, change `model`, `model_provider`, and the env variable:

| Provider | `model_provider` | Example model | `.env` key |
|----------|------------------|---------------|------------|
| Groq | `groq` | `llama-3.1-8b-instant` | `GROQ_API_KEY` |
| Google Gemini | `google_genai` | `gemini-2.0-flash` | `GOOGLE_API_KEY` |
| OpenAI | `openai` | `gpt-4o-mini` | `OPENAI_API_KEY` |
| Anthropic | `anthropic` | `claude-3-5-haiku-latest` | `ANTHROPIC_API_KEY` |

Example for Gemini (free tier via Google AI Studio):

```python
model = init_chat_model(
    "gemini-2.0-flash",
    model_provider="google_genai",
    api_key=os.getenv("GOOGLE_API_KEY"),
)
```

---

## `chats/modal-chat.py` — Groq-native

Uses `ChatGroq` from `langchain-groq` directly. Good when you only use Groq and want Groq-specific parameters.

```python
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
import os

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY is missing. Add it to your .env file.")

model = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=api_key,
)

response = model.invoke("Hello, how are you?")
print(response.content)
```

`ChatGroq` reads `GROQ_API_KEY` from the environment automatically if you omit `groq_api_key`, but passing it explicitly keeps behavior clear.

### Optional Groq models (free tier)

Check [Groq docs](https://console.groq.com/docs/models) for current models. Common choices:

| Model | Notes |
|-------|--------|
| `llama-3.1-8b-instant` | Fast, default in these scripts |
| `llama-3.3-70b-versatile` | Larger, slower |
| `mixtral-8x7b-32768` | Long context |

Change the `model=` argument in either script to try another model.

---

## Which script should I use?

| Use `index.py` if… | Use `modal-chat.py` if… |
|--------------------|-------------------------|
| You may switch OpenAI / Gemini / Groq later | You only use Groq |
| You prefer one `init_chat_model` pattern | You want Groq-specific options (temperature, streaming, etc.) |
| You're following LangChain tutorials | You're building a Groq-focused app |

---

## Troubleshooting

### `GROQ_API_KEY is missing`

- Create `.env` in the **project root** (not inside `chats/`)
- Add `GROQ_API_KEY=gsk_...`
- Call `load_dotenv()` before reading the key (both scripts already do this)
- Run scripts from the project root so `.env` is found

### `Unable to infer model provider`

- Only applies to `index.py` / `init_chat_model`
- Add `model_provider="groq"`

### Authentication / 401 errors

- Key is invalid or expired — create a new one at [console.groq.com/keys](https://console.groq.com/keys)
- No extra quotes in `.env`: use `GROQ_API_KEY=gsk_abc...` not `GROQ_API_KEY="gsk_abc..."`

### Rate limits (free tier)

Groq free tier has request and token limits. If you hit limits, wait a few minutes or check your usage in the Groq console.

---

## Project layout

```
Gen Ai Python/
├── .env                 # GROQ_API_KEY and other keys (not committed)
├── chats/
│   ├── index.py         # init_chat_model + Groq
│   └── modal-chat.py    # ChatGroq direct
├── docs/
│   ├── setup.md         # Environment & dependencies
│   └── chats.md         # This file
└── requirements.txt
```

---

## Next steps

- Change the prompt in `model.invoke("...")` to ask your own questions
- Pass a list of messages for multi-turn chat
- Try streaming: `model.stream("Hello")` and print chunks as they arrive
- Add other providers using the same `.env` keys — see [setup.md](./setup.md#environment-variables)

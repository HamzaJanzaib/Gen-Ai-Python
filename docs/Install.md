# Install Dependencies

```bash
# Using python
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

# what is The UV?
UV is a tool for managing Python projects. It is a replacement for pip and venv. It is a replacement for pip and venv. It is a replacement for pip and venv. It is a replacement for pip and venv. It is a replacement for pip and venv. It is a replacement for pip and venv.

```bash
uv --version
```

# install uv (recommended)
```bash
macos:
curl -LsSf https://astral.sh/uv/install.sh | sh

linux:
curl -LsSf https://astral.sh/uv/install.sh | sh

windows:
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

# add uv to your path
```bash
export PATH="$HOME/.local/bin:$PATH"
```


# Using uv

```bash
uv venv .venv && source .venv/bin/activate
uv pip install -r requirements.txt
```

# Using poetry

```bash
uv venv .venv && source .venv/bin/activate
uv pip install -r requirements.txt
```

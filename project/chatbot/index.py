import os
import re
import sys

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY is missing. Add it to your .env file.")

# gemini-2.0-flash free-tier quota may be exhausted; 2.5-flash-lite works on free tier.
model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")

model = init_chat_model(
    model_name,
    model_provider="google_genai",
    api_key=api_key,
    temperature=0.7,
)

messages: list = [
    SystemMessage(content="You are a helpful assistant. Keep replies clear and concise."),
]


def format_error(exc: Exception) -> str:
    message = str(exc)
    if "429" in message or "RESOURCE_EXHAUSTED" in message:
        retry_match = re.search(r"retry in ([0-9.]+)s", message, re.IGNORECASE)
        retry_hint = f" Retry in about {retry_match.group(1)}s." if retry_match else ""
        return (
            f"Gemini quota exceeded for {model_name}.{retry_hint} "
            "Try again later, switch GEMINI_MODEL in .env, or check "
            "https://aistudio.google.com/"
        )
    if "401" in message or "API key" in message:
        return "Invalid GOOGLE_API_KEY. Get a key at https://aistudio.google.com/apikey"
    return message


def main() -> None:
    print(f"Gemini Chatbot ({model_name}) — type 'quit', 'exit', or 'q' to stop\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break

        if not user_input:
            continue

        if user_input.lower() in {"quit", "exit", "q"}:
            print("Bye!")
            break

        messages.append(HumanMessage(content=user_input))

        try:
            response = model.invoke(messages)
        except Exception as exc:
            messages.pop()
            print(f"\nError: {format_error(exc)}\n", file=sys.stderr)
            continue

        messages.append(AIMessage(content=response.content))
        print(f"\nGemini: {response.content}\n")


if __name__ == "__main__":
    main()

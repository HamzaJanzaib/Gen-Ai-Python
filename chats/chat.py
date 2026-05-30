import os

from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import init_chat_model

# Groq free tier: get a key at https://console.groq.com/keys
# Add to .env as GROQ_API_KEY=gsk_...
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY is missing. Add it to your .env file.")

model = init_chat_model(
    "llama-3.1-8b-instant",
    model_provider="groq",  # required — LangChain can't infer this from the model name
    api_key=api_key,
)

response = model.invoke("Hello, how are you?")
print(response.content)

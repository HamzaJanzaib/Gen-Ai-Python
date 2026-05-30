import os

from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq

# Groq free tier: get a key at https://console.groq.com/keys
# Add to .env as GROQ_API_KEY=gsk_...
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY is missing. Add it to your .env file.")


"""
model: The model to use.
groq_api_key: The API key to use.
base_url: The base URL to use.
api_version: The API version to use.
api_key: The API key to use.
api_key_path: The API key path to use.
api_key_name: The API key name to use.
api_key_value: The API key value to use.
"""

model = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=api_key,
)

response = model.invoke("Hello, how are you?")
print(response.content)

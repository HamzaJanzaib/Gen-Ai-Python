import os

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is missing. Add it to your .env file.")

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    dimensions=64,
    api_key=api_key,
)

texts = [
    "The cat sat on the mat.",
    "Dogs love to play fetch in the park.",
    "Machine learning turns data into predictions.",
]

vectors = embeddings.embed_documents(texts)

for text, vector in zip(texts, vectors, strict=True):
    print(f"Text: {text}")
    print(f"Dimensions: {len(vector)}")
    print(f"First 5 values: {vector[:5]}")
    print()

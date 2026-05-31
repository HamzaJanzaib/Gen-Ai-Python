import os

from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not api_token:
    raise ValueError(
        "HUGGINGFACEHUB_API_TOKEN is missing. Add it to your .env file."
    )

# Required for huggingface_hub / langchain_huggingface auth
os.environ["HUGGINGFACEHUB_API_TOKEN"] = api_token

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    huggingfacehub_api_token=api_token,
    temperature=0.7,
    max_new_tokens=1024,
)
model = ChatHuggingFace(llm=llm)

response = model.invoke("write a poem about a cat")
print(response.content)

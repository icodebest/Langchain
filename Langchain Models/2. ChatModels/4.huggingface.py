from langchain_huggingface import HuggingFaceEndpoint

import os
from dotenv import load_dotenv

load_dotenv()
access_token = os.getenv("HUGGINGFACE_API_TOKEN")

# Load a simple, working text generation model
model = HuggingFaceEndpoint(
    repo_id="gpt2",
    task="text-generation",
    huggingfacehub_api_token=access_token
)

# Invoke the model
result = model.invoke("The capital of Pakistan is")
print(result)

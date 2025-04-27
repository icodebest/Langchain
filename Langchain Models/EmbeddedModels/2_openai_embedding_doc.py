from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

document=[
   "Would you like me to also give you a full offline working code?",
    "(No token, no API, just your Windows machine + GPU/CPU)?",
    "If still error? Alternative: Use direct huggingface pipeline (without langchain)"
]

result=embedding.embed_documents(document)

print(str(result))

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

print("GOOGLE_API_KEY:", os.getenv("GOOGLE_API_KEY"))  # Check API Key

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

print("Invoking model...")

result = model.invoke("What is the capital of Pakistan?")

print("Response received!")
print(result.content)

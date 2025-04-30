from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os

# Load environment variables from .env file (e.g., for GOOGLE_API_KEY)
load_dotenv()

# Initialize model with the required model name (e.g., "gemini-pro")
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# 1st prompt -> Detailed report
template1 = PromptTemplate(
    input_variables=["topic"],
    template="Write a detailed report on the following topic: {topic}",
)

# 2nd prompt -> Summary
template2 = PromptTemplate(
    input_variables=["text"],
    template="Write a 5-line summary of the following text: {text}",
)

# Format and invoke the 1st prompt
prompt1 = template1.format(topic="Artificial Intelligence")
result = model.invoke(prompt1)

# Format and invoke the 2nd prompt using the result of the 1st
prompt2 = template2.format(text=result.content)
result1 = model.invoke(prompt2)

# Print resultss
print("Detailed Report:\n", result.content)
print("\nSummary:\n", result1.content)

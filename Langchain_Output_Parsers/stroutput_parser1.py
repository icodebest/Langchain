from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os

from langchain_core.output_parsers import StrOutputParser


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

parser=StrOutputParser()

#chain to invoke the model with the first prompt and parse the output
chain= template1 | model | parser | template2 | model | parser

result=chain.invoke({"topic":"Artificial Intelligence"})

print(result)
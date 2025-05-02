from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# Define prompt templates
prompt1 = PromptTemplate(
    template="Generate a detailed report about {topic}, including its history, current trends, and future prospects. Think like a professional analyst.",
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template="Generate a 5-pointer summary from the following text:\n{text}",
    input_variables=["text"],
)

# Initialize the model (ensure you have access to the chosen model)
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")  # Check if "gemini-2.0-flash" is correct for your case

# Set up output parser
parser = StrOutputParser()

# Create the chain of transformations
chain = prompt1 | model | parser | prompt2 | model | parser

# Handle API response within a try-except block to catch errors (like quota exceed)
try:
    result = chain.invoke({"topic": "Unemployment in Pakistan"})
    print(result)
except Exception as e:
    print(f"Error: {str(e)}")

# Optional: Visualize the chain graph
chain.get_graph().print_ascii()

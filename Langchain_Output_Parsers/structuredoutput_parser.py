from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

# Load API key from .env
load_dotenv()
 
# Initialize the model
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")  # "gemini-2.0-flash" is fine too if supported

# Define response schema
schema = [
    ResponseSchema(name="fact_1", description="A fact one about the topic"),
    ResponseSchema(name="fact_2", description="A fact two about the topic"),
    ResponseSchema(name="fact_3", description="A fact three about the topic"),
]

# Initialize parser
parser = StructuredOutputParser.from_response_schemas(schema)

# Define prompt template
template = PromptTemplate(
    template="Give me three facts about the topic '{Topic}'.\n{format_instructions}",
    input_variables=['Topic'],
    partial_variables={
        'format_instructions': parser.get_format_instructions()
    }
)

chain= template | model | parser

# # Format the prompt
# prompt = template.format(Topic="Pakistan")

# Invoke the model
result = chain.invoke({"Topic": "Pakistan"})


# Display the result
print(result)
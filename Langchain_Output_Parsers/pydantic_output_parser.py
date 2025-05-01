from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
import os

load_dotenv()

# Initialize model with the required model name (e.g., "gemini-pro")
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(gt=18, description="Age of the person")
    city: str = Field(description="City of the person")


parser=PydanticOutputParser(pydantic_object=Person)

template= PromptTemplate(
    template='Give me the name, age, and city of the fictional {place} person\n{formate_instruction}',
    input_variables=[],
    partial_variables={
        'formate_instruction': parser.get_format_instructions()
    }
)

# prompt=template.format(place="pakistani")

# print(prompt)

# result=model.invoke(prompt)
# final_result=parser.parse(result.content)

chain=template | model | parser
final_result=chain.invoke({"place":"pakistani"})

print(final_result)
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# Initialize model with the required model name (e.g., "gemini-pro")
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

parser=JsonOutputParser()

template = PromptTemplate(
    template='Give me the name, age, and city of the fictional person\n{formate_instruction}',
    input_variables=[],
    partial_variables={
        'formate_instruction': parser.get_format_instructions()
    }
)


# prompt=template.format()
# result=model.invoke(prompt)
# final_result=parser.parse(result.content)

chain=template | model | parser
result=chain.invoke({})

print(result)
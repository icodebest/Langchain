from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model=ChatAnthropic(model="claude-2")
result=model.invoke("Can you tell me about the history of the Eiffel Tower?")
print(result)
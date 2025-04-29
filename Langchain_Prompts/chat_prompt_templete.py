from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

chat_template = ChatPromptTemplate([
    SystemMessage(content="You are a helpful {domain} expert."),
    HumanMessage(content='Explain in simplet terms what is {topic} and why it is important.')
])

prompt=chat_template.invoke({
    "domain": "AI",
    "topic": "Machine Learning"
})
print(prompt) # This will print the formatted prompt with the provided domain and topic.
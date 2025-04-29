from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional

load_dotenv()

# Create the model
model = ChatOpenAI(model="gpt-3.5-turbo")

# Correctly define the output schema
class Review(TypedDict):
    key_themes: Annotated[list[str], "Write down all the key themes discuss in a list"]
    summary: Annotated[str, "A bried summary of the review"]
    sentiment: Annotated[str, "The sentiment of the review, either positive or negative"]
    pros=Annotated[Optional[list[str]], "List of pros, if any"]
    cons=Annotated[Optional[list[str]], "List of cons, if any"]


# Use structured output with function_calling method
structured_model = model.with_structured_output(Review, method="function_calling")

# Call the model with a sample review
result = structured_model.invoke("""
I’ve had this smart vacuum cleaner for about two months now, and I have mixed feelings. On the plus side, it navigates very well around furniture, has strong suction for its size, and does a solid job with pet hair—something my older vacuum constantly struggled with. The companion app is intuitive, and scheduling cleanings is a breeze. But the battery life is disappointing—it barely makes it through a full session in my apartment, which isn’t huge. It also tends to get stuck under my sofa unless I physically block it. Customer support was helpful, but it took three days to get a response. I appreciate the features, but for this price point, I expected more polish. If battery and navigation quirks were fixed, I’d be 100% on board.
""")

print(result)

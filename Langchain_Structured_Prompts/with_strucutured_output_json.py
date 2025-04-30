from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

# Create the model
model = ChatOpenAI(model="gpt-3.5-turbo")

# Correctly define the output schema
#json schema
json_schema = {
    "title": "ProductReview",
    "type": "object",
    "properties": {
        "Key_themes": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "Key themes or topics discussed in the review"
        },
        "Summary": {
            "type": "string",
            "description": "A brief summary of the review"
        },
        "sentiment": {
            "type": "string",
            "enum": ["positive", "negative", "neutral"],
            "description": "The sentiment of the review (positive, negative, neutral)"
        },
        "pros": {
            "type": ["array", "null"],
            "items": {
                "type": "string"
            },
            "description": "Pros of the product as mentioned in the review"
        },
        "cons": {
            "type": ["array", "null"],
            "items": {
                "type": "string"
            },
            "description": "cons of the product as mentioned in the review"
        },
        "reviewer_name": {
            "type": ["string", "null"],
            "description": "The name of the reviewer"
        },
        "overall_rating": {
            "type": "number",
            "description": "The overall rating of the product out of 5"
        },
        
    },
    "required": ["Key_themes", "Summary", "sentiment","overall_rating"],
}



# Use structured output with function_calling method
structured_model = model.with_structured_output(json_schema, method="function_calling")

# Call the model with a sample review
result = structured_model.invoke("""
I’ve had this smart vacuum cleaner for about two months now, and I have mixed feelings. On the plus side, it navigates very well around furniture, has strong suction for its size, and does a solid job with pet hair—something my older vacuum constantly struggled with. The companion app is intuitive, and scheduling cleanings is a breeze. But the battery life is disappointing—it barely makes it through a full session in my apartment, which isn’t huge. It also tends to get stuck under my sofa unless I physically block it. Customer support was helpful, but it took three days to get a response. I appreciate the features, but for this price point, I expected more polish. If battery and navigation quirks were fixed, I’d be 100% on board my name is Waleed.
""")

print(result)

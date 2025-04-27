from langchain_openai import ChatOpenAI
from langchain.prompts import load_prompt
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
load_dotenv()

# Initialize the LLM
llm = ChatOpenAI(
    model='gpt-3.5-turbo'
)

# Load the PromptTemplate from JSON file
prompt_template = load_prompt("research_paper_explanation_template.json")

# Streamlit app
st.header("🧠 Research Paper Explainer Tool")

# Dropdown options
research_papers = [
    "Deep Learning for NLP",
    "Transformers in Vision",
    "Reinforcement Learning Basics",
    "Graph Neural Networks Overview",
    "Large Language Models Survey",
    "GANs and Their Applications",
    "Meta-Learning Techniques",
    "Federated Learning Concepts",
    "Explainable AI Trends",
    "Zero-Shot Learning Advances"
]

explanation_types = [
    "Simple Summary",
    "Detailed Explanation",
    "Key Points Extraction",
    "Step-by-Step Walkthrough",
    "Pros and Cons Analysis"
]

length_options = [
    "Short (50-100 words)",
    "Medium (100-200 words)",
    "Long (200+ words)"
]

# Select boxes
selected_paper = st.selectbox("Select a Research Paper", research_papers)
selected_explanation = st.selectbox("Select Explanation Type", explanation_types)
selected_length = st.selectbox("Select Length of Explanation", length_options)

# Combine prompt template and llm
chain = prompt_template | llm

# Prepare the inputs once
inputs = {
    "paper": selected_paper,
    "explanation_type": selected_explanation,
    "length": selected_length
}

# When "Summarize" button is clicked
if st.button("Summarize"):
    result = chain.invoke(inputs)
    st.subheader("📜 Generated Summary:")
    st.write(result.content)

# When "Generate Explanation" button is clicked 
if st.button('Generate Explanation'):
    result = chain.invoke(inputs)
    st.subheader("📜 Generated Explanation:")
    st.write(result.content)

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

# Load the PromptTemplate from JSON file
prompt_template = load_prompt("research_paper_explanation_template.json")

# When "Generate Explanation" button is clicked
if st.button('Generate Explanation'):
    # Fill the template using the loaded PromptTemplate
    formatted_prompt = prompt_template.format(
        paper=selected_paper,
        explanation_type=selected_explanation,
        length=selected_length
    )

    # Invoke the model with the formatted prompt
    result = llm.invoke(formatted_prompt)

    # Show the result
    st.subheader("📜 Generated Explanation:")
    st.write(result.content)

# When "Summarize" button is clicked
if st.button("Summarize"):
    formatted_prompt = prompt_template.format(
        paper=selected_paper,
        explanation_type="Simple Summary",
        length="Short (50-100 words)"
    )

    result = llm.invoke(formatted_prompt)
    st.subheader("📄 Summary:")
    st.write(result.content)

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()

# Initialize LLM
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

# Define the dynamic prompt template
prompt_template = PromptTemplate(
    input_variables=["paper", "explanation_type", "length"],
    template=(
        "You are a research expert.\n\n"
        "Please provide a {explanation_type} of the research paper titled "
        "'{paper}', with a length approximately matching {length}.\n\n"
        "Make sure the response is clear, informative, and easy to understand."
    )
)


# prompt=template.invoke({
#     'selected_paper': selected_paper,
#     'selected_explanation': selected_explanation,
#     'selected_length': selected_length
# })

# When button is clicked
if st.button('Generate Explanation'):
    # Dynamic prompt creation
    prompt = (
        f"You are a research expert.\n\n"
        f"Please provide a **{selected_explanation}** of the research paper titled "
        f"**'{selected_paper}'**, with a length approximately matching **{selected_length}**.\n\n"
        f"Make sure the response is clear, informative, and easy to understand."
    )
 
    # Invoke the model
    result = llm.invoke(prompt)

    # Show the result
    st.subheader("📜 Generated Explanation:")
    st.write(result.content)

if st.button("Summarize"):
    result=llm.invoke(prompt)
    st.write(result.content)


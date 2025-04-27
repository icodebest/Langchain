from langchain_core.prompts import PromptTemplate

# Define the PromptTemplate
prompt_template = PromptTemplate(
    input_variables=["paper", "explanation_type", "length"],
    validate_template=True,
    # This will ensure that the template is valid and all variables are used correctly
    template=(
        "You are a research expert.\n\n"
        "Please provide a {explanation_type} of the research paper titled "
        "'{paper}', with a length approximately matching {length}.\n\n"
        "Make sure the response is clear, informative, and easy to understand."
    )
)

prompt_template.save("research_paper_explanation_template.json")
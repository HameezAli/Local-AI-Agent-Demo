import streamlit as st
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever  # Ensure this exists and works as intended

# Initialize model and prompt template
model = OllamaLLM(model="llama3.2")
template = """
Pretend you are an expert in answering questions about a pizzeria.
Here are some relevant reviews: {reviews}
Here, now answer this question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Streamlit App
st.set_page_config(page_title="Pizzeria Q&A", page_icon="🍕")
st.title("🍕 Pizzeria Review Assistant")
st.markdown("Ask any question about the pizzeria and get insights based on customer reviews.")

# Input box for user question
question = st.text_input("Ask your question here:", placeholder="e.g. Is the pizza spicy?")

# Submit button
if st.button("Get Answer"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            reviews = retriever.invoke(question)
            result = chain.invoke({"reviews": reviews, "question": question})
            st.markdown("### Answer:")
            st.write(result)
            st.markdown("### Reviews Used:")
            st.code(reviews, language="markdown")

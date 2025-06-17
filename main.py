from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model=OllamaLLM(model="llama3.2")
template="""
Pretend you are an expert in answering questions about a pizzeria.
Here are some relevant reviews: {reviews}
Here, now answer this question: {question}
"""
prompt=ChatPromptTemplate.from_template(template)
chain=prompt|model
while True:
    print("\n---------------------------------------------")
    question=input("Ask any question:")
    if question=="q":
        break
    result=chain.invoke({"reviews":[],"question":"What is the average rating of the pizzeria?"})
    print(result)
    print("\n---------------------------------------------")

from config import *
from rag_retriever import use_rag
open_logs("concept_generator")


# README: This script can be used to generate 5 short concepts that respond to the context retrieved by the RAG agent on the knowledge pool.
# Choose between "local" or "openai" mode in config.py

# RAG Parameters
question = "What are 10 areas for improvement in the restaurant?"
embeddings_json= r"C:\Users\ohakimu\OneDrive - Perkins and Will\Desktop\IAAC\Semester 3\Gen AI\LLM\LLM-Knowledge-Pool-RAG\knowledge_pool\most_reviewed_business_reviews.json"
num_results = 100

def generate_concept(rag_result: str)-> str:
    response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {
                "role": "system",
                "content": """You are the creative director of a top restaurant chain.
                       Your goal is to propose 5 innovative and exciting changes or improvements to the restaurant experience. 
                       For each, provide a brief description of the concept, focusing on its uniqueness and appeal.
                       """,
            },
            {
                "role": "user",
                "content": f"""Propose 5 imaginative concepts for improving the restaurant. Each concept should be distinctive and captivating. 
                Use the following information as a starting point:
                {rag_result}""",
            },
        ],
        #max_tokens=50 #Set the maximum number of tokens for each response
    )
    return response.choices[0].message.content

# Execute the pipeline
rag_result= use_rag(question, embeddings_json, num_results)
print(rag_result)
concepts = generate_concept(rag_result)
print(concepts)

close_logs()

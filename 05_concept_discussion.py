from autogen import ConversableAgent
from config import *
from rag_retriever import use_rag
open_logs("concept_discussion")


# README: This script creates a conversation between an intern (creates concepts) and a jury (asks questions about them)
# Similar to script 2 and 3, but this time the questions are asked dinamically by another agent.

# RAG Parameters
question = "What is the current state of service at the restaurant?"
embeddings_json= r"C:\Users\ohakimu\OneDrive - Perkins and Will\Desktop\IAAC\Semester 3\Gen AI\LLM\LLM-Knowledge-Pool-RAG\knowledge_pool\most_reviewed_business_reviews.json"
num_results = 10

# Define the agents involved in the conversation
creative_director = ConversableAgent(name="creative director",
                       description="Provides guidance on restaurant concepts and improvements",
                       system_message=""" 
                       You are the creative director of a top restaurant chain.
                       Your role is to evaluate the current state of the restaurants and propose innovative concepts for improvement.
                       You will engage in a conversation with the restaurant consultant to discuss potential improvements. 
                       For each, come up a short paragraph describing the concept in a very poetic and imaginative way.
                       """,
                       is_termination_msg = lambda msg: msg.get("content") is not None
                        and "100%" in msg["content"],
                       llm_config={
                           "config_list": mistral_7b,
                           "temperature": 0.9,
                       },
                       code_execution_config=False,
                       )

restaurant_consultant= ConversableAgent(name="restaurant consultant",
                       description="Reviews suggestions and restaurant improvements",
                       system_message="""
                       Your role is to provide insights and suggestions for improving the restaurant.
                       You will engage in a conversation with the creative director to discuss the current state of the restaurants and propose concepts for improvement.
                       You will follow this subtasks:
                       1. Think about the concept and make three questions that will expose additional detail about the concept.
                       2. Classify between 0 and 100% how much the given concept answers your questions clearly and is related to the restaurant context information.
                       You will always ask new questions about the concept to the creative director until you are satisfied with the concept.
                       If you are satisfied, simply answer "100%"
                       """,
                       is_termination_msg = lambda msg: msg.get("content") is not None
                        and "100%" in msg["content"],
                        # human_input_mode="ALWAYS",
                       llm_config={
                           "config_list": mistral_7b,
                           "temperature": 0.9,
                       })

# Run RAG
rag_result= use_rag(question, embeddings_json, num_results)

# Start the conversation
chat_result= restaurant_consultant.initiate_chats(
    [
        {
            "recipient": creative_director,
            "message": f"""
                **design context information**: 
                {rag_result}
                ----
                Lets develop an idea for the restaurant. 
                What should be the concepts for the restaurant?
                """,
            "summary_method": "reflection_with_llm",
        },
    ]
)

close_logs()
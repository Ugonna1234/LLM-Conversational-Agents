from config import *
open_logs("concept_tasks")


# README: This script uses one concept you want to investigate further.
# Choose between "local" or "openai" mode in config.py

concept = """**Sensory Dining Nights: Host monthly themed events where guests are immersed in a multi-sensory dining experience. These nights may include live music performances, art installations related to the menu's theme, scents wafting through the air, or even blindfolded tastings to heighten other senses. Such unique experiences will draw attention from food enthusiasts seeking novel culinary adventures."""

tasks = """ 1. List out 5 potential themes for the sensory dining nights.
            2. Describe 5 ways how the restaurant space could be transformed to accommodate these themed events.
            3. Propose 5 marketing strategies to promote the sensory dining nights to potential customers."""  

def question_concept(tasks: str, concept: str)-> str:
    # client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {
                "role": "system",
                "content": """ 
                       You are a renowned restaurant consultant. You provide detailed answers to questions related to restaurant concepts and operations.""",
            },
            {
                "role": "user",
                "content": 
                        f"""You are given a set of tasks and a brief summary of a restaurant concept.
                        Provide creative and insightful answers:
                        #CONCEPTS#: {concept}
                        #TASKS#: {tasks}
                        """,
            },
        ],
        #max_tokens=450,
    )
    return response.choices[0].message.content


answer = question_concept(tasks, concept)
print(answer)

close_logs()



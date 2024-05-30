from config import *
open_logs("concept_tasks")


# README: This script uses one concept you want to investigate further.
# Choose between "local" or "openai" mode in config.py

concept = """**Concept 1: Whirlwind Winter Refuge: Evoking the graceful spirals of a snowstorm caught mid-whirl, this dynamic ski cabin concept unfolds as a helix rising skyward towards towering peaks. Its spiral design maximizes functionality through compact organization – storage nestled within windings, communal area at its core encircled by changing rooms and refreshments zones spiraling outward before opening into panoramic windows capturing breathtaking alpine views. At ground level lies an interactive info point alongside a snow groomer garage completing the circular narrative of winter wonderland sheltering all within."""

tasks = """ 1. First, list out the names of all interior spaces in this building.
            2. Second, explain how they are connected and one can move from space to space across the building.
            3. Third, describe what a visitor will see and find inside each of the spaces."""  

def question_concept(tasks: str, concept: str)-> str:
    # client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {
                "role": "system",
                "content": """ 
                       You are a world renowed architect. You answer questions about building design concepts.""",
            },
            {
                "role": "user",
                "content": 
                        f"""You are given a set of tasks and a brief summaries of a building design concept.
                        Be imaginative and creative in your answers:
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



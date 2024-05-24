import gradio as gr
from crewai import Agent, Task, Crew
import os
from dotenv import load_dotenv
from udio_wrapper import UdioWrapper

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
udio_auth_token = os.getenv("UDIO_API_KEY")
udio_wrapper = UdioWrapper(udio_auth_token)


def run_agent(role, goal, backstory, task_description, expected_output):
    # Create agent with user-specified parameters
    general_agent = Agent(
        role=role,
        goal=goal,
        backstory=backstory,
        verbose=True,
        allow_delegation=True
    )

    # Create task with user-specified parameters
    task = Task(
        description=task_description,
        agent=general_agent,
        expected_output=expected_output
    )

    # Create crew
    crew = Crew(
        agents=[general_agent],
        tasks=[task],
        verbose=2
    )

    # Execute crew kickoff
    result = crew.kickoff()
    song = make_song(task_description,result)
    print(song)
    song_path = song[0]['song_path']

    return [result,song_path]

def make_song(task_description, result):
    song = udio_wrapper.create_song(prompt=task_description,custom_lyrics=result)
    return song

# Define Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Agent and Task Configuration")

    role = gr.Textbox(label="Role of the Agent", placeholder="Enter the role of your agent")
    goal = gr.Textbox(label="Goal of the Agent", placeholder="Enter the goal of your agent")
    backstory = gr.Textbox(label="Backstory of the Agent", placeholder="Enter the backstory of your agent")
    task_description = gr.Textbox(label="Task Description", placeholder="Enter the description of the task")
    expected_output = gr.Textbox(label="Expected Output", placeholder="Enter the expected output of the task")

    submit_button = gr.Button("Run Agent")

    result = gr.Textbox(label="Result")
    player = gr.Audio(label="Audio")



    submit_button.click(
        fn=run_agent,
        inputs=[role, goal, backstory, task_description, expected_output],
        outputs=[result,player]
    )



# Launch the interface
demo.launch()
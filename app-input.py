from crewai import Agent, Task, Crew
from langchain_community.llms.llamafile import Llamafile
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

def get_user_input():
    role = input("Agent Job Title: ")
    backstory = input("Agent Qualifications: ")
    task_description = input("Agent Task: ")
    goal = input("Goal of Task: ")
    expected_output = input("Expected Output Format: ")

    return role, goal, backstory, task_description, expected_output

def main():
    # Get user input
    role, goal, backstory, task_description, expected_output = get_user_input()

    # Initialize Llamafile
    llm = Llamafile()

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

    print(result)

if __name__ == "__main__":
    main()
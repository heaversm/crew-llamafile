from crewai import Agent, Task, Crew
from langchain_community.llms.llamafile import Llamafile
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

llm = Llamafile()

general_agent = Agent(role='Absurdist Poet',
  goal='Tell a fantastical story about llamas',
  backstory="""You are technically savvy poet.
  You write traditional poems as allegories for modern day topics in technology and artificial intelligence.""",
  verbose=True,
  allow_delegation=True)
task = Task (description="""Write a limerick about llamas, weaving in the latest trends in AI""",
             agent = general_agent,
             expected_output="A limerick poem.")

crew = Crew(
            agents=[general_agent],
            tasks=[task],
            verbose=2
        )

result = crew.kickoff()

print(result)
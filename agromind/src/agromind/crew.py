from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from typing import List

# Import de l'outil personnalisé (maintenant avec le bon BaseTool)
from agromind.tools.classify_plant_by_api import classify_plant_by_api
from crewai_tools import SerperDevTool


@CrewBase
class Agromind():
    """Agromind crew"""

    def __init__(self):
        # Initialiser les outils
        self.remedy_web_search_tool = SerperDevTool()
        super().__init__()

    @agent
    def classifier(self) -> Agent:
        return Agent(
            config=self.agents_config['classifier'],
            tools=[classify_plant_by_api],  # Maintenant compatible avec crewai.tools.BaseTool
            verbose=True
        )

    @agent
    def remedy_searcher(self) -> Agent:
        return Agent(
            config=self.agents_config['remedy_searcher'],
            tools=[self.remedy_web_search_tool],
            verbose=True
        )

    @agent
    def remedy_verifier(self) -> Agent:
        return Agent(
            config=self.agents_config['remedy_verifier'],
            verbose=True
        )

    @agent
    def translator(self) -> Agent:
        return Agent(
            config=self.agents_config['translator'],
            verbose=True
        )

    @task
    def classify_task(self) -> Task:
        return Task(
            config=self.tasks_config['classify_task'],
        )

    @task
    def search_remedy_task(self) -> Task:
        return Task(
            config=self.tasks_config['search_remedy_task'],
        )

    @task
    def verify_remedy_task(self) -> Task:
        return Task(
            config=self.tasks_config['verify_remedy_task'],
        )

    @task
    def translate_task(self) -> Task:
        return Task(
            config=self.tasks_config['translate_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Agromind crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
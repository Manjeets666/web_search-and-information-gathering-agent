from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool

@CrewBase
class BuildingAnAiAgentForWebSearchAndInformationGatheringCrew():
    """BuildingAnAiAgentForWebSearchAndInformationGathering crew"""

    @agent
    def ai_info_gatherer(self) -> Agent:
        return Agent(
            config=self.agents_config['ai_info_gatherer'],
            tools=[ScrapeWebsiteTool()],
        )


    @task
    def search_for_latest_ai_services_and_trends(self) -> Task:
        return Task(
            config=self.tasks_config['search_for_latest_ai_services_and_trends'],
            tools=[ScrapeWebsiteTool()],
        )

    @task
    def summarize_gathered_information(self) -> Task:
        return Task(
            config=self.tasks_config['summarize_gathered_information'],
            
        )

    @task
    def store_chat_history_and_information(self) -> Task:
        return Task(
            config=self.tasks_config['store_chat_history_and_information'],
            
        )


    @crew
    def crew(self) -> Crew:
        """Creates the BuildingAnAiAgentForWebSearchAndInformationGathering crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )

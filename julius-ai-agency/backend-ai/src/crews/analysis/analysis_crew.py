from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class AnalysisCrew:
    """Analysis Crew"""
    agents_config = '../../config/agents.yaml'
    tasks_config = '../../config/tasks.yaml'

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True
        )

    @agent
    def data_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['data_analyst'],
            verbose=True
        )

    @agent
    def insights_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['insights_specialist'],
            verbose=True
        )

    @task
    def market_research(self) -> Task:
        return Task(
            config=self.tasks_config['market_research'],
            agent=self.researcher()
        )

    @task
    def data_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['data_analysis'],
            agent=self.data_analyst(),
            context=[self.market_research()]
        )

    @task
    def strategic_report(self) -> Task:
        return Task(
            config=self.tasks_config['strategic_report'],
            agent=self.insights_specialist(),
            context=[self.data_analysis()]
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents, # Automatically collected by the @agent decorator
            tasks=self.tasks,   # Automatically collected by the @task decorator
            process=Process.sequential,
            verbose=True,
        )

    def run(self, topic: str):
        inputs = {'topic': topic}
        # The kickoff method in newer CrewAI versions takes inputs dict
        return self.crew().kickoff(inputs=inputs)

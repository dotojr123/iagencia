from crewai import Agent

class SupervisorAgent:
    def __init__(self):
        self.agent = Agent(
            role='Agency Supervisor',
            goal='Orchestrate the agency teams to deliver the best results for the client.',
            backstory="You are the head of the Jules AI Agency. You receive client requests and decide which team (Analysis, Development, etc.) should handle them.",
            verbose=True,
            allow_delegation=True
        )

    def route_task(self, task_description: str) -> str:
        """
        Analyzes the task and returns the name of the sector that should handle it.
        Possible sectors: 'analysis', 'development', 'marketing'.
        """
        # In a real implementation, we would use the LLM to decide.
        # For this boilerplate, we'll do a simple keyword check or prompt the LLM.

        # Simple Mock Logic for v1
        task_lower = task_description.lower()
        if "analyze" in task_lower or "research" in task_lower or "report" in task_lower:
            return "analysis"
        elif "code" in task_lower or "app" in task_lower or "develop" in task_lower:
            return "development"
        else:
            return "general"

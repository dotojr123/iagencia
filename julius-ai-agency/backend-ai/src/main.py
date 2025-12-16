from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.crews.analysis.analysis_crew import AnalysisCrew
from src.agents.supervisor import SupervisorAgent
import os

app = FastAPI(title="Jules AI Agency API", version="1.0.0")

class AgencyRequest(BaseModel):
    task: str
    topic: str = None # Optional topic for specific crews

@app.get("/")
def read_root():
    return {"status": "online", "agency": "Jules v1.0"}

@app.post("/agency/dispatch")
def dispatch_task(request: AgencyRequest):
    """
    Main entry point for the Agency.
    The Supervisor decides which crew to run based on the task description.
    """
    try:
        supervisor = SupervisorAgent()
        # Decide sector
        sector = supervisor.route_task(request.task)

        result = None
        if sector == "analysis":
            # If topic is not provided, try to extract it from task (mock)
            topic = request.topic or request.task
            crew = AnalysisCrew()
            result = crew.run(topic)
            return {
                "supervisor_decision": "Routed to Analysis Sector",
                "crew_output": result
            }

        elif sector == "development":
            return {
                "supervisor_decision": "Routed to Development Sector",
                "status": "Development Crew not yet implemented in v1.0"
            }

        else:
             return {
                "supervisor_decision": "General Task",
                "status": "Handled by Generalist Agent (Mock)"
            }

    except Exception as e:
        # Log error in production
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

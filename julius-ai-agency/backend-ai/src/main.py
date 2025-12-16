from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.crews.analysis.analysis_crew import AnalysisCrew
from src.agents.supervisor import SupervisorAgent
import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("JulesAPI")

app = FastAPI(title="Jules AI Agency API", version="1.0.0", docs_url="/docs", redoc_url="/redoc")

# CORS Configuration
allowed_origins_env = os.getenv("ALLOWED_ORIGINS", "*")
origins = allowed_origins_env.split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AgencyRequest(BaseModel):
    task: str
    topic: str = None

@app.get("/")
def read_root():
    """Health check endpoint."""
    return {"status": "online", "agency": "Jules v1.0", "version": "1.0.0"}

@app.post("/agency/dispatch")
def dispatch_task(request: AgencyRequest):
    """
    Main entry point for the Agency.
    """
    logger.info(f"Received task: {request.task}")
    try:
        supervisor = SupervisorAgent()
        sector = supervisor.route_task(request.task)
        logger.info(f"Supervisor routed to sector: {sector}")

        if sector == "analysis":
            topic = request.topic or request.task
            crew = AnalysisCrew()
            result = crew.run(topic)
            return {
                "supervisor_decision": "Routed to Analysis Sector",
                "crew_output": str(result)
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
        logger.error(f"Error executing task: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))

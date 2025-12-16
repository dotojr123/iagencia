import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def test_imports():
    from src.crews.analysis.analysis_crew import AnalysisCrew
    from src.agents.supervisor import SupervisorAgent
    from src.main import app
    assert AnalysisCrew is not None
    assert SupervisorAgent is not None
    assert app is not None
    print("All imports successful")

if __name__ == "__main__":
    test_imports()

class BaseAgent:
    """
    Base class for all Genesis AI Venture Builder agents.
    Provides a common identity and response structure.
    """

    def __init__(self, name, mission):
        self.name = name
        self.mission = mission

    def analyze(self, request):
        return {
            "agent": self.name,
            "mission": self.mission,
            "request": request,
            "findings": [],
            "recommendations": [],
            "confidence_score": 0.0
        }

    def describe(self):
        return {
            "agent": self.name,
            "mission": self.mission
        }

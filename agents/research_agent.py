from agents.base_agent import BaseAgent


class ResearchAgent(BaseAgent):
    """
    Research Intelligence Agent.
    Discovers market opportunities, problems, and possible solutions.
    """

    def __init__(self):
        super().__init__(
            name="Research Intelligence Agent",
            mission="Analyze markets, identify problems, opportunities, and research directions."
        )

    def analyze(self, niche):

        report = {
            "agent": self.name,
            "mission": self.mission,
            "research_topic": niche,
            "sources_to_investigate": [
                "Academic research papers",
                "Industry reports",
                "Books",
                "Professional articles",
                "Online communities",
                "Market trends"
            ],
            "research_questions": [
                "What problem does this niche solve?",
                "Who needs this solution?",
                "What solutions already exist?",
                "What opportunity gaps exist?",
                "What digital products can be created?"
            ],
            "research_status": "Ready for source collection.",
            "confidence_score": 0.0
        }

        return report

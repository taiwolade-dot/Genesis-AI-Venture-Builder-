from rich import print
from agents.base_agent import BaseAgent


class NicheAgent(BaseAgent):
    """
    Market Niche Discovery Agent.
    Identifies promising business opportunities and target audiences.
    """

    def __init__(self):
        super().__init__(
            name="Niche Discovery Agent",
            mission="Identify profitable niches, target audiences, and digital product opportunities."
        )

    def analyze(self, idea):

        report = {
            "agent": self.name,
            "mission": self.mission,
            "idea": idea,
            "recommended_niche": "AI-Powered Ministry Leadership Training",
            "problem_identified": (
                "Many church leaders want to use artificial intelligence "
                "but need practical, ethical, and ministry-focused guidance."
            ),
            "target_audience": [
                "Pastors",
                "Church administrators",
                "Seminary students",
                "Christian educators"
            ],
            "possible_digital_products": [
                "Ebook",
                "Online Course",
                "Workshop",
                "AI Ministry Prompt Library"
            ],
            "demand_score": "90/100",
            "competition": "Moderate",
            "opportunity": "HIGH",
            "recommendation": "Proceed to research stage."
        }

        return report


if __name__ == "__main__":

    agent = NicheAgent()

    idea = input("Enter idea: ")

    result = agent.analyze(idea)

    print(result)

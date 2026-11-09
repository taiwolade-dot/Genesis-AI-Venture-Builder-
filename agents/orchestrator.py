from agents.niche_agent import NicheAgent
from agents.research_agent import ResearchAgent


class Orchestrator:

    def __init__(self):
        self.niche_agent = NicheAgent()
        self.research_agent = ResearchAgent()


    def create_venture_report(self, idea):

        print("\nGenesis AI CEO Agent")
        print("Analyzing your idea...")


        niche_report = self.niche_agent.analyze(idea)


        research_report = self.research_agent.analyze(
            "AI-Powered Ministry Leadership Training"
        )


        final_report = f"""

=============================
GENESIS AI VENTURE REPORT
=============================


{niche_report}


{research_report}

"""

        return final_report

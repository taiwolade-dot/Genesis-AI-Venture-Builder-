from agents.base_agent import BaseAgent
from agents.niche_agent import NicheAgent
from agents.research_agent import ResearchAgent
from agents.creator_agent import CreatorPartnershipAgent


class Orchestrator(BaseAgent):
    """
    Genesis AI CEO Orchestrator Agent.
    Coordinates specialized agents to build venture intelligence.
    """

    def __init__(self):

        super().__init__(
            name="Genesis AI CEO Agent",
            mission="Coordinate AI agents to analyze ideas and generate venture strategies."
        )

        self.niche_agent = NicheAgent()
        self.research_agent = ResearchAgent()
        self.creator_agent = CreatorPartnershipAgent()


    def create_venture_report(self, idea):

        print("\nGenesis AI CEO Agent")
        print("Analyzing your idea...")


        niche_report = self.niche_agent.analyze(idea)


        research_topic = niche_report["recommended_niche"]


        research_report = self.research_agent.analyze(
            research_topic
        )


        creator_report = self.creator_agent.analyze(
            research_topic
        )


        final_report = {

            "agent": self.name,

            "mission": self.mission,

            "idea": idea,

            "niche": niche_report,

            "research": research_report,

            "creator_partnership": creator_report,

            "next_stage": "Product strategy development and creator distribution"

        }


        return final_report



if __name__ == "__main__":

    agent = Orchestrator()

    idea = input("Enter venture idea: ")

    report = agent.create_venture_report(idea)

    print(report)

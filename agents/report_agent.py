from agents.base_agent import BaseAgent


class ReportIntelligenceAgent(BaseAgent):
    """
    Converts venture intelligence from multiple agents
    into a structured business report.
    """

    def __init__(self):
        super().__init__(
            name="Report Intelligence Agent",
            mission="Generate professional venture reports from AI agent insights."
        )


    def analyze(self, venture_data):

        niche = venture_data.get("niche", {})
        research = venture_data.get("research", {})
        product = venture_data.get("product", {})
        creator = venture_data.get("creator_partnership", {})

        return {

            "agent": self.name,

            "mission": self.mission,


            "executive_summary": {

                "opportunity": niche.get(
                    "recommended_niche",
                    "Emerging opportunity"
                ),

                "problem": niche.get(
                    "problem_identified",
                    "Problem analysis unavailable"
                ),

                "target_market": niche.get(
                    "target_audience",
                    []
                )
            },


            "market_opportunity": {

                "demand_score": niche.get(
                    "demand_score",
                    "Not available"
                ),

                "competition": niche.get(
                    "competition",
                    "Unknown"
                ),

                "research_status": research.get(
                    "research_status",
                    "Pending"
                )
            },


            "product_strategy": {

                "product_name": product.get(
                    "product_name",
                    "Product not defined"
                ),

                "formats": product.get(
                    "product_formats",
                    []
                ),

                "pricing": product.get(
                    "pricing_strategy",
                    {}
                ),

                "monetization": product.get(
                    "monetization_models",
                    []
                )
            },


            "growth_strategy": {

                "partnership_models": creator.get(
                    "partnership_models",
                    []
                ),

                "distribution": creator.get(
                    "whop_strategy",
                    {}
                )
            },


            "launch_readiness":
                "Ready for validation and execution."

        }

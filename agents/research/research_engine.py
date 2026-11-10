from agents.research.source_database import ResearchSourceDatabase


class ResearchEngine:

    def __init__(self):
        self.database = ResearchSourceDatabase()


    def generate_research(self, topic):

        sources = [

            {
                "title": f"Academic studies on {topic}",
                "category": "Academic Research",
                "source_type": "Research Paper",
                "author": "Academic Researchers",
                "year": 2025,
                "insight": "Identify theoretical foundations and evidence.",
                "relevance_score": 95
            },

            {
                "title": f"Industry trends in {topic}",
                "category": "Industry Report",
                "source_type": "Market Report",
                "author": "Industry Analysts",
                "year": 2025,
                "insight": "Understand market growth and adoption patterns.",
                "relevance_score": 90
            },

            {
                "title": f"Books and expert knowledge about {topic}",
                "category": "Books",
                "source_type": "Professional Literature",
                "author": "Subject Matter Experts",
                "year": 2024,
                "insight": "Extract established principles and best practices.",
                "relevance_score": 85
            },

            {
                "title": f"Existing solutions for {topic}",
                "category": "Competitor Research",
                "source_type": "Competitive Analysis",
                "author": "Market Research",
                "year": 2025,
                "insight": "Identify competitors and opportunity gaps.",
                "relevance_score": 92
            },

            {
                "title": f"Communities discussing {topic}",
                "category": "Community Research",
                "source_type": "Online Communities",
                "author": "Community Members",
                "year": 2025,
                "insight": "Discover user needs, questions, and pain points.",
                "relevance_score": 88
            },

            {
                "title": f"Future trends affecting {topic}",
                "category": "Market Trends",
                "source_type": "Trend Analysis",
                "author": "Market Analysts",
                "year": 2025,
                "insight": "Identify future opportunities and risks.",
                "relevance_score": 91
            }

        ]


        for source in sources:
            self.database.add_source(**source)


        return self.database.get_sources()

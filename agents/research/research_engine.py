from agents.research.source_database import ResearchSourceDatabase


class ResearchEngine:

    def __init__(self):
        self.database = ResearchSourceDatabase()


    def generate_research(self, topic):

        self.database.add_source(
            title=f"Academic studies on {topic}",
            category="Academic Research",
            year=2025,
            insight="Identify theoretical foundations and evidence."
        )

        self.database.add_source(
            title=f"Industry trends in {topic}",
            category="Industry Report",
            year=2025,
            insight="Understand market growth and adoption."
        )

        self.database.add_source(
            title=f"Existing solutions for {topic}",
            category="Competitor Research",
            year=2025,
            insight="Identify gaps and opportunities."
        )

        return self.database.get_sources()

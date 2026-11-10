class ResearchSourceDatabase:

    def __init__(self):
        self.sources = []


    def add_source(
        self,
        title,
        category,
        insight,
        year=None
    ):

        self.sources.append({
            "title": title,
            "category": category,
            "year": year,
            "insight": insight
        })


    def get_sources(self):
        return self.sources

class ResearchSourceDatabase:

    def __init__(self):
        self.sources = []


    def add_source(
        self,
        title,
        category,
        insight,
        year=None,
        author=None,
        source_type=None,
        url=None,
        relevance_score=0
    ):

        self.sources.append({
            "title": title,
            "category": category,
            "year": year,
            "author": author,
            "source_type": source_type,
            "url": url,
            "insight": insight,
            "relevance_score": relevance_score
        })


    def get_sources(self):
        return self.sources

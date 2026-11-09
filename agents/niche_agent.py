from rich import print


class NicheAgent:

    def analyze(self, idea):

        report = f"""
GENESIS AI MARKET REPORT

Idea:
{idea}

Recommended Niche:
AI-Powered Ministry Leadership Training

Problem Identified:
Many church leaders want to use artificial intelligence but need practical, ethical, and ministry-focused guidance.

Target Audience:
- Pastors
- Church administrators
- Seminary students
- Christian educators

Possible Digital Products:
1. Ebook
2. Online Course
3. Workshop
4. AI Ministry Prompt Library

Demand Score:
90/100

Competition:
Moderate

Opportunity:
HIGH

Recommendation:
Proceed to research stage.
"""

        return report


if __name__ == "__main__":

    agent = NicheAgent()

    idea = input("Enter idea: ")

    result = agent.analyze(idea)

    print(result)

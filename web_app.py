from flask import Flask, render_template, request
from agents.orchestrator import Orchestrator

app = Flask(__name__)

ceo = Orchestrator()


@app.route("/", methods=["GET", "POST"])
def home():

    report = None

    if request.method == "POST":

        idea = request.form["idea"]

        result = ceo.create_venture_report(idea)

        report = {
            "idea": result["idea"],
            "agent": result["agent"],
            "mission": result["mission"],
            "niche": result["niche_analysis"],
            "research": result["research_analysis"],
            "next_stage": result["next_stage"]
        }

    return render_template(
        "index.html",
        report=report
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

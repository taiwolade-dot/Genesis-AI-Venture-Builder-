from flask import Flask, render_template, request, jsonify
from agents.orchestrator import Orchestrator

app = Flask(__name__)

ceo = Orchestrator()


@app.route("/", methods=["GET", "POST"])
def home():

    report = None

    if request.method == "POST":

        idea = request.form["idea"]

        result = ceo.create_venture_report(idea)

        print(result)

        report = result

    return render_template(
        "index.html",
        report=report
    )


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    idea = data.get("idea")

    result = ceo.create_venture_report(idea)

    return jsonify({
        "status": "complete",
        "agents": {
            "ceo": "completed",
            "niche": "completed",
            "research": "completed"
        },
        "report": result
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )

from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

crowd_data = []
THRESHOLD = 5


@app.route("/")
def dashboard():
    return render_template("dashboard.html", threshold=THRESHOLD)


@app.route("/update", methods=["POST"])
def update():

    data = request.json
    count = data.get("count", 0)

    crowd_data.append({
        "time": datetime.now().strftime("%H:%M:%S"),
        "count": count
    })

    if len(crowd_data) > 50:
        crowd_data.pop(0)

    return jsonify({"status": "received"})


@app.route("/data")
def data():
    return jsonify(crowd_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
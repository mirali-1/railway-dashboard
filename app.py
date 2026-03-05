from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

crowd_data = []

@app.route("/")
def dashboard():
    return render_template("dashboard.html", data=crowd_data)

@app.route("/update", methods=["POST"])
def update():

    data = request.json

    crowd_data.append({
        "count": data["count"],
        "time": datetime.now().strftime("%H:%M:%S")
    })

    if len(crowd_data) > 50:
        crowd_data.pop(0)

    return jsonify({"status":"ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
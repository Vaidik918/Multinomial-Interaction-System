# backend/server.py
from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/run-system", methods=["POST"])
def run_system():
    subprocess.Popen(["python", "main.py"])
    return jsonify({"status": "System started"})

if __name__ == '__main__':
    app.run(debug=True)


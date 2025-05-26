# secure_app/app.py

from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the vulnerable Flask app!"

@app.route("/ping")
def ping():
    # Simple health check
    return "pong"

@app.route("/vuln")
def vuln():
    """
    Simulated vulnerable endpoint for testing DevSecOps pipelines.
    DO NOT use eval in production. This is for Bandit/Semgrep detection.
    """
    user_input = request.args.get("input", "")
    
    # WARNING: Deliberate insecure use of eval
    try:
        result = eval(user_input)
        return str(result)
    except Exception as e:
        return f"Error in input: {e}"

# TODO: Add logging and input validation for safe version

if __name__ == "__main__":
    # Run in debug mode for development only
    app.run(debug=True, host="0.0.0.0", port=5000)

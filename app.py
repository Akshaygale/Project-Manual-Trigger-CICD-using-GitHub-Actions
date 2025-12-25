from flask import Flask
import datetime

app = Flask(__name__)

with open("VERSION") as f:
    VERSION = f.read().strip()

@app.route("/")
def home():
    now = datetime.datetime.now()
    return f"""
    <h1>CI/CD Auto Deployment Successful 🚀</h1>
    <h3>Version: {VERSION}</h3>
    <p>Server Time: {now}</p>
    """

app.run(host="0.0.0.0", port=5000)

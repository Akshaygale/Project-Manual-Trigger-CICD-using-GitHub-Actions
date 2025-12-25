from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    now = datetime.datetime.now()
    return f"""
    <h1>CI/CD Auto Deployment Successful 🚀</h1>
    <p>Server Time: {now}</p>
    """

app.run(host="0.0.0.0", port=5000)

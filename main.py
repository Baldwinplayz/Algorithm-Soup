import requests
import json
from flask import Flask
from render_template import render_template

app = Flask(__name__)

import sorting
import searching

@app.route("/")
def index():
    return render_template(0, "pages/index.html", "Algorithm Soup")

@app.route("/ip")
def ip():
    return json.loads(requests.get("https://api.ipify.org?format=json").text)["ip"]

if "__main__" == __name__:
    app.run(host="0.0.0.0", port=80, debug=True)
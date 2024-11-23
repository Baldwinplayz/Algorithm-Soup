from flask import Flask
from render_template import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(0, "pages/index.html")

if "__main__" == __name__:
    app.run(host="0.0.0.0", port=8080, debug=True)
from __main__ import app
from render_template import render_template

@app.route("/searching")
def searching():
    return render_template(0, "pages/searching/index.html", "Searching Algorithm List")

#######################################################################################

@app.route("/searching/complete_search")
def complete_search():
    return render_template(0, "pages/searching/complete_search.html", "Complete Search")

@app.route("/searching/complete_search/embbed")
def complete_search_embbed():
    return render_template(-1, "pages/searching/complete_search_embbed.html", "Complete Search")
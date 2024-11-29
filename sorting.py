from __main__ import app
from render_template import render_template

@app.route("/sorting")
def sorting():
    return render_template(0, "pages/sorting/index.html")

#######################################################################################

@app.route("/sorting/number_sort")
def number_sorting():
    return render_template(0, "pages/sorting/number_sort.html")

@app.route("/sorting/number_sort/embbed")
def number_sorting_embbed():
    return render_template(-1, "pages/sorting/number_sort_embbed.html")

#######################################################################################

@app.route("/sorting/word_sort")
def word_sort():
    return render_template(0, "pages/sorting/word_sort.html")

@app.route("/sorting/word_sort/embbed")
def word_sort_embbed():
    return render_template(-1, "pages/sorting/word_sort_embbed.html")

#######################################################################################

@app.route("/sorting/sentence_sort")
def sentence_sort():
    return render_template(0, "pages/sorting/sentence_sort.html")

@app.route("/sorting/sentence_sort/embbed")
def sentence_sort_embbed():
    return render_template(-1, "pages/sorting/sentence_sort_embbed.html")

#######################################################################################

@app.route("/sorting/sentence_lenght_sort")
def sentence_sort_lenght():
    return render_template(0, "pages/sorting/sentence_lenght_sort.html")

@app.route("/sorting/sentence_lenght_sort/embbed")
def sentence_sort_lenght_embbed():
    return render_template(-1, "pages/sorting/sentence_lenght_sort_embbed.html")
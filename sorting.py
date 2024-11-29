from __main__ import app
from render_template import render_template

@app.route("/sorting")
def sorting():
    return render_template(0, "pages/sorting/index.html", "Sorting Algorithm List")

#######################################################################################

@app.route("/sorting/number_sort")
def number_sorting():
    return render_template(0, "pages/sorting/number_sort.html", "Number Sort")

@app.route("/sorting/number_sort/embbed")
def number_sorting_embbed():
    return render_template(-1, "pages/sorting/number_sort_embbed.html", "Number Sort")

#######################################################################################

@app.route("/sorting/word_sort")
def word_sort():
    return render_template(0, "pages/sorting/word_sort.html", "Word Sort")

@app.route("/sorting/word_sort/embbed")
def word_sort_embbed():
    return render_template(-1, "pages/sorting/word_sort_embbed.html", "Word Sort")

#######################################################################################

@app.route("/sorting/sentence_sort")
def sentence_sort():
    return render_template(0, "pages/sorting/sentence_sort.html", "Sentence Sort")

@app.route("/sorting/sentence_sort/embbed")
def sentence_sort_embbed():
    return render_template(-1, "pages/sorting/sentence_sort_embbed.html", "Sentence Sort")

#######################################################################################

@app.route("/sorting/sentence_length_sort")
def sentence_sort_length():
    return render_template(0, "pages/sorting/sentence_length_sort.html", "Sentence Length Sort")

@app.route("/sorting/sentence_length_sort/embbed")
def sentence_sort_length_embbed():
    return render_template(-1, "pages/sorting/sentence_length_sort_embbed.html", "Sentence Length Sort")
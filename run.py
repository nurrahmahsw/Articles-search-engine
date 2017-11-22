from flask import Flask, render_template, redirect, Markup
from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, SubmitField
from stki_scripts.main import findSim, findCosine, findManhattan_distance, findJaccard_similarity, findPearson_correlation

app = Flask(__name__)
app.config.update(dict(SECRET_KEY='12345'))

class SearchTask(FlaskForm):
    keyword = TextField('Keyword')
    search = SubmitField('Search')
    search2 = SubmitField('Search2')
    search3 = SubmitField('Search3')
    search4 = SubmitField('Search4')
    search5 = SubmitField('Search5')

def searchTask(form):
    keyword = form.keyword.data
    path_corpus = "./text files"
    res = findSim(keyword, path_corpus)
    return res

def searchTask2(form):
    keyword = form.keyword.data
    path_corpus = "./text files"
    res = findCosine(keyword, path_corpus)
    return res

def searchTask3(form):
    keyword = form.keyword.data
    path_corpus = "./text files"
    res = findManhattan_distance(keyword, path_corpus)
    return res
def searchTask4(form):
    keyword = form.keyword.data
    path_corpus = "./text files"
    res = findJaccard_similarity(keyword, path_corpus)
    return res
def searchTask5(form):
    keyword = form.keyword.data
    path_corpus = "./text files"
    res = findPearson_correlation(keyword, path_corpus)
    return res

@app.route('/', methods=['GET','POST'])
def main():
    # create form
    sform = SearchTask(prefix='sform')

    # get response
    data = {}
    if sform.validate_on_submit() and sform.search.data:
        data = searchTask(sform)
    elif sform.validate_on_submit() and sform.search2.data:
        data = searchTask2(sform)
    elif sform.validate_on_submit() and sform.search3.data:
        data = searchTask3(sform)
    elif sform.validate_on_submit() and sform.search4.data:
        data = searchTask4(sform)
    elif sform.validate_on_submit() and sform.search5.data:
        data = searchTask5(sform)


    # render HTML
    return render_template('index.html', sform = sform, data = data)

if __name__=='__main__':
    app.run(debug=True)

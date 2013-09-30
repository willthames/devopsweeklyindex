from flask import Flask, render_template, request
from whoosh.qparser import QueryParser
from whoosh.index import open_dir
import os

app = Flask(__name__)


@app.route('/')
def search():
    if request.method == 'GET':
        querystring = request.args.get('q')
    if request.method == 'POST':
        querystring = request.form.get('q')
    if querystring:
        indexdir = os.path.join(os.path.dirname(__file__), '..', 'index')
        ix = open_dir(indexdir, indexname="contents")
        qp = QueryParser("content", schema=ix.schema)
        q = qp.parse(querystring)
        
        with ix.searcher(closereader=False) as s:
            results = s.search(q, limit=100)
            return render_template('results.html', results=results, querystring=querystring)
    else: 
        return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True)

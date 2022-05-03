from flask import render_template
from app import app
from  .request import get_sources

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    sources = get_sources()
    title = 'People News'
    return render_template('index.html', title = title, sources = sources)
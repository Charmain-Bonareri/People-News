from flask import render_template
from app import app
from  .request import get_sources
import os


imagesFolder = os.path.join('static','images')

app.config['UPLOAD_FOLDER'] = imagesFolder

# Views
@app.route('/')
def index():
    header=os.path.join(app.config['UPLOAD_FOLDER'], 'header.jpg')

    '''
    View root page function that returns the index page and its data
    '''
    sources = get_sources()
    title = 'People News'
    return render_template('index.html', title = title, sources = sources, user_image = header)
from flask import render_template
from . import main
from  ..request import get_sources, get_articles
import os


imagesFolder = os.path.join('static','images')

main.config['UPLOAD_FOLDER'] = imagesFolder

# Views
@main.route('/')
def index():
    header=os.path.join(main.config['UPLOAD_FOLDER'], 'header.jpg')

    '''
    View root page function that returns the index page and its data
    '''
    sources = get_sources()
    title = 'People News'
    return render_template('index.html', title = title, sources = sources, user_image = header)

@main.route('/articles/<sources_id>')
def articles(sources_id):
    '''
    View articles page function that returns the  article details page and its data
    '''
    articles = get_articles(sources_id)
    
    return render_template('articles.html',articles = articles)
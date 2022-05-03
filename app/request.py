import urllib.request,json
from .models import Sources

#Getting the API key
api_key=None

# Getting the news base url
base_url=None

# Getting the news source url
source_url=None


def configure_request(app):
    global api_key,base_url,sources_url,articles_url
    api_key = app.config['NEWS_API_KEY']
    sources_url = app.config['NEWS_API_SOURCES_URL']
    articles_url = app.config['NEWS_API_ARTICLES_URL']
    
def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = 'https://newsapi.org/v2/sources?apiKey=7ff84f7f5d3f43ab99b610a6ddaf9e72'

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)
            
def process_sources(sources_list):
    '''
    Function  that processes the source result and transform them to a list of Objects
    Args:
        source_list: A list of dictionaries that contain source details
    Returns :
        sources_results: A list of source objects
    '''
    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        title = sources_item.get('title')
        category = sources_item.get('category')
        description = sources_item.get('description')
       
       
        sources_object = Sources(id,title,category,description)
        sources_results.append(sources_object)
        sources_results=sources_results[:4]

    return sources_results
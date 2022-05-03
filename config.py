import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL="https://newsapi.org/v2/{}?country=us&apiKey={}"
    NEWS_API_ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_KEY = '7ff84f7f5d3f43ab99b610a6ddaf9e72'
    SECRET_KEY='Flask WTF Secret Key'




class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}
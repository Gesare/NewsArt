import os

class Config:
    '''
    General configuration parent class.
    '''
    NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
   	ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
   	NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
@staticmethod
def init_app(app):
pass
    
class ProdConfig(Config):
    '''
    Production configuration child class.

    Args:
        Config: The parent configuration class with General configuration setting
    '''
    pass
class DevConfig(Config):
    '''
    Development configuration child class.

    Args:
        Config: The parent configuration class with General configuration setting
    '''
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
}
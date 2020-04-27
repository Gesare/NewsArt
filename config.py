import os

class Config:
    
    NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
    SECRET_KEY = os.environ.get('SECRET_KEY')

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
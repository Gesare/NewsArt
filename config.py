import os

class Config:
    '''
    General configuration parent class.
    '''
    SOURCES_API_BASE_URL= 'https://newsapi.org/v2/sources?apiKey={2714546ac97147e8b6f08a912e752e90}'
    SOURCE_ARTICLES_BASE_URL='https://newsapi.org/v2/everything?sources={}&apiKey={2714546ac97147e8b6f08a912e752e90}'
    NEW_API_KEY = os.environ.get('NEW_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
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
import os

class Config:
    
    SOURCES_BASE_URL='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    # ARTICLES_BASE_URL='https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
    ARTICLES_BASE_URL='https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
    SOURCES_API_KEY='644e5bbd1acf46bca21a48a9e32e08dd'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}
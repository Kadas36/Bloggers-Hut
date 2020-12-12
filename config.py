import os

class Config:
    
   '''
   General configuration parent class
   '''
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:kadas36@localhost/bloggers'
   SECRET_KEY = os.environ.get('SECRET_KEY')

   

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:kadas36@localhost/bloggers'
   DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}         
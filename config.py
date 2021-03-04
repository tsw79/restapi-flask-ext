from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class BaseConfig:
  # FLASK_APP = main
  JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY')
  SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
  # Mail settings (Gmail specific)
  MAIL_SERVER = "smtp.gmail.com"
  MAIL_PORT = 465
  MAIL_USE_TLS = False
  MAIL_USE_SSL = True
  MAIL_SUPPRESS_SEND = False
  MAIL_USERNAME = environ.get('MAIL_USERNAME')
  MAIL_PASSWORD = environ.get('MAIL_PASSWORD')

class DevelopmentConf(BaseConfig):
  FLASK_ENV = 'development'
  DEBUG = True
  TESTING = True
  DATABASE_URI = environ.get('DEV_DATABASE_URI')

class ProductionConf(BaseConfig):
  FLASK_ENV = 'production'
  DEBUG = False
  TESTING = False
  DATABASE_URI = environ.get('PROD_DATABASE_URI')

from os import environ, path
from dotenv import load_dotenv
from datetime import timedelta



# get absolute file path in current directory
basedir = path.abspath(path.dirname(__file__))

# load environment variables
load_dotenv(path.join(basedir, '.env'))

# retrieve env variables and assign to constants
CLIENT_ID = environ.get('client_id')
CLIENT_SECRET = environ.get('client_secret')
REDIRECT_URI = environ.get('redirect_uri')
SCOPE = environ.get('scope')
USER_ID = environ.get('user_id')


# Configuration Classes for Flask app parameters
class Config:
    """ Base Setup  """
    SECRET_KEY = environ.get('secret_key')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


class DevConfig(Config):
    """ Development Setup """
    ENV = 'development'
    DEBUG = True
    PERMANENT_SESSION_LIFETIME = timedelta(days=31)
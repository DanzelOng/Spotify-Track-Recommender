from flask import Flask
from .config import DevConfig



# create Flask app
app = Flask(__name__)

# configure app
app.config.from_object(DevConfig)

# import routes 
from . import routes

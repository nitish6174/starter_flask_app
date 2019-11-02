from flask import Blueprint
from flask_pymongo import PyMongo

# MongoDB client
pymongo = PyMongo()

# Flask blueprints
routes_module = Blueprint("routes_module", __name__)

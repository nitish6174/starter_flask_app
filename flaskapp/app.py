# External modules
from flask import Flask, send_from_directory
from flask_assets import Environment
from flask_compress import Compress
# Local modules
from flaskapp import config, constants as C, shared_variables as var
from flaskapp.assets import get_assets
from flaskapp.routes import routes_module


# Initialize flask app
app = Flask(__name__)

# Gzip compression
Compress(app)

# App configuration
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = config.STATIC_FILE_MAX_AGE
app.config['UPLOAD_FOLDER'] = config.UPLOADS_DIR

# MongoDB
app.config["MONGO_HOST"] = config.MONGO_HOST
app.config["MONGO_PORT"] = config.MONGO_PORT
app.config["MONGO_DBNAME"] = config.MONGO_NAME
# Uncomment below line to connect to mongo
# var.pymongo.init_app(app, config_prefix="MONGO")

# Add assets to app
assets = Environment(app)
assets.register(get_assets())

# Add app routes
app.url_map.strict_slashes = False
app.register_blueprint(routes_module)


# Uncomment and configure below function to enable downloading static files
# @app.route('/datafile/<path:filename>')
# def downloadFile(filename):
#     return send_from_directory(app.static_folder + config.DOWNLOADS_DIR, filename)

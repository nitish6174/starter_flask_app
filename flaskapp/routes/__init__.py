# External modules
from flask import request
# Local modules
from flaskapp.shared_variables import routes_module
from flaskapp.routes.api_routes import *
from flaskapp.routes.view_routes import *


# Redirect to non-trailing slash path
@routes_module.before_request
def clear_trailing():
    rp = request.path
    if rp != '/' and rp.endswith('/'):
        return redirect(rp[:-1], code=301)

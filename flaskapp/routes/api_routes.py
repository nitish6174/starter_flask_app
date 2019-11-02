# External modules
import json
import random
# Local modules
from flaskapp.shared_variables import routes_module


@routes_module.route("/api/user_info/<user_id>", methods=["GET", "POST"])
def user_data_api(user_id):
    user_data = {
        'id': user_id,
        'name': str(user_id).capitalize(),
        'rating': random.randint(1, 10)
    }
    return json.dumps(user_data, sort_keys=True)

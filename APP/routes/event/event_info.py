from flask import Blueprint, request, make_response, jsonify
from ...utils.jwt import JWT
from ...models import Event

event_info_bp = Blueprint('event_info', __name__, url_prefix="/event_info")

# This will be post request containing the jwt token
# fetching the user with all the details of the event
@event_info_bp.route("/<id>/", methods=["POST"])
@event_info_bp.route("/<id>", methods=["POST"])
def event_info(id):
	data = request.get_json()

	if not "token" in data:
		return make_response(jsonify({"message":"Unauthorized access."}), 401)

	userData = JWT.validator(data["token"])

	if not userData:
		return make_response(jsonify({"message":"Unauthorized access."}), 401)
	
	Event.query.get(id)

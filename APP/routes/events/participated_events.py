from flask import Blueprint, request, make_response, jsonify
from ...utils import access_required, JWT
from ...models import User

participation_bp = Blueprint("participation",__name__,url_prefix="/participation")

@participation_bp.route("/")
@participation_bp.route("")
@access_required(4)
def get_participations():
	token_dict = JWT.validator(request.cookies.get("token"))
	user_id = token_dict["id"]
	user = User.query.get(user_id)
	participations = []
	for event in user.events_participated:
		participations.append({
            "id":event.id,
            "title":event.title,
            "type":event.type,
            "organiser":event.organiser.name,
            "tag":event.event_tags,
            "start":event.start,
            "end":event.end,
			"certificate":event.participation_certificate.decode("utf-8") if event.participation_certificate else None
        })
	return make_response(jsonify(participations=participations, message="Success"))
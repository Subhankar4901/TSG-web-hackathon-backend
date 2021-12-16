from flask import Blueprint,request,jsonify,make_response
from ...models import Achievement
from ...utils import JWT
from ... import db

delete_achievement_bp = Blueprint("delete_achievement",__name__,url_prefix="/delete")

# request body contains token and id of achievement
@delete_achievement_bp.route("/", methods=["POST"])
def delete_achievement():
	data = request.get_json()
	token = data.get("token")
	achievement_id = data.get("achievement_id")
	token_dict = JWT.validator(token)
	if token_dict and achievement_id:
		achievement_obj = Achievement.query.get(achievement_id)
		if achievement_obj and ((token_dict["type"] < 3) or ((token_dict["type"]==3) and (achievement_obj.event.organiser.id==token_dict["id"]))):
			db.session.delete(achievement_obj)
			db.session.commit()
			return make_response(jsonify(message="achievement deleted")) 
	return make_response(jsonify(message="Invalid request"), 401) 
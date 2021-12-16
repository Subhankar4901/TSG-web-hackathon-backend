from .add_achievement import addAchievement
from .delete_achievement import delete_achievement
from flask import Blueprint,request,jsonify,make_response
from ...models.Achievement import Achievement
from ...utils import JWT
from ... import db

update_achievement_bp = Blueprint("update_achievement",__name__,url_prefix="/update")

# request body contains token and id of achievement
@update_achievement_bp.route("/", methods=["POST"])
def update_achievement():
	resp = delete_achievement()
	if (resp.status == 401):
		return resp
	addAchievement()
	return make_response(jsonify(message="achievement updated"))
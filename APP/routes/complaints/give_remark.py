from flask import Blueprint, json, request, make_response, jsonify
from ...models import Complain
from ...utils.jwt import JWT
from ...models import Complain
from ... import db

remark_bp = Blueprint('remark', __name__, url_prefix="/addRemark")

@remark_bp.route("/", methods=["POST"])
@remark_bp.route("", methods=["POST"])
def giveRemark():
	data = request.get_json()
	token = request.cookies.get("token")
	complain_id = data.get("complain_id")
	remarks = data.get("remark")
	token_dict = JWT.validator(token)
	if token_dict and complain_id and remarks:
		user_type = token_dict.get("type")
		if user_type < 3:
			complain_row = Complain.query.get(complain_id)
			complain_row.remarks = remarks
			db.session.add(complain_row)
			db.session.commit()
			return make_response(jsonify(message=f"remark updated as `{remarks}`"))
	return make_response(jsonify(message="Invalid request"), 401)

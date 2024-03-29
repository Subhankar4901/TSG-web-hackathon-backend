from flask import Blueprint, jsonify,request,make_response
from ....utils import JWT
from ....models import User

fetch_bp = Blueprint('fetchUser', __name__, url_prefix="/token")

@fetch_bp.route("/", methods=["POST"])
@fetch_bp.route("", methods=["POST"])
def fetchWithToken():
	token = request.cookies.get('token')
	token_dict = JWT.validator(token)
	if token_dict:
		user = User.query.get(token_dict['id'])
		return make_response(jsonify(user={
			'name':user.name,
			'type':user.type,
			'roll':user.roll,
			'email':user.email,
			# 'photo':user.photo.decode('utf-8') to be handled
		}))
	return make_response(jsonify(message="token invalid"), 401)

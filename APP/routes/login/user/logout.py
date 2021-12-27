from flask import Blueprint, jsonify,request,make_response
from ....utils import JWT
from ....models import User

logout_bp = Blueprint('logoutUser', __name__, url_prefix="/logout")

@logout_bp.route("/", methods=['POST'])
@logout_bp.route("", methods=['POST'])
def logout():
	resp=make_response(jsonify(message="logging out"))
	resp.delete_cookie('token')
	resp.status_code=200
	resp.headers.add("Content-Type","aplication/json")
	return resp
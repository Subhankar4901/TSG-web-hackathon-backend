from flask import Blueprint, request, make_response, jsonify
from ....models import OTP, User
from datetime import datetime
from .... import db
from ....utils.jwt import JWT

verifyotp_bp = Blueprint('verifyotp', __name__, url_prefix="/verifyotp")

@verifyotp_bp.route("/", methods=["POST"])
@verifyotp_bp.route("", methods=["POST"])
def verifyotp():
	data = request.get_json()
	user_email = data.get("email")
	user_otp = data.get("otp")
	if user_otp.isnumeric():
		user_otp = int(user_otp)
	else:
		resp=make_response(jsonify(message="otp invalid",email=None, password="OTP invalid"))
		resp.headers.add("Content-Type","aplication/json")
		resp.status_code=401
		return resp
	valid_time = 5 # in minutes
	saved_data = OTP.query.filter_by(email=user_email).first()

	if not saved_data:
		resp=make_response(jsonify(message="OTP not found" , email=None, password="OTP not available"))
		resp.headers.add("Content-Type","aplication/json")
		resp.status_code=200
		return resp
	
	timeDelta = datetime.now() - saved_data.time

	if (saved_data.otp == user_otp):
		if (timeDelta.total_seconds() > valid_time*60):
			resp=make_response(jsonify(message="otp expired",email=None, password="OTP expired"))
			resp.headers.add("Content-Type","aplication/json")
			resp.status_code=401
		else:
			user = User.query.filter_by(email=user_email).first()
			if user and (int(user.type) == 4):
				resp=make_response(jsonify(message="user authenticated",email=None, password=None, token=JWT.tokenizer({"id":user.id,"type":user.type}), user_type=user.type))
				resp.headers.add("Content-Type","aplication/json")
				resp.status_code=200
			else:
				resp=make_response(jsonify(message="user not found", email="Wrong Email", password=None))
				resp.headers.add("Content-Type","aplication/json")
				resp.status_code=401

		db.session.delete(saved_data)
		db.session.commit()
	else:
		resp=make_response(jsonify(message="OTP mismatch", email=None, password="Wrong OTP"))
		resp.headers.add("Content-Type","aplication/json")
		resp.status_code=401

	return resp
	


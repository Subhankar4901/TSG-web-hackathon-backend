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
	user_email = data["email"]
	user_otp = int(data["otp"])
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
			resp=make_response(jsonify(message="otp expired"))
			resp.headers.add("Content-Type","aplication/json")
			resp.status_code=401
		else:
			user_obj = User.query.filter_by(email=user_email).first()
			if user_obj and (int(user_obj.type) == 4):
				token=JWT.tokenizer({"id":user_obj.id,"type":user_obj.type})
				resp=make_response(jsonify(message="user authenticated",user_type=user_obj.type))
				resp.set_cookie('token', token, httponly = True)
				resp.status_code=200
				resp.headers.add("Content-Type","aplication/json")
				return resp
			else:
				resp=make_response(jsonify(message="generate a otp first"))
				resp.headers.add("Content-Type","aplication/json")
				resp.status_code=401

		db.session.delete(saved_data)
		db.session.commit()
	else:
		resp=make_response(jsonify(message="OTP invalid"))
		resp.headers.add("Content-Type","aplication/json")
		resp.status_code=401

	return resp
	


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
	user_otp = data["otp"]
	valid_time = 5 # in minutes
	saved_data = OTP.query.filter_by(email=user_email).first()

	if not saved_data:
		resp=make_response(jsonify({"message":"invalid access"}))
		resp.headers.add("Content-Type","aplication/json")
		resp.status_code=401
		return resp
	
	timeDelta = datetime.now() - datetime.fromtimestamp(saved_data.unixTimeStamp)
	resp = make_response()

	if (saved_data.otp == user_otp):
		if (timeDelta.total_seconds() > valid_time*60):
			resp=make_response(jsonify({"message":"otp expired"}))
			resp.headers.add("Content-Type","aplication/json")
			resp.status_code=401
		else:
			user = User.query.filter_by(email=user_email).first()
			resp=make_response(jsonify(message="user authenticated", token=JWT.tokenizer({"user_id":user.id,"type":user.type})))
			resp.headers.add("Content-Type","aplication/json")
			resp.status_code=200

		db.session.delete(saved_data)
		db.session.commit()
	else:
		resp=make_response(jsonify({"message":"otp invalid"}))
		resp.headers.add("Content-Type","aplication/json")
		resp.status_code=401

	return resp
	


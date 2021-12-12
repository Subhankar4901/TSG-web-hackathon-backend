from flask import Blueprint, request, make_response, jsonify
from ....models import OTP
import datetime

verifyotp_bp = Blueprint('verifyotp', __name__, url_prefix="/verifyotp")

@verifyotp_bp.route("/", methods=["POST"])
@verifyotp_bp.route("", methods=["POST"])
def verifyotp():
	data = request.get_json()
	user_email = data["email"]
	user_otp = data["otp"]
	valid_time = 5 # in minutes
	saved_data = OTP.query.filter(OTP.email == user_email).first()
	if not saved_data:
		resp=make_response(jsonify({"message":"invalid access"}))
		resp.headers.add("Content-Type","aplication/json")
		resp.status_code=401
		return resp
	
	timeDelta = datetime.datetime.now() - datetime.datetime.fromtimestamp(saved_data.unixTimeStamp)
	
	if (saved_data.otp == user_otp):
		if (timeDelta.total_seconds() == valid_time*60):
			resp=make_response(jsonify({"message":"otp expired"}))
			resp.headers.add("Content-Type","aplication/json")
			resp.status_code=401
			return resp
		else:
			resp=make_response(jsonify({"message":"user verified"}))
			resp.headers.add("Content-Type","aplication/json")
			resp.status_code=200
			return resp

	else:
		resp=make_response(jsonify({"message":"otp invalid"}))
		resp.headers.add("Content-Type","aplication/json")
		resp.status_code=401
		return resp

	


from flask import Blueprint, request, make_response, jsonify
from ....models import User
from ....utils.jwt import JWT
import csv
# input
# {
#     "username": "tsg_official",
#     "password": "123#abc%$pq"
# }
# output
# 
# {
#     "response": 1,
#     "token": "eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjoyLCJ0eXBlIjpudWxsLCJ1c2VybmFtZSI6InRzZ19vZmZpY2lhbCJ9.2iA22zSCbGngzr7fpBfPjE2e0Kng2xHD7CxA88ejy340ol5z3HyUSGJ8Nlsq5pLJ6mOhhHkpNSOB87blIiyxdg"
# }

auth_bp = Blueprint('auth', __name__, url_prefix="/auth")

@auth_bp.route("/", methods=["POST"])
@auth_bp.route("", methods=["POST"])
def auth():
	data = request.get_json()
	user = data["username"]
	password=data["password"]
	user_obj=User.query.filter_by(username=user).first()
	if user_obj:
		if password == user_obj.password:
			resp=make_response(jsonify(message="user authenticated",token=JWT.tokenizer({"user_id":user_obj.id,"type":user_obj.type, "username": user})))
			resp.status_code=200
			resp.headers.add("Content-Type","aplication/json")
			return resp
		else:
			resp=make_response(jsonify(message="password invalid"))
			resp.status_code=401
			resp.headers.add("Content-Type","aplication/json")
			return resp
	else:
		resp=make_response(jsonify(message="username invalid"))
		resp.status_code=401
		resp.headers.add("Content-Type","aplication/json")
		return resp
		

	
	
	


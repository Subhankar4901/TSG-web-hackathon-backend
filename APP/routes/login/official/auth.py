from flask import Blueprint, request, make_response, jsonify
from ....models import User
from ....utils.jwt import JWT
from .... import db
from decouple import config

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
	user = data.get("username")
	password=data.get("password")
	
	# adding admin in database
	if not User.query.filter_by(username=config("admin_username")).first():
		db.session.add(User(username=config("admin_username"), password=config("admin_password"), type=1, email=config("admin_email"),name='admin'))
		db.session.commit()

	user_obj=User.query.filter_by(username=user).first()
	if user_obj:
		if password == user_obj.password:
			token=JWT.tokenizer({"id":user_obj.id,"type":user_obj.type, "username": user})
			resp=make_response(jsonify(message="user authenticated",user_type=user_obj.type))
			resp.set_cookie('token', token, httponly = True);
			resp.status_code=200
			resp.headers.add("Content-Type","aplication/json")
			return resp
		else:
			resp=make_response(jsonify(message="wrong password"))
			resp.status_code=401
			resp.headers.add("Content-Type","aplication/json")
			return resp
	else:
		resp=make_response(jsonify(message="username invalid"))
		resp.status_code=401
		resp.headers.add("Content-Type","aplication/json")
		return resp
		

	
	
	


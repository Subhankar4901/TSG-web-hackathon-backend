from flask import Blueprint, request, make_response, jsonify
import csv
# input
# {
#     "username": "tsg_official",
#     "password": "123#abc%$pq"
# }
# output
# 
# 

auth_bp = Blueprint('auth', __name__, url_prefix="/auth")

@auth_bp.route("/", methods=["POST"])
@auth_bp.route("", methods=["POST"])
def auth():
	data = request.get_json()
	user = data["username"]
	password=data["password"]

	reader = csv.reader(open("docs/official.csv", 'r'))
	for row in reader:
		if row[0] == user and row[1] == password:
			return "User found " + row[3]
		elif row[0] == user:
			return "Password incorrect"
	return "NA"
		

	
	
	


from flask import Blueprint, json, request, make_response, jsonify
from ...models import Complain
from ...utils.jwt import JWT
from ...models import Complain, User

getcomplaints_bp = Blueprint('getcomplaints', __name__, url_prefix="/getcomplaints")

@getcomplaints_bp.route("/", methods=["GET"])
def getcomplaints():
	token=request.cookies.get("token")
	token_dict=JWT.validator(token)
	if token_dict:
		complains = []
		userType = int(token_dict['type'])
		userId = token_dict['id']
		if userType <= 2:
			complains.extend(list(map(lambda c: c.extractData(), Complain.query.all())))
		else:
			user = User.query.get(userId)
			complains.extend(list(map(lambda c: c.extractData(), user.complaints)))
		resp=make_response(jsonify(message="Success", complaints = complains))
		resp.status_code=200
		return resp
	else:
		resp=make_response(jsonify(message="Unauthorised"))
		resp.status_code=401
		return resp

	
	
	


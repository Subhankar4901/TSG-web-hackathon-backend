from flask import Blueprint,request,jsonify,make_response
from ...models.Event import Event
from ... import db
from ...utils.jwt import JWT
import datetime

update_event_bp=Blueprint("update_event",__name__,url_prefix="/update")
@update_event_bp.route("/",methods=["POST"])
@update_event_bp.route("",methods=["POST"])
def update_event():
	token=request.cookies.get("token")
	token_dict=JWT.validator(token)
	if token_dict:
		data=request.get_json()
		event=Event.query.get(int(data["id"]))
		if event.organizer_id==token_dict["id"] or token_dict["type"]<=2:
			if data["key"]=="start" or data["key"]=="end":
				setattr(event,data["key"],datetime.datetime.fromisoformat(data["value"]))
			elif data["key"]=="poster":
				poster=request.files.get("poster")
				setattr(event,data["key"],poster.read())
			else:
				setattr(event,data["key"],data["value"])
			db.session.commit()
			return make_response(jsonify(messge=f"{data['key']} Updated."),200)
		else:
			return make_response(jsonify(messege="Unathorized"),401)
	else:
		return make_response(jsonify(messege="Unathorized"),401) 		
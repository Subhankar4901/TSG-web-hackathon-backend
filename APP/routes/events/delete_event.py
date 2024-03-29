from flask import Blueprint,request,jsonify,make_response
from ...models import Event
from ... import db
from ...utils.jwt import JWT

delete_event_bp=Blueprint("delete_event",__name__,url_prefix="/")
@delete_event_bp.route("<event_id>/delete",methods=["POST"])
@delete_event_bp.route("<event_id>/delete/",methods=["POST"])
def delete_event(event_id):
	token = request.cookies.get("token")
	token_dict = JWT.validator(token)
	if token_dict and event_id:
		event_obj = Event.query.get(event_id)
		if event_obj and ((token_dict["type"] < 3) or ((token_dict["type"]==3) and (event_obj.organiser.id==token_dict["id"]))):
			db.session.delete(event_obj)
			db.session.commit()
			return make_response(jsonify(message="event deleted")) 
	return make_response(jsonify(message="Invalid request"), 401) 
from flask import Blueprint,request,jsonify,make_response
from ...models.Event import Event
from ...models.User import User
from ... import db
from ...utils.jwt import JWT
import datetime
from .add_event import add_event
from .delete_event import delete_event

update_event_bp=Blueprint("update_event",__name__,url_prefix="/update")
@update_event_bp.route("/",methods=["POST"])
@update_event_bp.route("",methods=["POST"])
def update_event():
	resp = delete_event()
	if (resp.status == 401):
		return resp
	add_event()
	return make_response(jsonify(message="event updated"))
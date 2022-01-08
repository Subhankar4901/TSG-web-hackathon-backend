from flask import Blueprint,request,jsonify,make_response
from ...models.Event import Event
from ...models.User import User
from ... import db
from ...utils import JWT, access_required
import datetime
from dateutil import parser

add_event_bp=Blueprint("add_event",__name__,url_prefix="/add")
@add_event_bp.route("/",methods=["POST"])
@add_event_bp.route("",methods=["POST"])
@access_required(3)
def add_event():
    data=request.form
    poster=request.files.get("poster")
    token=request.cookies.get("token")
    token_dict=JWT.validator(token)
    if token_dict:
        organiser=User.query.filter_by(id=token_dict.get("id")).first()
        event=Event(
            title=data.get("title"),
            introduction=data.get("introduction"),
            procedure=data.get("procedure"),
            jugde_criteria=data.get("jugde_criteria"),
            timeline=data.get("timeline"),
            venue=data.get("venue"),
            start=parser.parse(data.get("start")),
            end=parser.parse(data.get("end")),
            organiser=organiser,
            event_tags=data.get("tags"),
            type=data.get("type"),
            poster=poster.read()
        )
        db.session.add(event)
        db.session.commit()
        return make_response(jsonify(message="Event added"))
    else:
        resp=make_response(jsonify(message="Unauthorised"))
        resp.status_code=401
        return resp
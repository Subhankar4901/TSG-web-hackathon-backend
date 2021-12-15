from flask import Blueprint,request,jsonify,make_response
from ...models.Event import Event
from ...models.User import User
from ... import db
from ...utils.jwt import JWT
from datetime import datetime

add_event_bp=Blueprint("add_event",__name__,url_prefix="/add_event")
@add_event_bp.route("/",methods=["POST"])
def add_event():
    data=request.get_json()
    token=data.get("token")
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
            start=datetime.fromisoformat(data.get("start")) if data.get("start") else None,
            end=datetime.fromisoformat(data.get("end")) if data.get("end") else None,
            organiser=organiser,
            event_tags=data.get("tags"),
            type=data.get("type"),
            report=bytes(data.get("report"),"utf8"),
            poster=bytes(data.get("poster"),"utf8"),
            participation_certificate=bytes(data.get("participation_certificate"),"utf8")
        )
        db.session.add(event)
        db.session.commit()
        return make_response(jsonify(message="Event added"))
    else:
        resp=make_response(jsonify(message="Unauthorised"))
        resp.status_code=401
        return resp
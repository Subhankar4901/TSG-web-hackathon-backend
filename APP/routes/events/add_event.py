from flask import Blueprint,request,jsonify,make_response
from ...models.Event import Event
from ...models.User import User
from ... import db
from ...utils.jwt import JWT
import datetime

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
            start=datetime.datetime.fromisoformat(data.get("start")),
            end=datetime.datetime.fromisoformat(data.get("end")),
            organiser=organiser,
            event_tags=data.get("tags"),
            type=data.get("type"),
            poster= data.get("poster").encode("ascii") if data.get("poster") else data.get("poster"),
        )
        db.session.add(event)
        db.session.commit()
        return make_response(jsonify(message="Event added"))
    else:
        resp=make_response(jsonify(message="Unauthorised"))
        resp.status_code=401
        return resp
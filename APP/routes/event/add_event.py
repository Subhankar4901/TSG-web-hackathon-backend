from flask import Blueprint,request,jsonify,make_response
from ...models.Event import Event
from ...models.User import User
from ... import db
from ...utils.jwt import JWT
add_event_bp=Blueprint("add_event",__name__,url_prefix="/add_event")
@add_event_bp.route("/",methods=["GET","POST"])
def add_event():
    if request.method=="GET":
        return "hELLO"
    data=request.get_json()
    token=data["token"]
    token_dict=JWT.validator(token)
    if token_dict:
        organiser=User.query.filter_by(id=token_dict["user_id"]).first()
        event=Event(
            title=data["title"],
            introduction=data["introduction"],
            procedure=data["procedure"],
            jugde_criteria=data["jugde_criteria"],
            timeline=data["timeline"],
            venue=data["venue"],
            start=data["start"],
            end=data["end"],
            organiser=organiser,
            event_tags=data["tags"],
            type=data["type"]
        )
        db.session.add(event)
        db.session.commit()
        return make_response(jsonify(messege="Event added"))
    else:
        resp=make_response(jsonify(message="Unauthorised"))
        resp.status_code=401
        return resp
from flask import Blueprint,request,jsonify,make_response
from ...models.Achievement import Achievement
from ...models.User import User
from ...models.Event import Event
from ...utils.jwt import JWT
from ... import db
add_achievement_bp=Blueprint("add_achievement",__name__,url_prefix="/add")
@add_achievement_bp.route("/",methods=["POST"])
def addAchievement():
    data=request.get_json()
    token=data["token"]
    token_dict=JWT.validator(token)
    if token_dict:
        user=User.query.filter_by(roll=data["roll"]).first()
        event=Event.query.filter_by(id=data["event_id"]).first()
        if token_dict["type"]<3:
            achievement=Achievement(achiever=user,event=event,position=data["position"],certificate=b"certi-1")
            db.session.add(achievement)
            db.session.commit()
            resp=make_response(jsonify(message="Achievement added"))
            return resp
        elif token_dict["type"]==3 and event.organiser.id==data["event_id"]:
            achievement=Achievement(achiever=user,event=event,position=data["position"],certificate="certi-1")
            db.session.add(achievement)
            db.session.commit()
            resp=make_response(jsonify(message="Achievement added"))
            return resp
        else:
            resp=make_response(jsonify(message="Unauthorised"))
            resp.status_code=401
            return resp
    else:
        resp=make_response(jsonify(message="Unauthorised"))
        resp.status_code=401
        return resp
            
            
            
from flask import Blueprint,request,jsonify,make_response
from ...models.Achievement import Achievement
from ...models.User import User
from ...models.Event import Event
from ...utils import JWT, sendEmail
from ... import db

add_achievement_bp = Blueprint("add_achievement",__name__,url_prefix="/add")

# adds a achievement
# request contains jwt token, winner_email, event_id
# response contains a json message
@add_achievement_bp.route("/",methods=["POST"])
@add_achievement_bp.route("",methods=["POST"])
def addAchievement():
    data=request.form
    token=request.cookies.get("token")
    token_dict=JWT.validator(token)
    if token_dict:
        user=User.query.filter_by(email=data.get("winner_email")).first()
        event=Event.query.filter_by(id=data.get("event_id")).first()
        if (token_dict["type"] < 3) or ((token_dict["type"]==3) and event and (event.organiser.id==token_dict["id"])) and user:
            certificate = request.files.get("certificate")
            if certificate:
                certificate = certificate.read()
            achievement=Achievement(achiever=user,event=event,position=data.get("position"),certificate=certificate)
            db.session.add(achievement)
            db.session.commit()
            resp=make_response(jsonify(message="Achievement added"))
            sendEmail("Achievement added", f"Your achievement in {event.title} was added", [data.get("winner_email")])
            return resp
        else:
            resp=make_response(jsonify(message="Invalid request"))
            resp.status_code=401
            return resp
    else:
        resp=make_response(jsonify(message="Unauthorised"))
        resp.status_code=401
        return resp
            
            
            
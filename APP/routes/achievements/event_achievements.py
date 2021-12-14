from flask import Blueprint,jsonify,make_response,request
from ...models.Event import Event
from ...models.User import User
from ...utils.jwt import JWT
event_bp=Blueprint("event_achievements",__name__,url_prefix="/event")
@event_bp.route("/getAchievements")
def getAchievements():
    token=request.args.get("token")
    event_id=request.args.get("event_id")
    token_dict=JWT.validator(token)
    if token_dict:
        event:Event=Event.query.filter_by(id=event_id).first()
        if token_dict["type"]<3:
            achievements=[]
            for achievement in event.achievements:
                achievements.append({
                    "id":achievement.id,
                    "event_id":event_id,
                    "event_title":event.title,
                    "user_id":achievement.user,
                    "user_name":achievement.achiever.name,
                    "position": achievement.position
                })
            resp=make_response(jsonify(response=achievements))
            resp.status_code=200
            resp.content_type="application/json"
            return resp
        elif token_dict["type"]==3 and event.organizer.id==token_dict["user_id"]:
            achievements=[]
            for achievement in event.achievements:
                achievements.append({
                    "id":achievement.id,
                    "event_id":event_id,
                    "event_title":event.title,
                    "position": achievement.position
                })
            resp=make_response(jsonify(response=achievements))
            resp.status_code=200
            resp.content_type="application/json"
            return resp
        else:
            resp=make_response(jsonify(response="Unauthorised"))
            resp.status_code=401
            resp.content_type="application/json"
            return resp
            
from flask import Blueprint,request,make_response,jsonify
from ...utils.jwt import JWT
from ...models.User import User
student_bp=Blueprint("student_achievemens",__name__,url_prefix="/student")
@student_bp.route("/getAchievements")
def getAchievements():
    token=request.args.get("token")
    token_dict=JWT.validator(token)
    if token_dict:
        user=User.query.filter_by(id=token_dict["user_id"]).first()
        achivements=[]
        for achievement in user.achievements:
            achivements.append({
                "id":achievement.id,
                "event_id":achievement.event.id,
                "event_title":achievement.event.title,
                "position":achievement.position
            })
        resp=make_response(jsonify(response=achivements))
        resp.status_code=200
        resp.content_type="application/json"
        return resp
    else:
        resp=make_response(jsonify(response="Unauthorised"))
        resp.status_code=401
        resp.content_type="application/json"
        return resp    
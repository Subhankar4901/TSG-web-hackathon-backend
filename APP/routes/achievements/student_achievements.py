from flask import Blueprint,request,make_response,jsonify
from ...utils.jwt import JWT
from ...models.User import User
from decouple import config

# request has token query parameters
# response is achievements of student
student_bp=Blueprint("student_achievements",__name__,url_prefix="/student")
@student_bp.route("/getAchievements", methods=['GET'])
def getAchievements():
    token=request.cookies.get("token")
    token_dict=JWT.validator(token)
    if token_dict:
        user=User.query.filter_by(id=token_dict["id"]).first()
        achievements=[]
        for achievement in user.achievements:
            achievements.append({
                "id":achievement.id,
                "event_id":achievement.event.id,
                "event_title":achievement.event.title,
                "event_type":achievement.event.type,
                "event_tags":achievement.event.event_tags,
                "position":achievement.position,
                'start':achievement.event.start,
                'end':achievement.event.end,
                'certificate_uploaded':True if achievement.certificate else False,
                'certificate':f"{config('host')}/api/achievement/certificate/{achievement.id}"
            })
        resp=make_response(jsonify(achievements=achievements))
        resp.status_code=200
        resp.content_type="application/json"
        return resp
    else:
        resp=make_response(jsonify(message="Unauthorised access"))
        resp.status_code=401
        resp.content_type="application/json"
        return resp    
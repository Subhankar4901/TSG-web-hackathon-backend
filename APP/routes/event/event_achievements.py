from flask import Blueprint,jsonify,make_response,request
from ...models.Event import Event
from ...utils.jwt import JWT

achievements_bp=Blueprint("achievements",__name__,url_prefix="/")

# request contains event_id, no login required
# response is the list of achievements
@achievements_bp.route("<event_id>/getAchievements/")
@achievements_bp.route("<event_id>/getAchievements")
def getAchievements(event_id):
    event=Event.query.get(event_id)
    achievements=[]
    for achievement in event.achievements:
        achievements.append({
            "id":achievement.id,
            "user_name":achievement.achiever.name,
            "position": achievement.position
        })
    resp=make_response(jsonify(achievements=achievements,
            event_title=event.title,
            event_type=event.type,
            event_tags=event.event_tags.split(",")))
    resp.status_code=200
    resp.content_type="application/json"
    return resp
            
from flask import Blueprint,jsonify,make_response,request
from ...models.Event import Event
from ...utils.jwt import JWT

achievements_bp=Blueprint("achievements",__name__,url_prefix="/")

# request contains event_id, no login required
# but for viewing report a valid token should be given
# response is the list of achievements
@achievements_bp.route("<event_id>/getAchievements/")
@achievements_bp.route("<event_id>/getAchievements")
def getAchievements(event_id):
    token=request.args.get("token")
    event=Event.query.get(event_id)
    token_dict=JWT.validator(token)
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
            event_tags=event.event_tags.split(","),
            start=str(event.start),
            end=str(event.end),
            event_report=(event.report.decode('utf-8') if token_dict else None)
            ))
    resp.status_code=200
    resp.content_type="application/json"
    return resp
            
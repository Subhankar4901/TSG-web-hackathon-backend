from flask import Blueprint,jsonify,make_response,request
from ...models.Event import Event

achievements_bp=Blueprint("achievements",__name__,url_prefix="/")

# request contains event_id, no login required
# but for viewing report a valid token should be given
# response is the list of achievements
@achievements_bp.route("<event_id>/getAchievements/")
@achievements_bp.route("<event_id>/getAchievements")
def getAchievements(event_id):
    token=request.args.get("token")
    event=Event.query.get(event_id)
    achievements=[]
    for achievement in event.achievements:
        achievements.append({
            "id":achievement.id,
            "winner_name":achievement.achiever.name,
            "position": achievement.position
        })
    resp=make_response(jsonify(achievements=achievements))
    resp.status_code=200
    resp.content_type="application/json"
    return resp
            
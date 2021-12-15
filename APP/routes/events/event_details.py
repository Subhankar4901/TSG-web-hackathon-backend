from flask import Blueprint,jsonify,make_response,request
from ...models.Event import Event
from ...utils.jwt import JWT

info_bp=Blueprint("info",__name__,url_prefix="/")

# request contains event_id, no login required
# but for viewing report a valid token should be given
# response is the list of achievements
@info_bp.route("<event_id>/info/")
@info_bp.route("<event_id>/info")
def getAchievements(event_id):
    token = request.args.gettoken
    token_dict = JWT.validator(token)

    if token_dict:
        event = Event.query.get(event_id)
        resp = make_response(jsonify(
            title=event.title,
            introduction=event.introduction,
            procedure=event.procedure,
            jugde_criteria=event.jugde_criteria,
            timeline=event.timeline,
            venue=event.venue,
            start=str(event.start),
            end=str(event.end),
            organiser=event.organiser,
            event_tags=event.tags,
            type=event.type,
            report=event.report.decode('utf-8'),
            poster=event.poster.decode('utf-8')
        ))
    else:
        return make_response(jsonify(message="Unauthorized Access"), 401)
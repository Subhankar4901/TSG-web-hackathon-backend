from flask import Blueprint,jsonify,make_response,request
from ...models.Event import Event
from ...utils.jwt import JWT

info_bp=Blueprint("info",__name__,url_prefix="/")

# request contains event_id, no login required
# but for viewing report a valid token should be given
# response is the list of achievements
@info_bp.route("<event_id>/info/")
@info_bp.route("<event_id>/info")
def getInfo(event_id):
    event = Event.query.get(event_id)
    resp = make_response(jsonify(
        title=event.title,
        introduction=event.introduction,
        procedure=event.procedure,
        jugde_criteria=event.jugde_criteria,
        timeline=list(event.timeline.split(',')),
        venue=event.venue,
        start=event.start,
        end=event.end,
        organiser=event.organiser.name,
        event_tags=event.event_tags,
        type=event.type
    ))
    return resp
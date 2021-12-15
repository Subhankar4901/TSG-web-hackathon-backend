from datetime import datetime
from flask import Blueprint,jsonify
from ...models.Event import Event
upcoming_event_bp=Blueprint("upcoming_event",__name__,url_prefix="/upcoming")
@upcoming_event_bp.route("")
@upcoming_event_bp.route("/")
def upcoming_events():
    events=Event.query.filter(Event.start>datetime.now()).all()
    upcoming=[]
    for event in events:
        upcoming.append({
            "id":event.id,
            "title":event.title,
            "type":event.type,
            "organiser":event.organiser.name,
            "tag":event.event_tags,
            "start":str(event.start),
            "end":str(event.end)
        })
    return jsonify(events=upcoming)
    
from flask import Blueprint, jsonify
from ...models.Event import Event
from datetime import datetime

view_curr_events_bp = Blueprint("view_curr_events",__name__,url_prefix="/current")

@view_curr_events_bp.route('/')
@view_curr_events_bp.route("")
def events_basic_details():
    events = Event.query.filter(Event.end>datetime.now()).filter(Event.start<=datetime.now()).all()
    current = []
    for event in events:
        current.append(
            {
                'id':event.id,
                'title':event.title,
                "organiser":event.organiser.name,
                'type':event.type,
                "start":event.start,
                "end":event.end,
                'event_tags':event.event_tags
            }
        )
    
    return jsonify(events=current)

import re
from flask import Blueprint,request,jsonify,make_response
from ...models.Event import Event
import datetime
ended_events_bp=Blueprint("ended_events",__name__,url_prefix="/ended")

# query parameters
# t is time window for a event to be in results or in archives
# setting archive loads archive and avoiding it will load current results
@ended_events_bp.route("")
@ended_events_bp.route("/")
def ended_events():
    t=float(request.args.get("t")) # In days.
    archive = request.args.get("archive") != None
    today=datetime.date.today()
    today_datetime=datetime.datetime(today.year,today.month,today.day)
    datetime_before_t_days=today_datetime-datetime.timedelta(days=t)
    if not archive:
        required_events=Event.query.filter(Event.end>=datetime_before_t_days).filter(Event.end<today_datetime).all()
    else:
        required_events=Event.query.filter(Event.end<datetime_before_t_days).all()
    events=[]
    for event in required_events:
        events.append({
            "id":event.id,
            "title":event.title,
            "organiser":event.organiser.name,
            "type":event.type,
            "tag":event.event_tags,
            "start":event.start,
            "end":event.end,
        })
    resp=make_response(jsonify(events=events))
    resp.status_code=200
    return resp
    
    
    
from flask import Blueprint, jsonify
from ...models.Event import Event
from datetime import datetime

view_curr_events_bp = Blueprint("view_curr_events",__name__,url_prefix="/curr_events")

@view_curr_events_bp.route('/basic_details',methods=['GET'])
def events_basic_details():
    events = Event.query.all()
    current = []
    for event in events:
        start_str = event.start
        end_str = event.end
        start_date = datetime.strptime(start_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_str, '%Y-%m-%d')
        today = datetime.today()
        # filter events which are happening currently or will be happening in the future based on their end date
        if(end_date>=today or start_date>=today):
            event_dict={
                'id':event.id,
                'title':event.title,
                'introduction':event.introduction,
                # 'procedure':event.procedure,
                # 'jugde_criteria':event.judge_criteria,
                # 'timeline':event.timeline.split(','),
                'poster':event.poster.decode("utf-8"),
                'venue':event.venue,
                'start':event.start,
                'end':event.end,
                # 'report':event.report,
                # 'organizer_id':event.organizer_id,
                'type':event.type,
                'event_tags':event.event_tags
                # 'participation_certificate':event.participation_certificate
            }
            current.append(event_dict)
        return jsonify(current)

from flask import Blueprint
from .add_event import add_event_bp
from .event_achievements import achievements_bp
from .curr_events import view_curr_events_bp
from .ended_events import ended_events_bp
from .upcoming_events import upcoming_event_bp
from .event_details import info_bp
from .delete_event import delete_event_bp
from .update_event import update_event_bp
from .participated_events import participation_bp
from .update_user_events import update_user_events_bp
from .poster import poster_bp
from .report import report_bp

event_bp=Blueprint("event",__name__,url_prefix="/events")
event_bp.register_blueprint(add_event_bp)
event_bp.register_blueprint(update_event_bp)
event_bp.register_blueprint(delete_event_bp)
event_bp.register_blueprint(achievements_bp)
event_bp.register_blueprint(view_curr_events_bp)
event_bp.register_blueprint(ended_events_bp)
event_bp.register_blueprint(upcoming_event_bp)
event_bp.register_blueprint(info_bp)
event_bp.register_blueprint(participation_bp)
event_bp.register_blueprint(update_user_events_bp)
event_bp.register_blueprint(poster_bp)
event_bp.register_blueprint(report_bp)

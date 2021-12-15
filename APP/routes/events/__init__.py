from flask import Blueprint
from .add_event import add_event_bp
from .event_achievements import achievements_bp
from .curr_events import view_curr_events_bp

event_bp=Blueprint("event",__name__,url_prefix="/events")
event_bp.register_blueprint(add_event_bp)
event_bp.register_blueprint(achievements_bp)
event_bp.register_blueprint(view_curr_events_bp)
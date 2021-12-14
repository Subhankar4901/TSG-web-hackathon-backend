from flask import Blueprint
from .login import login_bp
from .updateusers import updateusers_bp
from .event.events import events_bp

base_bp = Blueprint('base', __name__, url_prefix="/")

base_bp.register_blueprint(login_bp)
base_bp.register_blueprint(updateusers_bp)
base_bp.register_blueprint(events_bp)

from flask import Blueprint
from .login import login_bp
from .updateusers import updateusers_bp
from .achievements import achievements_bp
from .events import event_bp
from .complaints import complaints_bp

base_bp = Blueprint('base', __name__, url_prefix="/")

base_bp.register_blueprint(login_bp)
base_bp.register_blueprint(updateusers_bp)
base_bp.register_blueprint(achievements_bp)
base_bp.register_blueprint(event_bp)
base_bp.register_blueprint(complaints_bp)

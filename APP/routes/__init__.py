from flask import Blueprint
from .login import login_bp
from .updateusers import updateusers_bp
from .achievements import achievements_bp
from .events import event_bp
from .complaints import complaints_bp
from .careers import career_bp
from .academics import academic_bp
from .news import news_bp

base_bp = Blueprint('base', __name__, url_prefix="/api")

base_bp.register_blueprint(login_bp)
base_bp.register_blueprint(updateusers_bp)
base_bp.register_blueprint(achievements_bp)
base_bp.register_blueprint(event_bp)
base_bp.register_blueprint(complaints_bp)
base_bp.register_blueprint(career_bp)
base_bp.register_blueprint(academic_bp)
base_bp.register_blueprint(news_bp)

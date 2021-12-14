from flask import Blueprint
from .student_achievements import student_bp
from .event_achievements import event_bp
from .add_achievement import add_achievement_bp
achievements_bp=Blueprint("achievement",__name__,url_prefix="/achievement")
achievements_bp.register_blueprint(student_bp)
achievements_bp.register_blueprint(event_bp)
achievements_bp.register_blueprint(add_achievement_bp)
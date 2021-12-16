from flask import Blueprint

from APP.routes.achievements.update_achievement import update_achievement
from .student_achievements import student_bp
from .add_achievement import add_achievement_bp
from .update_achievement import update_achievement_bp
from .delete_achievement import delete_achievement_bp

achievements_bp=Blueprint("achievement",__name__,url_prefix="/achievement")
achievements_bp.register_blueprint(student_bp)
achievements_bp.register_blueprint(add_achievement_bp)
achievements_bp.register_blueprint(delete_achievement_bp)
achievements_bp.register_blueprint(update_achievement_bp)
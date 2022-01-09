from flask import Blueprint
from .add_career import add_career_bp
from .report import report_bp
from .get_careers import get_careers_bp

career_bp=Blueprint("career",__name__,url_prefix="/careers")
career_bp.register_blueprint(add_career_bp)
career_bp.register_blueprint(report_bp)
career_bp.register_blueprint(get_careers_bp)

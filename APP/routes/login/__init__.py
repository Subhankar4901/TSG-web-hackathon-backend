from flask import Blueprint
from .student import student_bp
from .official import official_bp

login_bp = Blueprint('login', __name__, url_prefix="/login")

login_bp.register_blueprint(student_bp)
login_bp.register_blueprint(official_bp)

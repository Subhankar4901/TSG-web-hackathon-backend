from flask import Blueprint
from .sendotp import sendotp_bp
from .verifyotp import verifyotp_bp

student_bp = Blueprint('student', __name__, url_prefix="/student")

student_bp.register_blueprint(sendotp_bp)
student_bp.register_blueprint(verifyotp_bp)

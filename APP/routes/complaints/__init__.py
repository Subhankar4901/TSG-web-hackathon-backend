from flask import Blueprint
from .getcomplaints import getcomplaints_bp

complaints_bp = Blueprint('complaints', __name__, url_prefix="/complaints")

complaints_bp.register_blueprint(getcomplaints_bp)


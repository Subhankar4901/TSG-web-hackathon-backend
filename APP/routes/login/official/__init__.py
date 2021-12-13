from flask import Blueprint
from .auth import auth_bp
official_bp = Blueprint('official', __name__, url_prefix="/official")

official_bp.register_blueprint(auth_bp)

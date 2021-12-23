from flask import Blueprint
from .fetchWithToken import fetch_bp
user_bp = Blueprint('user', __name__, url_prefix="/user")

user_bp.register_blueprint(fetch_bp)

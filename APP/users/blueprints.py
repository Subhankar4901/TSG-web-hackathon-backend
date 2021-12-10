from flask import Blueprint
from .routes.test import test_bp
from .routes.login import login_bp

users_bp = Blueprint('users', __name__, url_prefix="/users")

users_bp.register_blueprint(test_bp)
users_bp.register_blueprint(login_bp)

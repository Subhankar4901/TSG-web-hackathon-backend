from flask import Blueprint
from .test.test import test_bp
from .login import login_bp
from .updateusers import updateusers_bp

base_bp = Blueprint('base', __name__, url_prefix="/")

base_bp.register_blueprint(test_bp)
base_bp.register_blueprint(login_bp)
base_bp.register_blueprint(updateusers_bp)

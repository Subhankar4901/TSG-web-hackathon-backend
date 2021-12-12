from flask import Blueprint
from .test.test import test_bp

base_bp = Blueprint('base', __name__, url_prefix="/")

base_bp.register_blueprint(test_bp)

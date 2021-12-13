from flask import Blueprint
from .test.test import test_bp
from .home import base_bp
from .login import login_bp
from .updateusers import updateusers_bp

base_bp.register_blueprint(test_bp)
base_bp.register_blueprint(login_bp)
base_bp.register_blueprint(updateusers_bp)

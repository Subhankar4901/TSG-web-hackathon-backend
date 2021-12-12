from flask import Blueprint
from ...utils.sendEmail import sendEmail
test_bp = Blueprint('test', __name__, url_prefix="/test")

@test_bp.route('/')
def test():
    return "hello"

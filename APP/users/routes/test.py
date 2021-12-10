from flask import Blueprint

test_bp = Blueprint('test', __name__, url_prefix="/test")

@test_bp.route('/')
def test():
    return "Hello"

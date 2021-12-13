from flask import Blueprint
from ..models.User import User
base_bp = Blueprint('base', __name__, url_prefix="/")

@base_bp.route('/')
def home():
    return "home route"

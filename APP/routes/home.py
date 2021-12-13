from flask import Blueprint
from ..models.User import User
from ..models.Event import Event
base_bp = Blueprint('base', __name__, url_prefix="/")

@base_bp.route('/')
def home():
    print(Event.query.limit(1).all()[0])
    return "home route"

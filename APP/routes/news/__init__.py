from flask import Blueprint
from .sendNews import mailNews_bp

news_bp = Blueprint('news', __name__, url_prefix="/news")

news_bp.register_blueprint(mailNews_bp)
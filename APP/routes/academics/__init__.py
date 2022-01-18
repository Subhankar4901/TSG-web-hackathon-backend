from flask import Blueprint
from .add_academic import add_academic_bp
from .get_academic import get_academics_bp
from .delete_academic import delete_academic_bp
from .attachment import attachment_bp

academic_bp=Blueprint("academic",__name__,url_prefix="/academic")
academic_bp.register_blueprint(add_academic_bp)
academic_bp.register_blueprint(get_academics_bp)
academic_bp.register_blueprint(delete_academic_bp)
academic_bp.register_blueprint(attachment_bp)
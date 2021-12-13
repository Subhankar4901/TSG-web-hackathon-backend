from .officials import officials_bp
from .students import students_bp
from flask import Blueprint

updateusers_bp=Blueprint('updateusers',__name__,url_prefix="/updateusers")
updateusers_bp.register_blueprint(officials_bp)
updateusers_bp.register_blueprint(students_bp)
from flask import Blueprint
from .getcomplaints import getcomplaints_bp
from .give_remark import remark_bp
from .addcomplaints import addcomplaint_bp
from .getattachment import getattachment_bp

complaints_bp = Blueprint('complaints', __name__, url_prefix="/complaints")

complaints_bp.register_blueprint(getcomplaints_bp)
complaints_bp.register_blueprint(remark_bp)
complaints_bp.register_blueprint(addcomplaint_bp)
complaints_bp.register_blueprint(getattachment_bp)


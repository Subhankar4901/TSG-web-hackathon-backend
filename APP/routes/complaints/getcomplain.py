from flask import Blueprint, json, request, make_response, jsonify
from ...models import Complain
from ...utils import access_required

getcomplaint_bp = Blueprint('getcomplaint', __name__, url_prefix="/getcomplaint")

@getcomplaint_bp.route("<complaint_id>/", methods=["GET"])
@getcomplaint_bp.route("<complaint_id>", methods=["GET"])
@access_required(4)
def getcomplaint(complaint_id):
	return make_response(jsonify(complain=Complain.query.get(complaint_id).extractData()))
from flask import Blueprint, json, request, make_response, jsonify
from ...models import Complain
from ...utils.jwt import JWT
from ...utils import access_required, sendEmail
from ... import db
addcomplaint_bp = Blueprint('addcomplaint', __name__, url_prefix="/addcomplaint")

@addcomplaint_bp.route("/", methods=["POST"])
@addcomplaint_bp.route("", methods=["POST"])
def addcomplaint():
    data = request.form
    token = request.cookies.get("token")
    token_dict=JWT.validator(token)
    if not token_dict:
        return make_response(jsonify(message="Unauthorised"), 401)
    readPdf = request.files.get("attachment")
    if readPdf:
        readPdf = readPdf.read()
    complain = Complain(
        userid = token_dict.get("id"),
        description = data.get("description"),
        subject=data.get("subject"),
        remarks = "In Review",
        attachment = readPdf
    )
    # return "ok", 200
    db.session.add(complain)
    db.session.commit()		
    resp=make_response(jsonify(message="Success, complaint added"))
    resp.status_code=200
    sendEmail("New Complaint", f"A new complaint was added", [], officials=True)
    return resp

    
    
    


from flask import Blueprint, request, make_response, jsonify
from ...models import Complain
from ...utils.jwt import JWT
from ...utils import access_required
from ... import db
addcomplaint_bp = Blueprint('addcomplaint', __name__, url_prefix="/addcomplaint")

@addcomplaint_bp.route("/", methods=["POST"])
@addcomplaint_bp.route("", methods=["POST"])
@access_required(4)
def addcomplaint():
    data = request.form
    token = data.get("token")
    token_dict=JWT.validator(token)
    mypdf = request.files.get("file")
    readPdf = mypdf.read()
    complain = Complain(
        userid = token_dict.get("id"),
        description = data.get("description"),
        remarks = "In Review",
        attachment = readPdf
    )
    # return "ok", 200
    db.session.add(complain)
    db.session.commit()		
    resp=make_response(jsonify(message="Success, complaint added"))
    resp.status_code=200
    return resp

    
    
    


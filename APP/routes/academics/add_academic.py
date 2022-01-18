from flask import Blueprint,request,jsonify,make_response
from ...models.Academic import Academic
from ... import db
from ...utils import JWT, access_required

add_academic_bp=Blueprint("add_academic",__name__,url_prefix="/add")
@add_academic_bp.route("/",methods=["POST"])
@add_academic_bp.route("",methods=["POST"])
@access_required(2)
def add_academic():
    data=request.form
    attachment=request.files.get("attachment")
    if(attachment != None):
        attachment = attachment.read()
    token=request.cookies.get("token")
    token_dict=JWT.validator(token)
    downloadLink = data.get("downloadLink")
    if downloadLink == None:
        downloadLink = ""
    print(token_dict)
    if token_dict:
        print(data)
        academic=Academic(
            title=data.get("title"),
            subjectcode=data.get("subjectcode"),
            department=data.get("department"),
            semester = data.get("semester"),
            type=data.get("type"),
            uploadedby=token_dict.get("username"),
            downloadLink=downloadLink,
            attachment=attachment,
        )
        db.session.add(academic)
        db.session.commit()
        return make_response(jsonify(message="Academics Added"))
    else:
        resp=make_response(jsonify(message="Unauthorised"))
        resp.status_code=401
        return resp
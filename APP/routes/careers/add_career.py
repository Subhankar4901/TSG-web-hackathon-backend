import re
from flask import Blueprint,request,jsonify,make_response
from ...models.Career import Career
from ... import db
from ...utils import JWT, access_required
import datetime

add_career_bp=Blueprint("add_career",__name__,url_prefix="/add")
@add_career_bp.route("/",methods=["POST"])
@add_career_bp.route("",methods=["POST"])
@access_required(2)
def add_career():
    data=request.form
    report=request.files.get("attachment")
    if(report != None):
        report = report.read()
    token=request.cookies.get("token")
    token_dict=JWT.validator(token)
    print(token_dict)
    if token_dict:
        print(data)
        career=Career(
            title=data.get("title"),
            location=data.get("location"),
            # date=datetime.datetime.fromisoformat(data.get("date")),
            report=report,
            jobprofile=data.get("jobprofile"),
            type=data.get("type"),
            uploadedby=token_dict.get("username")
        )
        db.session.add(career)
        db.session.commit()
        return make_response(jsonify(message="Career Added"))
    else:
        resp=make_response(jsonify(message="Unauthorised"))
        resp.status_code=401
        return resp
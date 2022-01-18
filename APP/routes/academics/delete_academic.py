from flask import Blueprint,request,jsonify,make_response
from ...models.Academic import Academic
from ... import db
from ...utils import JWT, access_required
from sqlalchemy.orm import defer


delete_academic_bp=Blueprint("delete_academic",__name__,url_prefix="/delete")
@delete_academic_bp.route("/",methods=["POST"])
@delete_academic_bp.route("",methods=["POST"])
@access_required(2)
def delete_academic():
    data=request.json
    academicid = int(data.get('academicid'))
    token=request.cookies.get("token")
    token_dict=JWT.validator(token)
    print(token_dict)
    if token_dict:
        print(data)
        Academic.query.filter_by(id=academicid).delete()
        academics = Academic.query.options(defer('attachment')).all()
        current = []
        for academic in academics:
            current.append(
                {
                    'id':academic.id,
                    'title':academic.title,
                    'subjectcode':academic.subjectcode,
                    'date':academic.date,
                    'department':academic.department,
                    'semester':academic.semester,
                    'type':academic.type,
                    "uploadedby": academic.uploadedby,
                    'downloadcount':academic.downloadcount,
                    'downloadLink':academic.downloadLink,
                    "attachment_url":f"api/academics/attachment/{academic.id}"  if academic.attachment else None,
                }
            )
        db.session.commit()
        return jsonify(academics=current), 200
    else:
        resp=make_response(jsonify(message="Unauthorised"))
        resp.status_code=401
        return resp
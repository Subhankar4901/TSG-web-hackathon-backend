from flask import Blueprint,request,jsonify,make_response
from ...models.Career import Career
from ... import db
from ...utils import JWT, access_required
from sqlalchemy.orm import defer


delete_career_bp=Blueprint("delete_career",__name__,url_prefix="/delete")
@delete_career_bp.route("/",methods=["POST"])
@delete_career_bp.route("",methods=["POST"])
@access_required(2)
def delete_career():
    data=request.json
    careerid = int(data.get('careerid'))
    token=request.cookies.get("token")
    token_dict=JWT.validator(token)
    print(token_dict)
    if token_dict:
        print(data)
        Career.query.filter_by(id=careerid).delete()
        careers = Career.query.options(defer('report')).all()
        current = []
        for career in careers:
            current.append(
                {
                    'id':career.id,
                    'title':career.title,
                    "location":career.location,
                    'type':career.type,
                    "date":career.date,
                    "jobprofile":career.jobprofile,
                    "uploadedby": career.uploadedby,
                    "report_url":f"api/careers/report/{career.id}"  if career.report else None,
                }
            )
        db.session.commit()
        return jsonify(careers=current),200
    #     db.session.add(career)
    #     db.session.commit()
    #     return make_response(jsonify(message="Career Added"))
    else:
        resp=make_response(jsonify(message="Unauthorised"))
        resp.status_code=401
        return resp
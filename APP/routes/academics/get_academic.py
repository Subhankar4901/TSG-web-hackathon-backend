from flask import Blueprint, jsonify

from sqlalchemy.orm import defer
from ...models.Academic import Academic
from ...utils import access_required

get_academics_bp = Blueprint("get_academics",__name__,url_prefix="/get_academics")

@get_academics_bp.route('/')
@get_academics_bp.route("")
@access_required(4)
def get_academics():
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
    
    return jsonify(academics=current)

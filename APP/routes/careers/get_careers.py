from os import access
from flask import Blueprint, jsonify

from ...models.Career import Career
from decouple import config
from ...utils import access_required

get_careers_bp = Blueprint("get_careers",__name__,url_prefix="/get_careers")

@get_careers_bp.route('/')
@get_careers_bp.route("")
@access_required(2)
def get_careers():
    careers = Career.query.all()
    current = []
    for career in careers:
        current.append(
            {
                'id':career.id,
                'title':career.title,
                "location":career.location,
                'type':career.type,
                "date":career.date,
                "report_url":f"http://{config('host')}/api/events/report/{career.id}"  if career.report else None,
            }
        )
    
    return jsonify(careers=current)

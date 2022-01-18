from flask import Blueprint,send_file,request,jsonify,make_response
from ...models.Academic import Academic
from ... import db
from ...utils.jwt import JWT
from io import BytesIO

attachment_bp=Blueprint("attachment",__name__,url_prefix="/attachment")
@attachment_bp.route("/<id>")
def get_attachment(id):
    '''
    Method to get attachment directly from backend.
    '''
    token=request.cookies.get("token")
    if JWT.validator(token):
        academic=Academic.query.filter_by(id=int(id)).first()
        attachment=academic.attachment
        if(len(attachment) == 0):
            return "No file uploaded",200
        academic.downloadcount += 1
        db.session.commit()
        return send_file(BytesIO(attachment), mimetype="application/pdf")
    else:
        resp=make_response(jsonify(message="Unauthorised"))
        resp.status=401
        return resp
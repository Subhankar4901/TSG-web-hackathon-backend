from flask import Blueprint,send_file,request,jsonify,make_response
from ...models import Achievement
from ...utils import JWT
from io import BytesIO

certificate_bp=Blueprint("certificate",__name__,url_prefix="/certificate")
@certificate_bp.route("/<id>")
def get_certificate(id):
    '''
    Method to get certificate directly from backend.
    '''
    token=request.cookies.get("token")
    if JWT.validator(token):
        achievement=Achievement.query.get(id)
        title=achievement.event.title
        name=f"{title}_certificate.pdf" if title else f"certificate_{id}.pdf"
        certificate=achievement.certificate
        return send_file(BytesIO(certificate),download_name=name,as_attachment=True)
    else:
        resp=make_response(jsonify(message="Unauthorised"))
        resp.status=401
        return resp
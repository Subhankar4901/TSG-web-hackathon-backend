from flask import Blueprint,send_file,request,jsonify,make_response
from ...models.Career import Career
from ...utils.jwt import JWT
from io import BytesIO

report_bp=Blueprint("report",__name__,url_prefix="/report")
@report_bp.route("/<id>")
def get_report(id):
    '''
    Method to get report directly from backend.
    '''
    token=request.cookies.get("token")
    if JWT.validator(token):
        career=Career.query.filter_by(id=int(id)).first()
        title=career.title
        name=f"{title}_report.pdf" if title else f"report_{id}.pdf"
        report=career.report
        if(len(report) == 0):
            return "No file uploaded",200
        return send_file(BytesIO(report),download_name=name,as_attachment=True)
    else:
        resp=make_response(jsonify(message="Unauthorised"))
        resp.status=401
        return resp
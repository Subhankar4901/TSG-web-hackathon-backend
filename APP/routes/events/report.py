from flask import Blueprint,send_file,request,jsonify,make_response
from ...models.Event import Event
from ...utils.jwt import JWT
from io import BytesIO
report_bp=Blueprint("report",__name__,url_prefix="/report")
@report_bp.route("/<id>")
def get_report(id):
    token=request.cookies.get("token")
    if JWT.validator(token):
        event=Event.query.filter_by(id=int(id)).first()
        title=event.title
        name=f"{title}_report.pdf" if title else f"report_{id}.pdf"
        report=event.report
        return send_file(BytesIO(report),download_name=name,as_attachment=True)
    else:
        resp=make_response(jsonify(messege="Unauthorised"))
        resp.status=401
        return resp
        
        
            
            
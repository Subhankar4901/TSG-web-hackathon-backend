from flask import Blueprint,send_file,request,jsonify,make_response
from ...models.Event import Event
from ...utils.jwt import JWT
from io import BytesIO
from ... import db
report_bp=Blueprint("report",__name__,url_prefix="/report")
@report_bp.route("/<id>")
def get_report(id):
    '''
    Method to get report directly from backend.
    '''
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
        
@report_bp.route("/<id>/save",methods=["POST"])
def save_report(id):
    '''
    Method to save report by admin.
    '''
    data=request.get_json()
    report=request.files["report"]
    token=data["token"]
    token_dict=JWT.validator(token)
    event=Event.query.filter_by(id=int(id)).first()
    if token_dict:
        if token_dict["type"]<3:
            event.report=report.read()
            db.session.commit()
            return make_response(jsonify(messege="Saved"),200)
        elif token_dict["type"]==3:
            if token_dict["id"]==event.organiser.id:
                event.report=report.read()
                db.session.commit()
                return make_response(jsonify(messege="Saved"),200)
            else:
                return make_response(jsonify(messege="Unauthorised"),401)
        else:
            return make_response(jsonify(messege="Unauthorised"),401)
    
    return make_response(jsonify(messege="Unauthorised"),401)
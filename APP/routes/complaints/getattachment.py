from flask import Blueprint, send_file, request, make_response, jsonify

from APP.utils.accessLevel import access_required
from ...models import Complain
from ...utils.jwt import JWT
from ...models import Complain, User
from io import BytesIO

getattachment_bp = Blueprint('getattachment', __name__, url_prefix="/")

@getattachment_bp.route("<complain_id>/getattachment/", methods=["GET"])
@getattachment_bp.route("<complain_id>/getattachment", methods=["GET"])
def getattachment(complain_id):
    token=request.cookies.get("token")
    token_dict=JWT.validator(token)
    if token_dict:
        file_data_buffer = None
        userType = int(token_dict['type'])
        userId = token_dict['id']
        if userType <= 2:
            complain = Complain.query.filter_by(id = complain_id).first()
            if complain:
                file_data_buffer = complain.attachment
        else:
            user = User.query.get(userId)
            complain = user.complaints.filter(Complain.id == complain_id).first()
            if complain:
                file_data_buffer = complain.attachment
            # print(len(file_data_buffer))
            # return "ok"
        if file_data_buffer:
            return send_file(BytesIO(file_data_buffer), attachment_filename="attachment.pdf", as_attachment = False)
    resp=make_response(jsonify(message="Unauthorised"))
    resp.status_code=401
    return resp

    
    
    


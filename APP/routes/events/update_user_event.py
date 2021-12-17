from flask import Blueprint,request,jsonify,make_response
from ...models import Event
from ...models import User
from ...utils import JWT
from ... import db

update_user_event_bp = Blueprint('update_user_event', __name__,url_prefix="/update_user_event")

#request should contain token
#request should contain emails of the participants
#request should contain event id

@update_user_event_bp.route("/",methods=["POST"])
def update_user_event():
    data = request.get_json()
    token = data.get("token")
    token_dict = JWT.validator(token)
    if token_dict:
        if token_dict["type"]<=3:
            userEmails = data.get("email")
            eventId = data.get("id")
            event = Event.query.filter_by(id=eventId)
            for userEmail in userEmails:
                user = User.query.filter_by(email=userEmail)
                User.events_participated.append(event)
                db.session.add(user)
                db.session.commit()

            resp=make_response(jsonify(message="participation added"))
            resp.status_code=201
            return resp
        else:
            resp = make_response(jsonify(message="Unauthorised"))
            resp.status_code=401
            return resp
    else:
        resp = make_response(jsonify(message="Unauthorised"))
        resp.status_code=401
        return resp


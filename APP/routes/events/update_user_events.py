from flask import Blueprint,request,jsonify,make_response
from ...models import Event
from ...models import User
from ...utils import JWT
from ... import db

update_user_events_bp = Blueprint('update_user_events', __name__,url_prefix="/update_user_events")

# request should contain token, list of emails of the participants, event id
@update_user_events_bp.route("/",methods=["POST"])
@update_user_events_bp.route("",methods=["POST"])
def update_user_events():
    data = request.get_json()
    token = data.get("token")
    token_dict = JWT.validator(token)
    participant_emails = data.get("emails")
    eventId = data.get("event_id")
    if token_dict and participant_emails and eventId:
        participant_emails = list(participant_emails)
        eventId = int(eventId)
        event_obj = Event.query.get(eventId)
        if ((token_dict["type"] < 3) or ((token_dict["type"]==3) and (event_obj.organiser.id==token_dict["id"]))):
            for email in participant_emails:
                user = User.query.filter_by(email=email).first()
                if not event_obj in user.events_participated:
                    user.events_participated.append(event_obj)
                db.session.add(user)
                db.session.commit()

            resp=make_response(jsonify(message="participation added"))
            resp.status_code=201
            return resp
    resp = make_response(jsonify(message="Unauthorised"))
    resp.status_code=401
    return resp


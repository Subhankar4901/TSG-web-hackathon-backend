from flask import Blueprint, jsonify,request,make_response
from ....utils.sendEmail import sendEmail
from ....models import OTP, User
from .... import db
from random import randint
from datetime import datetime

sendotp_bp = Blueprint('sendotp', __name__, url_prefix="/sendotp")


@sendotp_bp.route("/", methods=["POST"])
@sendotp_bp.route("", methods=["POST"])
def sendotp():
    data = request.get_json()
    user_email = data.get("email")
    user = User.query.filter_by(email=user_email).first()
    if not(user and (int(user.type) == 4)):
        resp=make_response(jsonify({"message":"User Not authorized to send otp"}))
        resp.headers.add("Content-Type","aplication/json")
        return resp
    user = OTP.query.filter_by(email=user_email).first()
    valid_time = 5 #in minutes

    if user:
        timeDelta = datetime.now() - user.time

        if (timeDelta.total_seconds() <= valid_time*60):
            secondsLeft =int( valid_time*60 - timeDelta.total_seconds())
            resp=make_response(jsonify({"message":f"otp already sent, check your email. Retry in {secondsLeft} seconds"}))
            resp.headers.add("Content-Type","aplication/json")
            return resp

        db.session.delete(user)
        db.session.commit()

    message_subject = f"OTP for login"
    otp = 100000 #randint(100000, 999999)
    message_body = f"OTP is {otp}. It is valid for {valid_time} minutes only."
    sendEmail(messageSubject=message_subject, messageBody=message_body, recipients=[user_email])
    response = {
        "message": "OTP sent successfully"
    }
    newUser = OTP(email=user_email, otp=otp, time=datetime.now())
    db.session.add(newUser)
    db.session.commit()
    return jsonify(response)

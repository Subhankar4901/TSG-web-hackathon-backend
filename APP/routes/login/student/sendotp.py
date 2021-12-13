from flask import Blueprint, jsonify,request
from ....utils.sendEmail import sendEmail
from ....models import OTP
from .... import db
from random import randint
from datetime import datetime

sendotp_bp = Blueprint('sendotp', __name__, url_prefix="/sendotp")


@sendotp_bp.route("/", methods=["POST"])
@sendotp_bp.route("", methods=["POST"])
def sendotp():
    data = request.get_json()
    user_email = data["email"]
    message_subject = f"OTP subject"
    otp = randint(100000, 999999)
    message_body = f"OTP is {otp}"
    sendEmail(messageSubject=message_subject, messageBody=message_body, recipients=[user_email])
    response = {
        "message": "OTP sent successfully"
    }
    newUser = OTP(email=user_email, otp=otp, unixTimeStamp=datetime.timestamp(datetime.now()))
    db.session.add(newUser)
    db.session.commit()
    return jsonify(response)

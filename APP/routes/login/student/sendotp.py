from flask import Blueprint, request
from ....utils.sendEmail import sendEmail
from random import randint

sendotp_bp = Blueprint('sendotp', __name__, url_prefix="/sendotp")


@sendotp_bp.route("/", methods=["POST"])
@sendotp_bp.route("", methods=["POST"])
def sendotp():
    data = request.get_json()
    user_email = data["email"]
    message_subject = f"OTP subject"
    message_body = f"OTP is {randint(100000, 999999)}"
    sendEmail(messageSubject=message_subject, messageBody=message_body, recipients=[user_email])
    return "OTP sent successfully"

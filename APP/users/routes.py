from flask import Blueprint,request,make_response,jsonify
from ..models import User
from ..utils.jwt import JWT
from ..utils.idType import parse_id
import bcrypt
user=Blueprint('user',__name__)
# For login users.
@user.route('/login',methods=['POST'])
def login():
    data=request.get_json()
    identifier=data["user"]
    password=data["password"]
    id_type=parse_id(identifier)
    if id_type == 1:
        user_obj=User.query.filter_by(roll=identifier).first()
    elif id_type==2:
        user_obj=User.query.filter_by(insti_email=identifier).first()
    elif id_type==3:
        user_obj=User.query.filter_by(email=identifier).first()
    else:
        user_obj=User.query.filter_by(username=identifier).first()
    if user_obj:
        if bcrypt.checkpw(password=password.encode("utf-8"),hashed_password=user_obj.password):
            resp=make_response(jsonify(response=1,token=JWT.tokenizer({"user_id":user_obj.id,"type":user.type})))
            resp.status_code=200
            resp.headers.add("Content-Type","aplication/json")
            return resp
        else:
            resp=make_response(jsonify(response=0))
            resp.status_code=200
            resp.headers.add("Content-Type","aplication/json")
            return resp
    else:
        resp=make_response(jsonify(response=-1))
        resp.status_code=200
        resp.headers.add("Content-Type","aplication/json")
        return resp

#For register users.
@user.route('/signup',methods=['POST'])
def signup():
    pass
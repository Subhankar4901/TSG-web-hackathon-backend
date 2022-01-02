from flask.json import  jsonify
from flask import request, make_response
from functools import wraps
from .jwt import JWT



'''
A decorator for access level validation
level - 1 admin
level - 2 tsg officials
level - 3 society and cells
level - 4 students
'''
def access_required(level = 1):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            token = request.cookies.get("cookies")
            token_dict = None
            '''
            Add more possible ways to get JWT token here
            '''
            if token:
                token_dict=JWT.validator(token)
            if token_dict and token_dict.get("type") and int(token_dict.get("type")) <= level:
                return fn(*args, **kwargs)
            else:
                resp=make_response(jsonify(message="Unauthorised"))
                resp.status_code=401
                return resp
        return decorator
    return wrapper

from flask.json import  jsonify
from flask import request
from functools import wraps
from .jwt import JWT



'''
A decorator for access level validation
level - 1 admin
level - 2 tsg officials
level - 3 society and cells
level - 4 stucdents
'''
def access_required(level = 1):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            token = None
            data = request.get_json()
            token_dict = None
            if data:
                token = data.get("token")
                
            if token is None:
                data = request.args
                if data:
                    token = data.get("token")
            '''
            Add more possible ways to get JWT token here
            '''
            if token:
                token_dict=JWT.validator(token)
            if token_dict and token_dict.get("type") and int(token_dict.get("type")) <= level:
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Not Allowed!"), 401
        return decorator
    return wrapper

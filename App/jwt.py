from itsdangerous import JSONWebSignatureSerializer
from . import app
salt=b'$2b$12$i/lNuys3HrzDZeG5XCditu'
sauce=JSONWebSignatureSerializer(secret_key=app.secret_key,salt=salt)
def getToken(user:str):
    token=sauce.dumps({"user":user}).decode("utf_8")
    return token
def validateToken(token):
    try:
        user=sauce.loads(token)
        return user["user"]
    except:
        return None
    
    
    
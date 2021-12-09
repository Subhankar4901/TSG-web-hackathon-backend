from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import time
secret_key = 'secret_key'
s= Serializer(secret_key, expires_in=30)
a={"email": "subhankarh"}
token = s.dumps(a).decode("utf-8")
time.sleep(31)
data=s.loads(token)
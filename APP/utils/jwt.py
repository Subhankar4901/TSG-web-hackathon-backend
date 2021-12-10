from itsdangerous import JSONWebSignatureSerializer,TimedJSONWebSignatureSerializer
from decouple import config


class JWT:
    '''A utility class to create and validate Json web tokens    
    '''
    __salt__=b'$2b$12$i/lNuys3HrzDZeG5XCditu'
    __expire__=300 # seconds
    normal_sauce=JSONWebSignatureSerializer(config("app_secret_key"),salt=__salt__)
    timed_sauce=TimedJSONWebSignatureSerializer(config("app_secret_key"),expires_in=__expire__)
    @classmethod
    def tokenizer(cls,data:dict,time:bool=False):
        '''
        set time=True for timed Json web token.
        '''
        if time:
            token=cls.timed_sauce.dumps(data).decode("utf-8")
        else:
            token=cls.normal_sauce.dumps(data).decode("utf-8")
        return token
    @classmethod
    def validator(cls,token:str,time:bool=False):
        '''
        set time=True for timed Json web token.
        '''
        try:
            if time:
                data=cls.timed_sauce.loads(token)
            else:
                data=cls.normal_sauce.loads(token)
            return data
        except:
            return None

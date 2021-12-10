import re
def parse_id(id:str):
    '''
    A utility function that parses user entered id and return it's type.
    
    Return;
    1 : Roll number
    2 : institute email
    3 : email other than institute email
    4 : username
    '''
    email_pattern=re.compile(r'^[a-zA-Z0-9+_.-]+@([a-zA-Z0-9.-]+)$')
    roll_pattern=re.compile(r'^\d\d([A-Z][A-Z])[0-9A-Z]+$')
    kgp_domains=["iitkgp.ac.in","kgpian.iitkgp.ac.in"]
    if email_pattern.match(id):
        domain=email_pattern.match(id).group(1)
        if domain in kgp_domains:
            return 2
        return 3
    elif roll_pattern.match(id):
        return 1
    else:
        return 4
    
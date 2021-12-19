from datetime import datetime
from flask import Flask,url_for
from flask_sqlalchemy import SQLAlchemy
from decouple import config
from flask_mail import Mail, Message
from flask_migrate import Migrate
from flask.json import JSONEncoder
from flask_cors import CORS

# Main application and configuration
app=Flask(__name__)
CORS(app)

# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = config("email_sender")
app.config['MAIL_PASSWORD'] = config("email_password")
app.config["MAIL_DEFAULT_SENDER"]=config("email_sender")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
# Our custom jsonencoder for datetime.
class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime):
            return obj.isoformat()
        return super().default(obj)
app.json_encoder=CustomJSONEncoder
# instantiate the mail class
mail = Mail(app)

app.secret_key=config("app_secret_key")
app.config["SQLALCHEMY_DATABASE_URI"]=config("db_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database
db=SQLAlchemy(app)
migrate = Migrate(app, db)

from .routes import base_bp

#This below route is for visualising url paths.Only for development purposes
app.register_blueprint(base_bp)
@app.route("/map")
def get_map():
    data={}
    for rule in app.url_map.iter_rules():
        try:
            data[str(rule.endpoint)]=str(url_for(rule.endpoint))
        except:
            pass
    return data

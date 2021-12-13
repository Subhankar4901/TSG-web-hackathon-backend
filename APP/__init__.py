from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from decouple import config
from flask_mail import Mail, Message


# Main application and configuration
app=Flask(__name__)

# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = config("email_sender")
app.config['MAIL_PASSWORD'] = config("email_password")
app.config["MAIL_DEFAULT_SENDER"]=config("email_sender")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# instantiate the mail class
mail = Mail(app)

app.secret_key=config("app_secret_key")
app.config["SQLALCHEMY_DATABASE_URI"]=config("db_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database
db=SQLAlchemy(app)

from .routes import base_bp

app.register_blueprint(base_bp)

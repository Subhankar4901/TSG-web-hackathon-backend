from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from decouple import config
# Main application and configuration
app=Flask(__name__)
app.secret_key=config("app_secret_key")
app.config["SQLALCHEMY_DATABASE_URI"]=f"mysql://{config('dbUser')}:{config('dbPassword')}@{config('dbHost')}/{config('dbName')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Database
db=SQLAlchemy(app)


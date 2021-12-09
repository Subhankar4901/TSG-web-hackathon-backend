from flask import Flask
app=Flask(__name__,template_folder="../templates")
from decouple import config
app.secret_key="1052d3e96a21b62bf4e02ac9ee75abd4"
app.config["SQLALCHEMY_DATABASE_URI"]=f"mysql://{config('user')}:{config('password')}@{config('host')}/{config('dbname')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from .routes import *

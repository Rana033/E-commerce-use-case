from flask import Flask
from app.config import Config
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy 
app=Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)
api = Api(app)
from app.models import category,user

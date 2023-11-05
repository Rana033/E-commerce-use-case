from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app=Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
api = Api(app)

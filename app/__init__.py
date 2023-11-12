from flask import Flask
from app.config import Config
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy 
#################################################


app=Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)
api = Api(app)


#######################################################3
from app.resources import category_resource,user_resource,product_resource,cart_resource,favourite_resource


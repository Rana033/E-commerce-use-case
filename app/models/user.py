from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "user"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String,nullable=False)
    user_name=db.Column(db.String,unique=True,nullable=False)
    user_email=db.Column(db.String,unique=True,nullable=False)
    passward_hash=db.Column(db.String,nullable=False)
    role=db.Column(db.String,nullable=False)
    created_at=db.Column(db.DateTime,nullable=False,default=datetime.now())
    avatar_id=db.Column(db.String)


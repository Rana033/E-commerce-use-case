from app import db
from datetime import datetime

class Favourite(db.Model):
    __tablename__ = "favourite"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    added_at=db.Column(db.DateTime,nullable=False,default=datetime.now())


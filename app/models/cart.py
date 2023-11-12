from app import db
from datetime import datetime

class Cart(db.Model):
    __tablename__ = "cart"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    added_at=db.Column(db.DateTime,nullable=False,default=datetime.now())
    count=db.Column(db.Integer,default=0)


from app import db

class Category(db.Model):
    __tablename__ = "category"
    
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,nullable=False)
    user_email=db.Column(db.String,db.ForeignKey('user.user_email'),nullable=False)




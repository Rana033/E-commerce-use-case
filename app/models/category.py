from app import db

class Category(db.Model):
    __tablename__ = "category"
    
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,nullable=False)
    
    def to_dict(self):
        return {
            'id':self.id,
            'name':self.name
        }
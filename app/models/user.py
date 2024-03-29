from app import db
import enum
from datetime import datetime

class RoleEnum(enum.Enum):
    user = "user"
    admin = "admin"
    seller = "seller"
    

class User(db.Model):
    __tablename__ = "user"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String,nullable=False)
    user_name=db.Column(db.String,unique=True,nullable=False)
    user_email=db.Column(db.String,unique=True,nullable=False)
    password=db.Column(db.String,nullable=False)
    role=db.Column(db.Enum(RoleEnum),nullable=False)
    created_at=db.Column(db.DateTime,nullable=False,default=datetime.now())
    avatar_id=db.Column(db.String)
    
    def to_dict(self):
        return {
            'id':self.id,
            'name':self.name,
            'user_name':self.user_name,
            'user_email':self.user_email,
            'password':self.password,
            'role':self.role.value if isinstance(self.role, RoleEnum) else None,
            'avatar_id':self.avatar_id,
        }


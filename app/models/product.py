from app import db

class Product(db.Model):
    __tablename__ = "product"
    
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,nullable=False)
    description=db.Column(db.String,nullable=False)
    product_img= db.relationship('Image', backref='product', lazy=True)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    data = db.Column(db.LargeBinary)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)


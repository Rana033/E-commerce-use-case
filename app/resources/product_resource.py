from flask import jsonify , request
from flask_restful import Resource
from app import db,api
from app.models.product import Product,Image
from flask_jwt_extended import  jwt_required, get_jwt_identity
from app.resources import crud


class ProductResource(Resource):
    #create product

    @jwt_required()
    def post(self):
        try:
            current_user_id = get_jwt_identity()
            data=request.get_json()
            new_product=Product(**data,user_id=current_user_id)
            db.session.add(new_product)
            db.session.commit()
            return jsonify({'message':'created successfully'},201)
        except Exception as e:
            return jsonify({'error': f'An error occurred while creation: {str(e)}'}, 500)
        
        
    #get all product
    def get(self):
        return crud.get_all(Product)




class ProductResourceID(Resource):
    #get product by id
    def get(self,id):
        return crud.get_one_entity(Product,id)
    
    
    
    #update product 
    @jwt_required()
    def put(self,id):
        try:
            data = request.get_json()
            current_user_id = get_jwt_identity()

            print(current_user_id)
            product = db.session.query(Product).get(id)
            if not product:
                return jsonify({'error': 'User not found'}, 404)

            for key, value in data.items():
                setattr(product, key, value)
            db.session.commit()
            return jsonify({'message': 'product is updated successfully'}, 200)
        except Exception as e:
            return jsonify({'error': f'An error occurred while retrieving all data: {str(e)}'}, 500)
    
    #delete product
    @jwt_required()
    def delete(self,id):
        try:
            current_user_id = get_jwt_identity()
            if not (
                current_product := db.session.query(Product)
                .filter(Product.id == id)
                .delete()
            ):
                return jsonify({'error':'delete product failed'},400)
            db.session.commit()
            return jsonify({'message':'product is deleted successfully'},200)
        except Exception as e:
            return jsonify({'error': f'An error occurred while retrieving all data: {str(e)}'}, 500)
        
        




################################################################

#Image of products

class ImageResource(Resource):
    #create image:
    def post(self):
        return crud.create_entity(Image)
    
    #get all images
    def get(self):
        return crud.get_all(Image)
    
    
    
    
########################################
#id
class ImageResourceID(Resource):
    #get image by id
    def get(self,id):
        return crud.get_one_entity(Image,id)
            
    
    #update image by id
    def put(self,id):
        return crud.update_entity(Image,id)
            
    
    #delete image by id
    def delete(self,id):
        return crud.delete_entity(Image,id)


api.add_resource(ProductResource, '/product')
api.add_resource(ProductResourceID, '/product/<int:id>')

api.add_resource(ImageResource, '/image')
api.add_resource(ImageResourceID, '/image/<int:id>')
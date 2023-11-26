from flask import jsonify , request
from flask_restful import Resource
from app import db,api
from app.models.favourite import Favourite
from flask_jwt_extended import  jwt_required, get_jwt_identity
from app.resources import crud



class FavouriteResource(Resource):
    #create product

    @jwt_required()
    def post(self):
        try:
            current_user_id = get_jwt_identity()
            data=request.get_json()
            new_fav=Favourite(**data,user_id=current_user_id)
            db.session.add(new_fav)
            db.session.commit()
            return jsonify({'message':'created successfully'},201)
        except Exception as e:
            return jsonify({'error': f'An error occurred while creation: {str(e)}'}, 500)
        
        
    #get all product
    def get(self):
        return crud.get_all(Favourite)




class FavouriteResourceID(Resource):
    #get product by id
    def get(self,id):
        return crud.get_one_entity(Favourite,id)
    
    #delete product
    @jwt_required()
    def delete(self,id):
        try:
            current_user_id = get_jwt_identity()
            if not (
                current_product := db.session.query(Favourite)
                .filter(Favourite.id == id)
                .delete()
            ):
                return jsonify({'error':'delete favourite failed'},400)
            db.session.commit()
            return jsonify({'message':'favourite is deleted successfully'},200)
        except Exception as e:
            return jsonify({'error': f'An error occurred while retrieving all data: {str(e)}'}, 500)
        
        
        
        
api.add_resource(FavouriteResource, '/product')
api.add_resource(FavouriteResourceID, '/product/<int:id>')
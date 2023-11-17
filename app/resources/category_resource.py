from flask import jsonify , request
from flask_restful import Resource
from app import db,api
from app.models.category import Category
from app.resources import crud

class CategoryResource(Resource):
    #create category:
    def post(self):
        return crud.create_entity(Category)
    
    #get all categories
    def get(self):
        return crud.get_all(Category)
    
    
    
    
########################################
#id
class CategoryResourceID(Resource):
    #get category by id
    def get(self,id):
        return crud.get_one_entity(Category,id)
            
    
    #update category by id
    def put(self,id):
        return crud.update_entity(Category,id)
            
    
    #delete category by id
    def delete(self,id):
        return crud.delete_entity(Category,id)


api.add_resource(CategoryResource, '/category')
api.add_resource(CategoryResourceID, '/category/<int:id>')


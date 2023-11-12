from flask import jsonify , request
from flask_restful import Resource
from app import db,api
from app.models.category import Category


class CategoryResource(Resource):
    #create category:
    def post(self):
        data=request.get_json()
        if 'name' not in data:
            return jsonify({'error': 'category name is required'},400)
        new_category=Category(name=data['name'])
        db.session.add(new_category)
        db.session.commit()
        return jsonify({'message':'category is created successfully'},201)
    
    #get all categories
    def get(self):
        categories=db.session.query(Category).all()
        if len(categories)==0:
            return jsonify({'error': 'not found'},404)
        category_list=[{'id':cat.id,'name':cat.name} for cat in categories]
        return jsonify(category_list)
    
class CategoryResourceID(Resource):
    #get category by id
    def get(self,id):
        cat = db.session.query(Category).get(id)
        if  cat==None:
            return jsonify({'error': 'not found'},404)
        return jsonify({'id': cat.id, 'name': cat.name})
    
    #update category by id
    def put(self,id):
        data=request.get_json()
        if 'name' not in data:
            return jsonify({'error': 'category name is required'},400)
        if db.session.query(Category).filter(Category.id==id).update ({Category.name: data['name']}):
            db.session.commit()
            return jsonify({'message':'category is updated successfully'},200)
        return jsonify({'error':'update category failed'},400)
    
    
    #delete category by id
    def delete(self,id):
        deleted_category=db.session.query(Category).get(id)
        if deleted_category==None:
            return jsonify({'error': 'not found'},404)       
        if db.session.query(Category).filter(Category.id==id).delete():
            db.session.commit()
            return jsonify({'message':'category is deleted successfully'},200)
        return jsonify({'error':'delete category failed'},400)


api.add_resource(CategoryResource, '/category')
api.add_resource(CategoryResourceID, '/category/<int:id>')


from flask import jsonify , request
from app import db

#creation
def create_entity(model):
    try:
        data=request.get_json()
        new_entity=model(**data)
        db.session.add(new_entity)
        db.session.commit()
        return jsonify({'message':'created successfully'},201)
    except Exception as e:
        return jsonify({'error': f'An error occurred while creation: {str(e)}'}, 500)

#get all
def get_all(model):
    try:
        entities=db.session.query(model).all()
        if len(entities)==0:
            return jsonify({'error': 'not found'},404)
        print(model)
        entity_list=[ent.to_dict() for ent in entities]
        print(entity_list)
        return jsonify(entity_list)
    except Exception as e:
        return jsonify({'error': f'An error occurred while retrieving all data: {str(e)}'}, 500)
    



#get by id

def get_one_entity(model,id):
    try:
        entity = db.session.query(model).get(id)
        if entity is None:
            return jsonify({'error': 'not found'},404)
        return jsonify(entity.to_dict())
    except Exception as e:
        return jsonify({'error': f'An error occurred while retrieving data: {str(e)}'}, 500)
    

#update by id

def update_entity(model,id):
    try:

        data = request.get_json()

        print(id)
        entity = db.session.query(model).get(id)
        if not entity:
            return jsonify({'error': 'not found'}, 404)

        for key, value in data.items():
            setattr(entity, key, value)
        db.session.commit()
        return jsonify({'message': 'updated successfully'}, 200)
    except Exception as e:
                return jsonify(
                    {'error': f'An error occurred while updating: {str(e)}'},
                    500,
                )
                
                
#delete by id

def delete_entity(model,id):
    try:
        if not (
            current_entity := db.session.query(model)
            .filter(model.id == id)
            .delete()
        ):
            return jsonify({'error':'deleted failed'},400)
        db.session.commit()
        return jsonify({'message':'deleted successfully'},200)
    except Exception as e:
        return jsonify({'error': f'An error occurred while deleting: {str(e)}'}, 500)
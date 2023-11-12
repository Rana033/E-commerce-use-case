from flask import jsonify , request
from flask_restful import Resource
from app import db,api,jwt
from app.models.user import User
from passlib.hash import sha256_crypt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

############################################

class RegistrationUser(Resource):
    def post(self):
        data = request.get_json()
        print("##############",data.values())
        new_user=User(*data.values(),password_hash=sha256_crypt.hash(data['password']))
        try:
            access_token = create_access_token(identity=new_user.id)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({'message':'success registeration','access_token':access_token},201)
        except Exception as e:
            # Handle exceptions, such as database errors
            db.session.rollback()
            return jsonify({'message': 'Error creating user'}), 500
    

 
    
    
    
    
    
    
    
    
api.add_resource(RegistrationUser, '/user')

from flask import jsonify , request
from flask_restful import Resource,abort
from app import db,api,jwt
from app.models.user import User
from passlib.hash import sha256_crypt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

############################################

class RegistrationUser(Resource):
    def post(self):
        data = request.get_json()
        password=sha256_crypt.hash(data['password'])
        del data['password']
        new_user = User(**data, password=password)
        try:
            access_token = create_access_token(identity=new_user.id)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({'message':'success registeration','access_token':access_token},201)
        except Exception as e:
            # Handle exceptions, such as database errors
            db.session.rollback()
            return jsonify({'message': 'Error creating user'}, 500)
        
        
 

class UserAll(Resource):
    def post(self):
        try:
            data = request.get_json()

            user_log = db.session.query(User).filter(User.user_email==data['user_email']).first()
            print(user_log)
            if user_log and sha256_crypt.verify(data['password'],user_log.password):
                access_token = create_access_token(identity=user_log.id)
                return jsonify({'message': 'Login successful', 'access_token': access_token}, 200)
            else:
                return jsonify({'message':'invalid email or password'},401)

        except Exception as e:
            abort(400, message=str(e))
    
    
    
    
    
api.add_resource(RegistrationUser, '/user')
api.add_resource(UserAll, '/user/log')

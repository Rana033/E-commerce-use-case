from flask import jsonify , request
from flask_restful import Resource,abort
from app import db,api,jwt
from app.models.user import User,RoleEnum
from passlib.hash import sha256_crypt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.resources import crud

############################################

class RegistrationUser(Resource):
    def post(self):
        data = request.get_json()
        password=sha256_crypt.hash(data['password'])
        del data['password']
        new_user = User(**data, password=password)
        #print(new_user.id)
        try:
            db.session.add(new_user)
            db.session.commit()
            user=db.session.query(User).filter(User.user_email==data['user_email']).first()
            #print(new_user.user_email,user.id)
            access_token = create_access_token(identity=user.id)

            return jsonify({'message':'success registeration','access_token':access_token},201)
        except Exception as e:
            # Handle exceptions, such as database errors
            db.session.rollback()
            print(str(e))
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
                return jsonify({'message':'invalid email or password'},401)

    def get(self):
        return crud.get_all(User)
    
    
    


        
            
class UserBy(Resource):

    
    def get(self):
        role=request.get_json()
        if not role:
            return jsonify({'error': 'Role parameter is required'}, 400)
        users=db.session.query(User).filter(User.role==role['role']).all()
        if len(users)==0:
            return jsonify({'error': 'not found'},404)
        user_list=[user.to_dict() for user in users]    
        return jsonify(user_list)
    
    @jwt_required()
    def get(self):
        current_user_id = get_jwt_identity()
        if (
            current_user := db.session.query(User)
            .filter(User.id == current_user_id)
            .first()
        ):
            return jsonify(current_user.to_dict())
        else:
            return jsonify({'message': 'User not found'}, 404)
    
    
    @jwt_required()
    def put(self):
        data = request.get_json()
        current_user_id = get_jwt_identity()

        print(current_user_id)
        user = db.session.query(User).get(current_user_id)
        if not user:
            return jsonify({'error': 'User not found'}, 404)

        for key, value in data.items():
            setattr(user, key, value)
        db.session.commit()
        return jsonify({'message': 'user is updated successfully'}, 200)
    
    
    @jwt_required()
    def delete(self):
        current_user_id = get_jwt_identity()
        if not (
            current_user := db.session.query(User)
            .filter(User.id == current_user_id)
            .delete()
        ):
            return jsonify({'error':'delete user failed'},400)
        db.session.commit()
        return jsonify({'message':'user is deleted successfully'},200)
    
api.add_resource(RegistrationUser, '/user')
api.add_resource(UserAll, '/user/all')
api.add_resource(UserBy, '/user/by')

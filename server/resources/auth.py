from flask_restful import Resource
from flask import request
from marshmallow import ValidationError
from server.extension import db
from server.models import User
from server.Schemas import user_schema
from flask_jwt_extended import (create_access_token,get_jwt_identity,jwt_required)
# Register new user account
class SignUp(Resource):
    def post(self):
        try:

            data = user_schema.load(request.get_json())
            existing_user = User.query.filter_by(username=data["username"]).first()
            if existing_user:
                # prevent duplicate usernames
                return ({"error":"User already exists"}),409  
            # create a new user and securely hash the password
            user = User(username=data["username"])
            user.password = data["password"]
            db.session.add(user)
            db.session.commit()
            return ({"message":"User successfully created","user":user_schema.dump(user)}),201
        except ValidationError as e:
            return ({"error":e.messages}),400
        except Exception as error:
        
            db.session.rollback()
            print(error)
            return ({"error":str(error)}),500
# Authenticate an existing user and generate a token 
class Login(Resource):
    def post(self):
        data = request.get_json() or {}
        username = data.get("username")
        password = data.get("password")
        # ensure both credentials are provided
        if not username or not password:
            return ({"error":"Provide username or password"}),400

        user = User.query.filter_by(username=username).first()

        if not user or not user.check_password(password):
            return({"error":"Invalid email or password"}),401
        # Generate a token containing user's id
        access_token = create_access_token(identity=str(user.id))

        return({"message":"Login successful!",
                "access_token":access_token,
                "user":user_schema.dump(user)
                }),200

class CheckSession(Resource):
    # protect this route so only authenticated users access it
    @jwt_required()
    def get(self):
        # get user's id from the JWT
        user_id = get_jwt_identity()
        user = User.query.get(int(user_id))

        if not user:
            return({"error":"User not found"}),404

        return({"user":user_schema.dump(user)}),200
      




from flask_restful import Resource
from flask import request
from marshmallow import ValidationError
from server.extension import db
from server.models import User
from server.Schemas import user_schema

class SignUp(Resource):
    def post(self):
        try:
            data = user_schema.load(request.get_json())
            existing_user = User.query.filter_by(username=data["username"]).first()
            if existing_user:
                return ({"error":"User already exists"}),409

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


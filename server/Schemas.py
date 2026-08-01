from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from mashmallow import fields
from server.models import User,Note
from server.extension import db

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        exclude = ("password_hash")

    password = fields.String(load_only=True,required=True)

class NoteSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Note
        load_instance = True
        include_relationship = True


from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from server.models import User,Note
from server.extension import db

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = False
        exclude = ("password_hash",)
# allow plain password instead of serializing the hash password
    password = fields.String(load_only=True,required=True)

class NoteSchema(SQLAlchemyAutoSchema):
    user_id = fields.Integer(dump_only=True)
    class Meta:
        model = Note
        load_instance = False
        include_fk= True

user_schema = UserSchema()
users_schema = UserSchema(many=True)

note_schema = NoteSchema()
notes_schema = NoteSchema( many=True)

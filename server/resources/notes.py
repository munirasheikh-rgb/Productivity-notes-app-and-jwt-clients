from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required,get_jwt_identity

from server.extension import db
from server.models import Note
from server.Schemas import note_schema,notes_schema

class Notes(Resource):
    def get(self):
        user_id = int(get_jwt_identity())

        page = request.args.get("page",1,type=int)
        per_page = request.args.get("per_page",5,type=int)

        pagination = (Note.query.filter_by(user_id=user_id).order_by(Note.id.desc())
                      .paginate(page=page,per_page=per_page))


        return({"notes":notes_schema.dump(pagination.items),
                "pagination":{
                    "current_page":pagination.page,
                    "per_page":pagination.per_page,
                    "total_items":pagination.total,
                    "has_next":pagination.has_next,
                    "has_previous":pagination.has_previous
                }
                }),200
from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required,get_jwt_identity

from server.extension import db
from server.models import Note
from server.Schemas import note_schema,notes_schema

class Notes(Resource):
    @jwt_required()
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
                    "has_previous":pagination.has_prev
                }
                }),200
    
    @jwt_required()
    def post(self):
        user_id = int(get_jwt_identity())

        try:
            data = note_schema.load(request.get_json() or {})

            note = Note(title=data["title"],content=data.get("content"),
                category=data.get("category","general"),is_pinned=data.get("is_pinned",False),user_id=user_id)

            db.session.add(note)
            db.session.commit()

            return({"message":"Note Created sucessfully",
                    "note":note_schema.dump(note)}),201
        
        except Exception as error:
            db.session.rollback()
            print(error)
            return({"error":"Unable to create a note"}),500
        
class NoteById(Resource):
    @jwt_required()
    def patch(self,id):
       user_id = int(get_jwt_identity())
       
       note = Note.query.filter_by(id=id,user_id=user_id).first()
       if not note:
           return({"error":"Note not found"}),404

       try:
           data = note_schema.load(request.get_json() or{} , partial=True)

           r_fields = ["title","content","category","is_pinned"]
           for field in r_fields:
               if field in data:
                   setattr(note,field ,data["field"] )

           db.session.commit()
           return({"message":"Note updated successfully",
                           "note":note_schema.dump(note)}),200
       except Exception as e :
           db.session.rollback()
           print(e)
           return({"error":"Unable to update this note"}),400

 
                 

       
      
    
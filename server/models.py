from extension import db

class User(db.Model):
    __tablename__ ="users"

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String,nullable=False,unique=True)
    password_hash = db.Column(db.String,nullable=False)
    notes = db.relationship("Note",backref="user",cascade="all,delete-orphan")

class Note(db.Model):
    __tablename__ = "notes"
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)
    title = db.Column(db.String,nullable=False)
    content= db.Column(db.Text)
    category = db.Column(db.String,default="general",nullable=False)
    is_pinned = db.Column(db.Boolean,default=False,nullable=False) 

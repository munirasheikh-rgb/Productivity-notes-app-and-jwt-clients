from extension import db,bcrypt

class User(db.Model):
    __tablename__ ="users"

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String,nullable=False,unique=True)
    password_hash = db.Column(db.String,nullable=False)
    notes = db.relationship("Note",backref="user",cascade="all,delete-orphan")
# add secure password handling
    @property
    def password(self):
        raise AttributeError("Password cannot be viewed")
    @password.setter
    def password(self,password):
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self,password):
       return bcrypt.check_password_hash(self.password_hash,password)
    
    def __repr__(self):
     return f"<User {self.username}>"
    
class Note(db.Model):
    __tablename__ = "notes"
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)
    title = db.Column(db.String,nullable=False)
    content= db.Column(db.Text)
    category = db.Column(db.String,default="general",nullable=False)
    is_pinned = db.Column(db.Boolean,default=False,nullable=False) 

    def __repr__(self):
         return f"<Note {self.title}>"
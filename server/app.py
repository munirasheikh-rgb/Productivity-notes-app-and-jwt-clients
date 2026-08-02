from flask import Flask,make_response
from server.extension import db,migrate,bcrypt,jwt,ma,cors,api
from server.config import Config

from server.resources.auth import SignUp,Login,CheckSession
from server.resources.notes import Notes,NoteById
app = Flask(__name__)
app.config.from_object(Config)

api.add_resource(SignUp,"/signup")
api.add_resource(Login,"/login")
api.add_resource(CheckSession,"/me")
api.add_resource(Notes,"/notes")
api.add_resource(NoteById,"/notes/<int:id>")

db.init_app(app)
migrate.init_app(app,db)
bcrypt.init_app(app)
jwt.init_app(app)
ma.init_app(app)
cors.init_app(app)
api.init_app(app)

from server.models import User,Note
# from server.resources.auth import SignUp

# api.add_resource(SignUp,"/signup")

@app.route("/",methods=["GET"])
def index():
    return make_response({"message":"Welcome to Notes Productivity app"})


if __name__ == "__main__":
    app.run(port=5555,debug=True)
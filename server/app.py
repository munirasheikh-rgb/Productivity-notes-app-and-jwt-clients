from flask import Flask,make_response
from server.extension import db,migrate,bcrypt,jwt,ma,cors
from server.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app,db)
bcrypt.init_app(app)
jwt.init_app(app)
ma.init_app(app)
cors.init_app(app)

from server.models import User,Note

@app.route("/")
def index():
    return make_response({"message":"Welcome to Notes Productivity app"})


if __name__ == "__main__":
    app.run(port=5555,debug=True)
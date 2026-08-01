from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Metadata
from flask_migrate import Migrate
from flask_bcrypt  import Bcrypt
from flask_jwt_extended import JWTManager
from marshmallow_sqlalchemy import Marshmallow

metadata =Metadata()
db = SQLAlchemy(metadata=metadata)
migrate = Migrate()
bcrypt = Bcrypt()
ma = Marshmallow()
jwt =JWTManager()


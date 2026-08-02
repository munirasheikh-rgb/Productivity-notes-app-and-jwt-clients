from server.models import User,Note
from server.extension import db
from server.app import app

with app.app_context():
    Note.query.delete()
    User.query.delete()
    db.session.commit()   #clear previous user data to prevent duplicates
# seed users table
    Amina =User(username="Amina")
    Amina.password = "amina1234"

    willson =User(username="Willson")
    willson.password = "test567"

    johnson =User(username="Johnson")
    johnson.password ="johny789"

    db.session.add_all([Amina,willson,johnson])
    db.session.commit()
# seed notes table
    note1 = Note(title="Flask RESTFUL",content="practice creating routes and implement all CRUD operations",category="study",is_pinned=True,user=Amina)
    note2 = Note(title="JWT",content="process of intergrationg JWT to login routes and implement route protection",category="backend-development",is_pinned=False,user=Amina)
    note3 = Note(title="Backend frameworks",content="Types of backend framework which solve complex problems and easy to work with",is_pinned=True,user=willson)
    note4 = Note(title="Finance intelligence",content="power of saving",category="personal",user=johnson)
    note5 = Note(title="shopping",content="my shopping list",category="personal",is_pinned=True,user=willson)
    note6 = Note(title="Biuld full-stack app",content="frameworks,libraries and tools needed",category="professional",is_pinned=True,user=johnson)

    db.session.add_all([note1,note2,note3,note4,note5,note6])
    db.session.commit()

    print("Database successfully seeded")
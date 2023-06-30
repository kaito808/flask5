from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#insert tables below

class Pet(db.Model):
    """Pet."""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(50),
                     nullable=False,
                     unique=True)
    species = db.Column(db.String(30), nullable=True)
    hunger = db.Column(db.Integer, nullable=False, default=20)

class Story(db.Model):
    """Story."""

    __tablename__ = "stories"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False, unique=True)

    category = db.Column(db.Integer, nullable=False, default=0)

    content = db.Column(db.Text, nullable=False)

#keep it
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

    with app.app_context():
        db.create_all()
        db.session.commit()

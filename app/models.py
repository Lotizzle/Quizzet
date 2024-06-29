""" Defines the SQLAlchemy models for a User and a Quiz """

from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    """This class defines the user model."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Quiz(db.Model):
    """This class defines the quiz model."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    questions = db.Column(db.PickleType, nullable=False)
    created_by = db.Column(
            db.Integer, db.ForeignKey('user.id'), nullable=False
            )

""" User model module """

from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    """User model for storing user details"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hash and set the user's password"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check the hashed password"""
        return check_password_hash(self.password_hash, password)

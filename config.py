""" Configuration module """

import os


class Config:
    """Configuration class for a Flask application."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecret')
    SQLALCHEMY_DATABASE_URI = os.getenv(
            'DATABASE_URI', 'sqlite:///quiz_app.db'
            )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'myjwtsecret')

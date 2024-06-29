""" Initializes the Flask app. """
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from .auth import auth_bp
    from .quiz import quiz_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(quiz_bp)

    return app

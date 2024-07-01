""" Flask sever module """
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'

# Set the secret key for JWT
app.config['JWT_SECRET_KEY'] = 'yourSecretKey'

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Initialize JWT
jwt = JWTManager(app)

@app.route('/')
def home():
    """Home route for the application"""
    return 'Hello, Quiz App!'

if __name__ == '__main__':
    app.run(debug=True)


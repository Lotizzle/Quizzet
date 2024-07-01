""" Authentication module """
from flask import Blueprint, request, jsonify
from app import app, db
from models import User
from flask_jwt_extended import create_access_token


# Blueprint for authentication routes
auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['POST'])
def register():
    """User registration route"""
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    if User.query.filter_by(email=email).first():
        return jsonify({"msg": "User already exists"}), 400
    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "User created successfully"}), 201


@auth.route('/login', methods=['POST'])
def login():
    """User login route"""
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity={"email": user.email})
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Invalid credentials"}), 401


app.register_blueprint(auth, url_prefix='/auth')

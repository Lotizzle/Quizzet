""" Quiz Module """

from flask import Blueprint, request, jsonify
from app import app, db
from models import User
from flask_jwt_extended import jwt_required, get_jwt_identity
import requests


quiz = Blueprint('quiz', __name__)


@quiz.route('/questions', methods=['GET'])
@jwt_required()
def get_questions():
    """Fetch questions from the Open Trivia Database"""
    response = requests.get(
            'https://opentdb.com/api.php?amount=10&type=multiple'
            )
    questions = response.json()
    return jsonify(questions), 200


app.register_blueprint(quiz, url_prefix='/quiz')

from flask import Blueprint, jsonify

bp = Blueprint('home', __name__)

@bp.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to Production Grade Flask API!"
    }), 200

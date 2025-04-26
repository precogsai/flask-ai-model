from flask import Blueprint, jsonify
from app.services.health_service import check_health

bp = Blueprint('health', __name__, url_prefix='/health')

@bp.route('/', methods=['GET'])
def health_check():
    health_status = check_health()
    return jsonify(health_status), 200

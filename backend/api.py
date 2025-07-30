from flask import Blueprint, request, jsonify

api_bp = Blueprint('v1', __name__)


@api_bp.route('/get_web_picture', methods=['POST'])
def get_web_picture():
    data = request.get_json()
    return jsonify({"status": "success", "data": data})


@api_bp.route('/health', methods=['GET'])
def health_check():
    print(1)
    return jsonify({"status": "healthy", "service": "picture_processor"})

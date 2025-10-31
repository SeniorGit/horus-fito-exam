from flask import Blueprint, jsonify, request
from app.services.user_service import UserService
users_bp = Blueprint('users', __name__)

@users_bp.route('/')
def get_users():
    return jsonify({"message": "Get all users"})

@users_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "Data Json diperlukan"
        }), 400
    
    result, status_code = UserService.register(
        Nama=data.get('nama'),
        Email=data.get('email'),
        Username=data.get('username'),
        Password=data.get('password')
    )
    return jsonify(result), status_code


@users_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or not data.get('username') or not data.get('password'):
        return jsonify({
            "success": False,
            "message": "Data Json diperlukan"
        }), 400
    
    result, status_code = UserService.login(
        Username=data.get('username'),
        Password=data.get('password')
    )
    return jsonify(result), status_code
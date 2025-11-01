from flask import Blueprint, jsonify, request
from app.services.user_service import UserService
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import modelUsers

users_bp = Blueprint('users', __name__)
protected_bp = Blueprint('protected', __name__)

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

@protected_bp.route('/me', methods=['GET'])
@jwt_required
def get_user():
    user_id = get_jwt_identity()
    user = modelUsers.get_user_by_id(user_id)

    return jsonify({
        "success":True,
        "user":{
            "id": user["id"],
            "nama": user["nama"],
            "email": user["email"]
        }
    })
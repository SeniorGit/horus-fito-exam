from flask import Blueprint, jsonify, request
from app.services.user_service import UserService
from flask_jwt_extended import jwt_required, get_jwt_identity

users_bp = Blueprint('users', __name__)
protected_bp = Blueprint('protected', __name__)

# register router
@users_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    result, status_code = UserService.register(
        Nama=data.get('nama'),
        Email=data.get('email'), 
        Username=data.get('username'),
        Password=data.get('password')
    )
    return jsonify(result), status_code

# login router
@users_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    result, status_code = UserService.login(
        Username=data.get('username'),
        Password=data.get('password')
    )
    return jsonify(result), status_code

# get all data 
@users_bp.route('/getdata', methods=['GET'])
def all_users():
    result, status_code = UserService.get_all_users()
    return jsonify(result), status_code

# protected router (Dashboard)
@protected_bp.route('/me', methods=['GET'])
@jwt_required()
def get_user():
    user_id = get_jwt_identity()
    result, status_code = UserService.get_user_by_id(user_id)  
    return jsonify(result), status_code

# update router
@users_bp.route('/update/<int:user_id>', methods=['PUT'])
def update(user_id):
    data = request.get_json()
    result, status_code = UserService.update(
        id=user_id,
        username=data.get('username'),
        nama=data.get('nama'),
        email=data.get('email')
    )
    return jsonify(result), status_code

# detele user
@users_bp.route('/delete/<int:user_id>', methods=['DELETE'])
def delete(user_id):
    result, status_code = UserService.delete(id=user_id)
    return jsonify(result), status_code
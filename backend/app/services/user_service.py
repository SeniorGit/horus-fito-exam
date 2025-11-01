from app.utils.validator import validation
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import modelUsers
from flask_jwt_extended import create_access_token

class UserService:
    @staticmethod
    def register(Nama, Email, Username, Password):
        try:
            # Validasi input
            validator_error = validation._validate_input_reg(Nama, Email, Username, Password)
            if validator_error:
                return validator_error
            
            # is email
            if modelUsers.get_user_by_email(email=Email):
                return {"success": False, "message": "Email telah terdaftar"}, 409
            
            # is username
            if modelUsers.get_user_by_username(username=Username):
                return {"success": False, "message": "Username telah terdaftar"}, 409
            
            hash_password = generate_password_hash(Password)
            result = modelUsers.post_register(email=Email, username=Username, nama=Nama, password=hash_password)
            
            # get id
            user_id = result['id'] if result else None
            if not user_id:
                return {
                    "success": False,
                    "message": "Gagal membuat user di database"
                }, 500
            sendUser = modelUsers.get_user_by_id(id=user_id)
            if not sendUser:
                return {
                    "success": False,
                    "message": "User tidak ditemukan setelah registrasi"
                }, 500
            
            # send data to body
            return {
                "success": True,
                "message": f"Registrasi berhasil untuk {Username}",
                "data": {
                    "id": sendUser['id'],
                    "nama": sendUser['nama'],
                    "username": sendUser['username'],
                    "email": sendUser['email'],
                    "create_at": sendUser['create_at'].isoformat() if sendUser['create_at'] else None
                }
            }, 201
            
        except Exception as e:
            return {
                "success": False,
                "message": f"Terjadi kesalahan server: {str(e)}"
            }, 500

    @staticmethod
    def login(Username, Password):
        try:
            # Validasi input
            validator_error = validation._validate_input_log(Username, Password)
            if validator_error:
                return validator_error
            
            user = modelUsers.get_user_by_username(username=Username)

            # is username & is not password
            if not user:
                return {"success": False, "message": "Username atau password salah"}, 401
            
            if not check_password_hash(user['password'], Password):
                return {"success": False, "message": "Username atau password salah"}, 401
            
            access_token = create_access_token(
                identity=str(user['id']),
                additional_claims={
                    'username': user['username'],
                }
            )

            # send data to body
            return {
                "success": True,
                "message": f"Login berhasil untuk {Username}",
                "data": {
                    "access_token": access_token,
                    "token_type": "bearer",
                    "user":{
                        "id": user['id'],
                        "nama": user['nama'],
                        "username": user['username'],
                        "email": user['email'],
                        "create_at": user['create_at'].isoformat() if user['create_at'] else None
                    }
                    
                }
            }, 200
            
        except Exception as e:
            return {
                "success": False,
                "message": f"Terjadi kesalahan server Login: {str(e)}"
            }, 500
    
    @staticmethod
    def get_all_users():
        try:
            users = modelUsers.get_all_users()
            return {
                "success": True,
                "data": users,
            }, 200
        except Exception as e:
            return {
                "success": False,
                "message":  f"Terjadi kesalahan server Update: {str(e)}"
            }, 500
    
    @staticmethod
    def get_user_by_id(user_id):
        try:
            user = modelUsers.get_user_by_id(user_id)
            if not user:
                return {
                    "success": False,
                    "message": "User tidak ditemukan"
                }, 404
            return {
                "success": True,
                "data": user
            }, 200
        except Exception as e:
            return {
                "success": False, 
                "message":  f"Terjadi kesalahan server : {str(e)}"
            }, 500

    @staticmethod
    def update(id, username, email, nama):
        try:

            existing_user = modelUsers.get_user_by_id(id=id)
            if not existing_user:
                return {
                    "success": False,
                    "message": "User tidak dapat ditemukan"
                }, 404
            
            validator_error = validation._validate_input_update(nama=nama, username=username, email=email)
            if validator_error:
                return validator_error
            
            # is email
            existing_email_user = modelUsers.get_user_by_email(email=email)
            if existing_email_user and existing_email_user['id'] != id:
                return {"success": False, "message": "Email telah terdaftar oleh user lain"}, 409
            
            # is username
            existing_username_user = modelUsers.get_user_by_username(username=username)
            if existing_username_user and existing_username_user['id'] != id:
                return {"success": False, "message": "Username telah terdaftar oleh user lain"}, 409
            
            updated_user = modelUsers.update_user_data(id=id, username=username, email=email, nama=nama)
            if not updated_user:
                return {
                    "success": False,
                    "message": "Gagal mengupdate user di database"
                }, 500
            
            return{
                "success":True,
                "message": "data berhasil diupdate",
                "data": {
                    "username" : updated_user["username"],
                    "email" : updated_user["email"],
                    "nama" : updated_user["nama"]
                }
            },200
        
        except Exception as e:
            return{
                "success": False,
                "message": f"Terjadi kesalahan server Update: {str(e)}"   
            },500

    @staticmethod
    def delete(id):
        try:

            existing_user = modelUsers.get_user_by_id(id=id)
            if not existing_user:
                return {
                    "success": False,
                    "message": "User tidak dapat ditemukan"
                }, 404
            
            delete_user = modelUsers.delete_user(id=id)
            if not delete_user:
                return{
                    "success": False,
                    "message": "gagal menghapus user dari database"
                }, 500
            
            return{
                "success":True,
                "message": "data berhasil didelete",
            }, 200
        
        except Exception as e:
            return{
                "success": False,
                "message": f"Terjadi kesalahan server delete: {str(e)}"   
            },500

            
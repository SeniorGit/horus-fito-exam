from app.utils.validator import validation
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import modelUsers

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
                  
            # send data to body
            return {
                "success": True,
                "message": f"Login berhasil untuk {Username}",
                "data": {
                    "id": user['id'],
                    "nama": user['nama'],
                    "username": user['username'],
                    "email": user['email'],
                    "create_at": user['create_at'].isoformat() if user['create_at'] else None
                }
            }, 200
            
        except Exception as e:
            return {
                "success": False,
                "message": f"Terjadi kesalahan server: {str(e)}"
            }, 500
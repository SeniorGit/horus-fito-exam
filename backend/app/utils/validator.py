import re

class validation:
    @staticmethod
    def _validate_input_reg(nama, email, username, password):
        # cek jika data keselurahan tidak kosong 
        if not all([nama.strip(), email.strip(), username.strip(), password]):
            return {
                "success": False,
                "message": "semua field harus diisi"
            }, 400
        
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            return{
                "success": False,
                "message": "Format email tidak valid"
            }, 400
        
        if len(password) < 6:
            return{
                "success": False,
                "message": "Password minimal 6 karakter"
            }, 400
        
        if len(username)< 3:
            return{
                "success":False,
                "message": "Username minimal 3 karakter"
            }, 400
        return None
    
    @staticmethod
    def _validate_input_log(username, password):
        # cek jika data keselurahan tidak kosong         
        if len(password) == 0:
            return{
                "success": False,
                "message": "Username atau password tidak boleh kosong"
            },400
        
        if len(username)== 0:
            return{
                "success":False,
                "message": "Username atau password tidak boleh kosong"
            }, 400
        
        if len(password) < 6:
            return{
                "success": False,
                "message": "Password minimal 6 karakter"
            }, 400
        
        if len(username)< 3:
            return{
                "success":False,
                "message": "Username minimal 3 karakter"
            }, 400
        return None
        
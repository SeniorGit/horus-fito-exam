from app.extensions import get_db
import psycopg2.extras
class modelUsers:
    @staticmethod
    def get_user_by_id(id):
        db = get_db()
        cursor = db.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        try:
            cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
            return cursor.fetchone()
        finally:
            cursor.close()


    @staticmethod
    def get_user_by_email(email):
        db = get_db()
        cursor = db.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        try:
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            return cursor.fetchone()
        finally:
            cursor.close()

    @staticmethod
    def get_user_by_username(username):
        db = get_db()
        cursor = db.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        try:
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            return cursor.fetchone()
        finally:
            cursor.close()

    @staticmethod 
    def post_register(nama, email, username, password):
        db = get_db()
        cursor = db.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        try:
            cursor.execute("""
                INSERT INTO users (nama, email, username, password)
                VALUES (%s, %s, %s, %s)
                RETURNING id, nama, email, username, create_at
            """, (nama, email, username, password))
            result = cursor.fetchone()
            db.commit()
            return result
        except Exception as e:
            db.rollback() 
            raise e
        finally:
            cursor.close()
    
    @staticmethod
    def get_all_users():
        db = get_db()
        cursor = db.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        try:
            cursor.execute("SELECT id, username, email, nama FROM users ORDER BY id DESC")
            return cursor.fetchall()
        finally:
            cursor.close()

    @staticmethod
    def update_user_data(id, username, email, nama):
        db = get_db()
        cursor = db.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        try:
            cursor.execute("""
                           UPDATE users
                           SET username = %s, email = %s, nama = %s
                           WHERE id = %s
                           RETURNING id, username, email, nama, create_at
                           """,(username, email, nama, id))
            result = cursor.fetchone()
            db.commit()
            return result
        except Exception as e:
            db.rollback()  
            print(f"Error updating user: {e}")
            return None
        finally:
            cursor.close()

    @staticmethod
    def delete_user(id):
        db = get_db()
        cursor = db.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        try:
            cursor.execute("DELETE FROM users WHERE id = %s",(id,))
            return cursor.fetchone()
        finally:
            cursor.close()
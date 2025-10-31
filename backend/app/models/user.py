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
# from app.extensions import db

# class User(db.Model):
#     __tablename__ = 'users'
    
#     id = db.Column(db.Integer, primary_key=True)
#     nama = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(150), unique=True, nullable=False)
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     password = db.Column(db.String(255), nullable=False)
#     create_at = db.Column(db.DateTime, default=db.func.now())
    
#     def __repr__(self):
#         return f'<User {self.username}>'
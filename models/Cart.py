from flask_sqlalchemy import SQLAlchemy
from User import User

db = SQLAlchemy()

class Cart(db.Model):
    __tablename__ = 'carts'
    cart_id = db.Column(db.Integer, primary_key =True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    def __init__(self, user_id):
        self.user_id = user_id
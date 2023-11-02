from flask_sqlalchemy import SQLAlchemy
from Cart import Cart

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.cart_id'), nullable=False)
    #GO MAKE A CART

    #MAX KEEP SECURITY IN MIND JSON WEB TWOKEN ENCRYPTION

    def __init__(self, username, password, cart_id):
        self.username = username
        self.password = password
        self.cart_id = cart_id
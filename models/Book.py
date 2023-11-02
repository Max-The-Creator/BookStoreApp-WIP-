from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = 'books'
    book_id = db.Column(db.Integer, primary_key =True)
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    price = db.Column(db.Float(), nullable=False)

    def __init__(self, title, author, description, price):
        self.title = title
        self.author = author
        self.description = description
        self.price = price

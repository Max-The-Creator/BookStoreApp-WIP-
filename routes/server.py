from flask import Flask, jsonify, request
from models import db, User, Book, Cart

app = Flask(__name__)

#Make sure to set up config 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password:localhost:5432:axlehealthdb'

db.init_app(app)

#POST ROUTES
#This route creates a new user
@app.route('/users/', methods= ['GET'])
def createUser():
    data = request.get_json()
    new_user = User(username=data['username'], password=data['password'], cart_id=data['cart_id'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"messsage":"New user successfully created"}), 201

#GET ROUTES
#This method retrieves a list of all books
@app.route('/books/', methods=['GET'])
def getAllBooks():
    data = request.get_json()
    new_book = Book()
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"messsage":"Here is a list of all the books"}), 201


#PUT ROUTES

#DELETE ROUTES

if __name__ == "__main__":
    app.run(debug=True)
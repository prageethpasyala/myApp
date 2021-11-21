
from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy
from config import Config
import json
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__, instance_relative_config=False)
app.config.from_object(Config)

db = SQLAlchemy(app)

# class Movies(db.Model):
#     id = db.Column('id', db.Integer, primary_key=True)
#     name = db.Column(db.VARCHAR(length=255))
#     release_year = db.Column(db.Integer)

class book_db(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(length=255))
    release_date = db.Column(db.VARCHAR(length=255))
    isdn = db.Column(db.Integer)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/books")
def books():
    # RETRIEVE ALL MOVIES FROM TABLE Moviesß
    booklist = book_db.query.all()    # SELECT * FROM Movies

    html_response = "<ul>"
    for m in booklist:
        html_response += "<li>" + "<a href='/book/" + str(m.id) + "'>  " + str(m.id) + " - " + m.name + " - " + m.release_date +"</a> --- <a href='book/delete/"+str(m.id)+"'>DEL</a></li>"
    html_response += "</ul>"
    return html_response

# READ
@app.route("/book/<int:book_id>" , methods=['GET'])
def get_book(book_id):
    book = book_db.query.get(book_id)   # SELECT * FROM Movies WHERE id = movie_id
    return "<h1>" + book.name + " - " + book.release_date + " - " + str(book.isdn) + "</h1>" 

# CREATE    - POST
@app.route("/book/add", methods=['POST'])
def add_book():
    req_data = request.get_json()
    book = req_data['bookdetail'] 
    new_book = book_db(name=book["name"], release_date=book["release_date"],isdn=book["isdn"])
    # new_book = book_db(name="testmovie", release_date="mar2021" )
    db.session.add(new_book)
    db.session.commit()    
    return "Book was added successfully"

# UPDATE    - POST
@app.route("/book/update/<int:book_id>", methods=['POST'])
def update_book(book_id):
    book2 = book_db.query.get(book_id)   #from database book details

    req_data = request.get_json() #from curl command data request 
    book = req_data['bookdetail'] # curl data assigned to book variable
    book2.name=book["name"]
    book2.release_date = book["release_date"]
    book2.isdn = book["isdn"]
    db.session.commit()    
    return "Book was updated successfully"

# DELETE    - GET
@app.route("/book/delete/<int:book_id>", methods=['GET'])
def delete_book(book_id):
    book2 = book_db.query.get(book_id)   #from database book details

    db.session.delete(book2)
    db.session.commit()    
    return "Book was deleted successfully <a href='/books'>BACK</a>"
    





if __name__ == "__main__":
    app.run(host='127.0.0.1')




### new movie
# { "movie" : { "name" : "The Matrix", "release_date" : "1999"} }
### { "bookdetail": { "name": "The Matrix6", "release_date": "206", "isdn" : 5556 }}





# READ      - GET
# UPDATE    - PUT
# DELETE    - GET
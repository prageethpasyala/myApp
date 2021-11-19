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
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(length=255))
    release_date = (db.VARCHAR(length=255))
    isdn = db.Column(db.Integer)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/books")
def movies():
    # RETRIEVE ALL MOVIES FROM TABLE Moviesß
    booklist = book_db.query.all()    # SELECT * FROM Movies

    html_response = "<ul>"
    for m in booklist:
        html_response += "<li>" + "<a href='/book/" + str(m.id) + "'>" + m.name + "</a>" + "</li>"
    html_response += "</ul>"
    return html_response

# READ
@app.route("/book/<book_id>")
def get_movie(book_id):
    movie = book_db.query.get(book_id)   # SELECT * FROM Movies WHERE id = movie_id
    return "<h1>" + movie.name + " - " + str(movie.release_date) + "</h1>"

# CREATE    - POST
@app.route("/movie/add", methods=['POST'])
def add_movie():
    req_data = request.get_json()
    movie = req_data['movie']       # { name: "something", release_date: "something" }

    new_movie = Movies(name=movie["name"], release_year=movie["release_year"])
    db.session.add(new_movie)
    db.session.commit()
    
    return "Movie was added successfully"

if __name__ == "__main__":
    app.run(host='127.0.0.1')




### new movie
# { "movie" : { "name" : "The Matrix", "release_date" : "1999"} }






# READ      - GET
# UPDATE    - PUT
# DELETE    - GET
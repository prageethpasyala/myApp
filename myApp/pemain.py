from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy
from peconfig import Config
import json

app = Flask(__name__, instance_relative_config=False)
app.config.from_object(Config)

db = SQLAlchemy(app)

class Movies(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(length=255))
    release_year = db.Column(db.Integer)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/movies")
def movies():
    # RETRIEVE ALL MOVIES FROM TABLE Movies
    movies = Movies.query.all()    # SELECT * FROM Movies

    html_response = "<ul>"
    for m in movies:
        html_response += "<li>" + "<a href='/movie/" + str(m.id) + "'>" + m.name + "</a>" + "</li>"
    html_response += "</ul>"
    return html_response

# READ
@app.route("/movie/<movie_id>")
def get_movie(movie_id):
    movie = Movies.query.get(movie_id)   # SELECT * FROM Movies WHERE id = movie_id
    return "<h1>" + movie.name + " - " + str(movie.release_year) + "</h1>"

# CREATE    - POST
@app.route("/movie/add", methods=['POST'])
def add_movie():
    req_data = request.get_json()
    movie = req_data['movie']       # { name: "something", release_date: "something" }

    # new_movie = Movies(name=movie["name"], release_year=movie["release_year"])
    new_movie = Movies(name="test", release_year="12")
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
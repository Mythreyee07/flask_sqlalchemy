from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
import json


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@127.0.0.1/flask_project"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)

class Movie(db.Model):
    __tablename__ = 'movies'  
    id = db.Column(db.Integer, primary_key=True)  
    title = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(80), nullable=False)


    def json(self):
        return {'id': self.id, 'title': self.title,
                'year': self.year, 'genre': self.genre}   

    def get_all_movies():
             
             return [Movie.json(movie) for movie in Movie.query.all()]

    def get_movie(_id):
            
            return [Movie.json(Movie.query.filter_by(id=_id).first())]

    def add_movie(_title, _year, _genre):
            
            new_movie = Movie(title=_title, year=_year, genre=_genre)
            db.session.add(new_movie)  
            db.session.commit()      

    def update_movie(_id, _title, _year, _genre):
            
            movie_to_update = Movie.query.filter_by(id=_id).first()
            movie_to_update.title = _title
            movie_to_update.year = _year
            movie_to_update.genre = _genre
            db.session.commit()     

    def delete_movie(_id):
            
            Movie.query.filter_by(id=_id).delete()
            db.session.commit()                      


@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify({'Movies': Movie.get_all_movies()})

@app.route('/movies/<int:id>', methods=['GET'])
def get_movie_by_id(id):
    return_value = Movie.get_movie(id)
    return jsonify(return_value)   

# route to add new movie
@app.route('/movies', methods=['POST'])
def add_movie():
    request_data = request.get_json()  
    Movie.add_movie(request_data["title"], request_data["year"],
                    request_data["genre"])
    response = Response("Movie added", 201)
    return response 

# route to update movie with PUT method
@app.route('/movies/<int:id>', methods=['PUT'])
def update_movie(id):
    request_data = request.get_json()
    Movie.update_movie(id, request_data['title'], request_data['year'],                                      request_data['genre'])
    response = Response("Movie Updated", status=200 )
    return response  

@app.route('/movies/<int:id>', methods=['DELETE'])
def remove_movie(id):
    Movie.delete_movie(id)
    response = Response("Movie Deleted", status=200)
    return response          


if __name__ == "__main__":
    app.run(debug=True)




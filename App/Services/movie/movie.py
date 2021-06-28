from flask import  request, Response, jsonify
from App.Models.movie import Movie
from App import db


class Movies:
    def exception_handling(func):
            def inner_function(*args, **kwargs):
                    try:
                            return func(*args, **kwargs)
                            
                    except Exception as error:
                            return{"Status":400, "message":str(error)} 
            return inner_function                            

    def format(self):
        return {'id': self.id, 'title': self.title,
                'year': self.year, 'genre': self.genre}   
    @exception_handling
    def get_all_movies():
             return [Movies.format(movie) for movie in Movie.query.all()]

    @exception_handling
    def get_movie(_id):
            return [Movies.format(Movie.query.filter_by(id=_id).first())]

    @exception_handling
    def add_movie(_title, _year, _genre):
            new_movie = Movie(title=_title, year=_year, genre=_genre)
            db.session.add(new_movie)  
            db.session.commit() 
            return jsonify({  'message': 'successfully added movie', 'error':False})

    @exception_handling        
    def update_movie(_id, _title, _year, _genre):
            movie_to_update = Movie.query.filter_by(id=_id).first()
            movie_to_update.title = _title
            movie_to_update.year = _year
            movie_to_update.genre = _genre
            db.session.commit()   
            return jsonify({  'message': 'successfully updated movie', 'error':False})

    @exception_handling
    def delete_movie(_id):
            Movie.query.filter_by(id=_id).delete()
            db.session.commit()             
            return(Response("Movie Deleted", status=200))
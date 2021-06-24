from flask_json_schema import JsonValidationError
from flask import  request, Response, jsonify
from App import app
from App.Services.movie.movie import Movies
from App.Routes.validation.movie import schema, movie_schema



@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify({'Movies': Movies.get_all_movies()})

@app.route('/movies1', methods=['GET'])
def get_movie_by_id():
    id=request.args.get('id')
    return jsonify( Movies.get_movie(id))
      

# route to add new movie
@app.route('/movies', methods=['POST'])
@schema.validate(movie_schema)
def add_movie():
    request_data = request.get_json()  
    return(Movies.add_movie(request_data["title"], request_data["year"], request_data["genre"]))
    

# route to update movie with PUT method
@app.route('/movies', methods=['PUT'])
@schema.validate(movie_schema)
def update_movie():
    id=request.args.get('id')
    request_data = request.get_json()
    return(Movies.update_movie(id, request_data['title'], request_data['year'], request_data['genre']))
    
# route to del movie 
@app.route('/movies', methods=['DELETE'])
def remove_movie():
    id=request.args.get('id')
    return(Movies.delete_movie(id))
             
@app.errorhandler(JsonValidationError)
def validation_error(e):
    return jsonify({ 'error': e.message, 'errors': [validation_error.message for validation_error  in e.errors]})


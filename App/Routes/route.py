from flask import  request, Response, jsonify
from App import app
from App.Services.movie.movie import Movies


@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify({'Movies': Movies.get_all_movies()})

@app.route('/movies1', methods=['GET'])
def get_movie_by_id():
    id=request.args.get('id')
    return_value = Movies.get_movie(id)
    return jsonify(return_value)   

# route to add new movie
@app.route('/movies', methods=['POST'])
def add_movie():
    request_data = request.get_json()  
    return(Movies.add_movie(request_data["title"], request_data["year"], request_data["genre"]))
    

# route to update movie with PUT method
@app.route('/movies', methods=['PUT'])
def update_movie():
    id=request.args.get('id')
    request_data = request.get_json()
    return(Movies.update_movie(id, request_data['title'], request_data['year'], request_data['genre']))
     

@app.route('/movies', methods=['DELETE'])
def remove_movie():
    id=request.args.get('id')
    return(Movies.delete_movie(id))
             


from App import db

class Movie(db.Model):
    __tablename__ = 'movies'  
    id = db.Column(db.Integer, primary_key=True)  
    title = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(80), nullable=False)

    
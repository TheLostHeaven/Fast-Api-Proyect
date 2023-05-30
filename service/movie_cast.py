from models.movie_cast import Movie_cast as Movie_castModel
# from schemas.movie_cast import Movie_cast

class MovieCast():
    def __init__(self, db):
        self.db = db 

    def get_movie_cast(self):
        result = self.db.query(Movie_castModel).all()
        return result
    
    def create_movie_cast(self, movie_cast:Movie_castModel):
        new_movie_cast = Movie_castModel(
            
            mov_id = movie_cast.mov_id,
            role = movie_cast.role.upper()      
        )
        self.db.add(new_movie_cast)
        self.db.commit()
        return 
    
    def get_for_id(self, data:Movie_castModel):
        result = self.db.query(Movie_castModel).filter(Movie_castModel.id == id).first()
        return result 
    
    def update_movie_cast(self, data:Movie_castModel):
        movie_cast = self.db.query(Movie_castModel).filter(Movie_castModel.id == id).first()
        movie_cast.mov_id = data.mov_id
        movie_cast.role = data.role
        self.db.commit()
        return
    
    def delete_movie_cast(self, id:int):
        self.db.query(Movie_castModel).filter(Movie_castModel.id == id).delete()
        self.db.commit()
        return
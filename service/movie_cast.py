from models.movie_cast import Movie_cast as Movie_castModel
from schemas.movie_cast import Movie_cast 

class MovieCast():
    def __init__(self, db):
        self.db = db 

    def get_movie_cast(self):
        result = self.db.query(Movie_castModel).all()
        return result
    
    def create_movie_cast(self, movie_cast:Movie_castModel):
        new_movie_cast = Movie_castModel(
            actor_id = movie_cast.actor_id,
            movie_id = movie_cast.movie_id,
            role = movie_cast.role.upper()      
        )
        self.db.add(new_movie_cast)
        self.db.commit()
        return 
    
    

    def get_for_id(self, id:int):     
        result = self.db.query(Movie_castModel).filter(Movie_castModel.id==id).first()    
        return result
    
    

    def update_movie_cast(self,data:Movie_castModel):        
        cast = self.db.query(Movie_castModel).filter(Movie_castModel.id == data.id).first()       
        cast.actor_id = data.actor_id   
        cast.movie_id = data.movie_id      
        cast.role = data.role     
        self.db.commit()            
        return 
    

    def delete_movie_cast(self, id:int):
        self.db.query(Movie_castModel).filter(Movie_castModel.id == id).delete()
        self.db.commit()
        return
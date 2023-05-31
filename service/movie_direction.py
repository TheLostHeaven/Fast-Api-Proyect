from models.movie_direction import MovieDirection as MovieDirectionModel 
from schemas.movie_direction import MovieDirection

class MovieDirectionService():
    def __init__(self, db):
        self.db = db
    
    def get_moviedirection(self):
        result = self.db.query(MovieDirectionModel).all()
        return result
    
    def create_moviedirection(self,moviedirection:MovieDirectionModel):
         new_movie_direction = MovieDirectionModel(
             dir_id = moviedirection.dir_id,
             mov_id = moviedirection.mov_id.upper()
         )
         self.db.add(new_movie_direction)
         self.db.commit()
         return

    
    def get_for_id(self,id:int):
         result = self.db.query(MovieDirectionModel).filter(MovieDirectionModel.id==id).first()
         return result
    
    def update_moviedirection(self,data:MovieDirection):
         moviedirection = self.db.query(MovieDirectionModel).filter(MovieDirectionModel.id==data.id).first()
         moviedirection.dir_id=data.dir_id
         moviedirection.mov_id=data.mov_id
         self.db.commit()
         return
    
    def delete_moviedirection(self, id:int):
         self.db.query(MovieDirectionModel).filter(MovieDirectionModel.id==id).delete()
         self.db.commit()
         return
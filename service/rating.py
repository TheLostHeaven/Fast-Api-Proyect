from models.rating import Rating as RatingModel
from schemas.rating import Rating

class RatingService():
    def __init__(self, db) :
        self.db = db

    def get_rating(self):
        result = self.db.query(RatingModel).all()
        return result
    
    def create_rating(self,rating:RatingModel):
        new_rating = RatingModel(
            mov_id = rating.movie_id,
            rev_id = rating.rev_id,
            rev_star = rating.rev_stars,
            num_o_ratings = rating.num_o_ratings.upper()
        )
        self.db.add(new_rating)
        self.db.commit()
        return
    
    def get_for_id(self,id:int):
        result = self.db.query(RatingModel).filter(RatingModel.id == id).first()
        return result
    
    def update_rating(self,data:Rating):
        rating = self.db.query(RatingModel).filter(RatingModel.id == data.id).first()
        rating.mov_id=data.movie_id
        rating.rev_id=data.rev_id
        rating.rev_star=data.rev_stars
        rating.num_o_ratings=data.num_o_rating
        self.db.commit()
        return
    
    def delete_rating(self,id:int):
        self.db.query(RatingModel).filter(RatingModel.id == id).delete()
        self.db.commit()
        return
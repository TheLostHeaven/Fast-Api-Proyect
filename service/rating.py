from models.rating import rating as ratingModel
from schemas.rating import rating

class ratingService():
    def init(self, db) :
        self.db = db

    def get_rating(self):
        result = self.db.query(ratingModel).all()
        return result
    
    def create_rating(self,rating:ratingModel):
        new_rating = ratingModel(
            mov_id = rating.movie_id,
            rev_id = rating.rev_id,
            rev_star = rating.rev_stars,
            num_o_ratings = rating.num_o_ratings.upper()
        )
        self.db.add(new_rating)
        self.db.commit()
        return
    
    def get_for_id(self,id:int):
        result = self.db.query(ratingModel).filter(ratingModel.id == id).first()
        return result
    
    def update_rating(self,data:rating):
        rating = self.db.query(ratingModel).filter(ratingModel.id == data.id).first()
        rating.mov_id=data.movie_id
        rating.rev_id=data.rev_id
        rating.rev_star=data.rev_stars
        rating.num_o_ratings=data.num_o_rating
        self.db.commit()
        return
    
    def delete_rating(self,id:int):
        self.db.query(ratingModel).filter(ratingModel.id == id).delete()
        self.db.commit()
        return
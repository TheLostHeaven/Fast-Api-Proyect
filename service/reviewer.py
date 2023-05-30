from models.reviewers import Reviewers as ReviewersModel
from schemas.reviewers import Reviewers

class ReviewerService():
    def __init__(self, db):
        self:db = db
        
    def get_reviewer_hello(self):
        result = self.db.query(ReviewerService).all()
        return result
    
    def create_reviewer(self,reviewer:ReviewersModel):
        new_reviewer = ReviewersModel(
            rev_name = reviewer.rev_name.upper()
        )
        self.db.add(new_reviewer)
        self.db.commit()
        return
    
    def get_for_id(self,id:int):
        result = self.db.query(ReviewersModel).filter(ReviewersModel.id == id).first()
        return result
    
    def update_reviewer(self,data:Reviewers):
        reviewer = self.db.query(ReviewersModel).filter(ReviewersModel.id == data.id).first()
        reviewer.rev_name = data.rev_name
        self.db.commit()
        return
    
    def delete_reviewer(self,id:int):
        self.db.query(ReviewersModel).filter(ReviewersModel.id == id).delete()
        self.db.commit()
        return
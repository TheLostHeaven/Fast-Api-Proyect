from models.reviewers import Reviewers as ReviewersModel
from schemas.reviewers import Reviewers as ReviewerSchemas
class ReviewerService():
    def __init__(self, db) -> None:
        self.db = db
        
    def get_reviewer(self):
        result = self.db.query(ReviewersModel).all()
        return result
    
    def create_reviewer(self,reviewer:ReviewersModel):
        new_reviewer = ReviewersModel(
            rev_name = reviewer.rev_name.upper()
        )
        self.db.add(new_reviewer)
        self.db.commit()
        return
    
    
    def get_for_id(self, id:int):  
        result = self.db.query(ReviewersModel).filter(ReviewersModel.id==id).first() 
        return result
   
   
    def update_reviewer(self,data):
        reviewer = self.db.query(ReviewersModel).filter(ReviewersModel.id == data.id).first()
        reviewer.rev_name = data.rev_name
        self.db.commit() 
        return 
    
    def delete_reviewer(self,id:int):
        self.db.query(ReviewersModel).filter(ReviewersModel.id == id).delete()
        self.db.commit()
        return
from pydantic import BaseModel, Field
from typing import Optional

class rating(BaseModel):
    id: Optional[int] = None
    movie_id: Optional[int] = None
    rev_id: Optional[int] = None
    rev_stars: int = Field(max_length=10,min_length=1)
    num_o_rating: int = Field(max_length=100,min_length=1)

    class config:
        shema_extra = {
            "example":{
                "id" : 1,
                "movie_id" : 2,
                "rev_id" : 3,
                "rev_stars" : 8,
                "num_o_rating" : 90 
            }
        }

    
    
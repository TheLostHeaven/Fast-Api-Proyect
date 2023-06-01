from pydantic import BaseModel, Field
from typing import Optional

class Rating(BaseModel):
    id: Optional[int] = None
    movie_id: Optional[int] = None
    rev_id: Optional[int] = None
    rev_stars: int = Field(ge=1, le=10)
    num_o_rating: int = Field(ge=1, le=100)

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

    
    
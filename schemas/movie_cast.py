from pydantic import BaseModel, Field 
from typing import Optional 
 
class Movie_cast(BaseModel): 
   id: Optional[int] = None   
   act_id : int = Field (gen= 1, description="identificacion del actor") 
   mov_id : int = Field (gen= 1, description="identificacion de la pelicula") 
   role : str = Field (max_length=15, min_length=3, description="papel del usuario involucrado") 
 
   class config: 
      schema_extra = { 
                "example": { 
                    "id": 1, 
                    "act_id": 2, 
                    "mov_id": 3, 
                    "role": "director" 
                } 
      }
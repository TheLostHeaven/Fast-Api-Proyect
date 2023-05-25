from pydantic import BaseModel, Field
<<<<<<< HEAD
from typing import Opcional 

class Genres(BaseModel):
    id : Opcional[int] = None
    gen_title : str = Field(max_length=15, min_length=3, description="Genero de la pelicula")
=======
from typing import Optional

class Genres(BaseModel):
    id : Optional[int] = None
    gen_title : str = Field(max_length=15,min_length=3,description="genero de la pelicula")
>>>>>>> schemas/reviewers

    class Config:
        schema_extra = {
            "example":{
<<<<<<< HEAD
                "id":1,
                "gen_title":"Action"
=======
            "id":1,
            "gen_title":"Action"
>>>>>>> schemas/reviewers
            }
        }
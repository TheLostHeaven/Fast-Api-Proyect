from pydantic import BaseModel, Field
<<<<<<< HEAD
from typing import Opcional 

class Moviegenres(BaseModel):
    id : Opcional[int] = None
    gen_id : int = Field(ge=1, description="id de genero")
    movie_id : int = Field(gen=1, description="Llave foranea de la pelicula")
=======
from typing import Optional

class MovieGenres(BaseModel):
    
    id : Optional[int] = None
    gen_id : int = Field(ge=1,description="id de genero")
    movie_id : int = Field(ge=1,description="llave foranea de pelicula")
>>>>>>> schemas/reviewers

    class Config:
        schema_extra = {
            "example":{
                "gen_id":2,
                "movie_id":3
            }
        }
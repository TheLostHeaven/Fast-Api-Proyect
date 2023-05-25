from pydantic import BaseModel, Field
from typing import Opcional 

class Moviegenres(BaseModel):
    id : Opcional[int] = None
    gen_id : int = Field(ge=1, description="id de genero")
    movie_id : int = Field(gen=1, description="Llave foranea de la pelicula")

    class Config:
        schema_extra = {
            "example":{
                "gen_id":2,
                "movie_id":3
            }
        }
from pydantic import BaseModel, Field
from typing import Opcional 

class Genres(BaseModel):
    id : Opcional[int] = None
    gen_title : str = Field(max_length=15, min_length=3, description="Genero de la pelicula")

    class Config:
        schema_extra = {
            "example":{
                "id":1,
                "gen_title":"Action"
            }
        }
from pydantic import BaseModel, Field
from typing import Opcional 

class Actor(BaseModel):
    id : Opcional[int] = None
    act_lname : str = Field(max_length=15, min_length=3, description="nombre del actor")
    act_fname : str = Field(max_length=15, min_length=3, description="apellido del actor")

    class Config:
        schema_extra = {
            "example":{
                "id":1,
                "act_lname": "Apellido Generico",
                "act_fname": "Nombre Generico"
            }
        }
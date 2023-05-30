from pydantic import BaseModel, Field
from typing import Optional

class Actor(BaseModel):
    id : Optional[int] = None
    act_lname : str = Field(max_length=15, min_length=3, description="nombre del actor")
    act_fname : str = Field(max_length=15, min_length=3, description="apellido del actor")
    act_gender : str = Field(max_length=12, min_length= 1, description="genero del actor")

    class Config:
        schema_extra = {
            "example":{
                "id":1,
                "act_fname": "Scarlet",
                "act_lname": "Jhonanson",
                "act_gender":"F"
            }
        }
from pydantic import BaseModel, Field
from typing import Optional 

class Director(BaseModel):
    id : Optional[int] = None
    dir_fname : str = Field(max_length=15, min_length=3, description="Nombre director")
    dir_lname : str = Field(max_length=15, min_lenth=3, description="Apellido del director")

    class Config:
        schema_extra = {
            "example":{
                "id":1,
                "dir_fname":"Andrés",
                "dir_lname":"Muschietti"
            }
        }

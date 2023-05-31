from pydantic import BaseModel, Field
from typing import Optional

class MovieDirection(BaseModel):
    id: Optional[int] = None
    dir_id: int = Field(ge=1)
    mov_id: int = Field(ge=1)

    class Config:
        schema_extra = {
            "example":{
                "id":1,
                "dir_id":2,
                "mov_id":3
            }
        }
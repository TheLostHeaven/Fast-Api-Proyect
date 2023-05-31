from pydantic import BaseModel, Field
from typing import Optional

class Reviewers(BaseModel):
    id : Optional[int] = None
    rev_name : str = Field(max_length=30, min_length=3,description="name reviewer")

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "rev_name": "cualquiera"
                }
                }


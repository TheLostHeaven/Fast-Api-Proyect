from sqlalchemy import Column, Integer, ForeignKey
from config.database import Base
from sqlalchemy.orm import relationship

class movie_direction(Base):

    __tablename = "movie_direction"
    dir_id = Column(Integer, ForeignKey ("dir.id") )
    mov_id = Column(Integer, ForeignKey("mov.id"))

  
    
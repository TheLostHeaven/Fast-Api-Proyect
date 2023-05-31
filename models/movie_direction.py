from sqlalchemy import Column, Integer, ForeignKey

from config.database import Base
from sqlalchemy.orm import relationship

class MovieDirection(Base):

    __tablename__ ="moviedirection"


    id = Column(Integer, primary_key=True)
    dir_id = Column(Integer,ForeignKey("director.id"))
    mov_id = Column(Integer, ForeignKey("movie.id"))

    director=relationship("Director",back_populates="moviedirection")
    movie=relationship("Movie",back_populates="moviedirection")
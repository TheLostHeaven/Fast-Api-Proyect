from sqlalchemy import Column, Integer, String, ForeignKey
from config.database import Base
from sqlalchemy.orm import relationship

class Movie_cast(Base):

    __tablename__ ="movie_cast"
    act_id = Column(Integer, ForeignKey("actor.id"))
    mov_id = Column(Integer, ForeignKey("movie.id"))
    role = Column(String) 

    movies = relationship("Movie", back_populates="movies_cast")
    actors = relationship("Actor", back_populates="movie_cast")
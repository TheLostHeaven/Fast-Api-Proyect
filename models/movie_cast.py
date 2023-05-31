from sqlalchemy import Column, Integer, String, ForeignKey
from config.database import Base
from sqlalchemy.orm import relationship

class Movie_cast(Base):

    __tablename__ ="movie_cast"
    
    id = Column(Integer, primary_key = True, index=True)
    actor_id= Column(Integer, ForeignKey("actor.id"))
    movie_id = Column(Integer,ForeignKey("movie.id"))
    role = Column(String)

    actor = relationship("Actor", back_populates="movie_cast")
    movie = relationship("Movie", back_populates="movie_cast")        
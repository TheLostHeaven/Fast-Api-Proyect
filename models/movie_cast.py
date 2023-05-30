from sqlalchemy import Column, Integer, String, ForeignKey
from config.database import Base

from models.actor import Actor

class Movie_cast(Base):

    __tablename__ ="movie_cast"
    
    id = Column(Integer, primary_key = True, index=True)
    actor_id = Column(Integer, ForeignKey("actor.id"))
    movie_id = Column(Integer,ForeignKey("movie.id"))
    role = Column(String)

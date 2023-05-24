from sqlalchemy import Column, Integer, String, ForeignKey

from config.database import Base


class movie_cast(Base):

    __tablename__ ="movie_cast"
    act_id = Column(Integer, ForeignKey("actor.id"))
    mov_id = Column(Integer, ForeignKey("movie.id"))
    role = Column(String) 




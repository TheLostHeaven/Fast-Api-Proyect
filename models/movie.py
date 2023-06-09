from sqlalchemy import Column,Integer, String, Float
from sqlalchemy.orm import relationship
from config.database import Base


class Movie(Base):

    __tablename__ = "movie"

    id = Column(Integer,primary_key = True)
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    time = Column(Float)
    date_release = Column(String)
    release_contry = Column(String)

    movie_cast = relationship("Movie_cast", foreign_keys="Movie_cast.movie_id", back_populates="movie")






    
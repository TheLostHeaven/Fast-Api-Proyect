from sqlalchemy import Column, ForeignKey, Integer

from config.database import Base


class rating(Base):
    __tablename__ = "rating"

    id = Column(Integer, primary_Key=True)
    movie_id = Column(Integer, ForeignKey("movie.id"))
    rev_id = Column(Integer, ForeignKey("reviewers.id"))
    rev_stars = Column(Integer)
    num_o_ratings = Column(Integer)

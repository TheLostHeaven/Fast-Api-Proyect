from sqlalchemy import column, ForeignKey, Integer

from config.database import Base


class rating(Base):
    __tablename__ = "rating"

    id = column(Integer, primary_Key=True)
    movie_id = column(Integer, ForeignKey("movie.id"))
    rev_id = column(Integer, ForeignKey("reviewers.id"))
    rev_stars = column(Integer)
    num_o_ratings = column(Integer)

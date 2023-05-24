from sqlalchemy import column, Integer, String

from config.database import Base

class Genres(Base):

    __tablename__ ="genres"

    id= column(Integer, primary_key=True)
    gen_title = column(String)
from sqlalchemy import column, Integer, String

from config.database import Base

class Reviewers(Base):

    __tablename__ ='reviewers'

    rev_id = column(Integer,primary_key=True)
    rev_name = column(String)

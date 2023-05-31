from sqlalchemy import Column, Integer, String

from config.database import Base

class Reviewers(Base):

    __tablename__ ='reviewers'

    rev_id = Column(Integer,primary_key=True)
    rev_name = Column(String)

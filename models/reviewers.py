from sqlalchemy import Column, Integer, String

from config.database import Base

class Reviewers(Base):

    __tablename__ ='reviewers'

    id = Column(Integer, primary_key = True, index = True)
    rev_name = Column(String)


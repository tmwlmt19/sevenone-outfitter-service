from sqlalchemy import Column,Integer,String,ForeignKey
from app.db.base import Base

class Client(Base):

    __tablename__ = "client"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)

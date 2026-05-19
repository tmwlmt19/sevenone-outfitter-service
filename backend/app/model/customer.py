from sqlalchemy import Column,Integer,String,ForeignKey
from app.db.base import Base

class Customer(Base):

    __tablename__ = "customer"

    id = Column(Integer, primary_key=True)

    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone = Column(String)
from sqlalchemy import Column,Integer,String,ForeignKey,Numeric
from app.db.base import Base

class Inventory(Base):

    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True)

    clientId = Column(
        Integer,
        ForeignKey("client.id")
    )

    type = Column(String)
    subtype = Column(String)
    cost = Column(Numeric(10,2))
    name = Column(String)
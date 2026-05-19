from sqlalchemy import Column,Integer,String,ForeignKey,Date,Numeric
from app.db.base import Base

class Booking(Base):

    __tablename__ = "booking"

    id = Column(Integer, primary_key=True)

    clientId = Column(
        Integer,
        ForeignKey("client.id")
    )

    customerId = Column(
        Integer,
        ForeignKey("customer.id")
    )

    inventoryId = Column(
        Integer,
        ForeignKey("inventory.id")
    )

    startDate = Column(Date)
    endDate = Column(Date)
    cost = Column(Numeric(10,2))
    paid = Column(Numeric(10,2))
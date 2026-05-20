from sqlalchemy import Column,Integer,String,ForeignKey,Numeric
from app.db.base import Base

ZERO_AVAIL = "0" * 53

class Inventory(Base):

    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True)
    clientId = Column(
        Integer,
        ForeignKey("client.id"),
        nullable=False
    )

    iType = Column(String(3), nullable=False)
    iSubtype = Column(String(3))

    name = Column(String)
    cost = Column(Numeric(10,2), nullable=False)
    costUnit = Column(String(2), nullable=False)

    mondayAvail = Column(
        String(53),
        nullable=False,
        default=ZERO_AVAIL
    )
    tuesdayAvail = Column(
        String(53),
        nullable=False,
        default=ZERO_AVAIL
    )
    wednesdayAvail = Column(
        String(53),
        nullable=False,
        default=ZERO_AVAIL
    )
    thursdayAvail = Column(
        String(53),
        nullable=False,
        default=ZERO_AVAIL
    )
    fridayAvail = Column(
        String(53),
        nullable=False,
        default=ZERO_AVAIL
    )
    saturdayAvail = Column(
        String(53),
        nullable=False,
        default=ZERO_AVAIL
    )
    sundayAvail = Column(
        String(53),
        nullable=False,
        default=ZERO_AVAIL
    )

    capacity = Column(Integer)
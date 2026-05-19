from pydantic import BaseModel
from datetime import date

class BookingCreate(BaseModel):

    clientId: int
    customerId: int
    inventoryId: int
    startDate: date
    endDate: date
    cost: float
    paid: float

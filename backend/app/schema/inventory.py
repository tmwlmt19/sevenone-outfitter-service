from pydantic import BaseModel, ConfigDict
from typing import Optional
from decimal import Decimal

class InventoryCreate(BaseModel):

    clientId: int
    iType: str
    iSubtype: str
    name: str
    cost: float
    costUnit: str
    capacity: int


class InventoryFilter(BaseModel):
    id: Optional[int] = None
    clientId: Optional[int] = None
    iType: Optional[str] = None
    iSubtype: Optional[str] = None
    capacity: Optional[int] = None


class InventoryResponse(BaseModel):
    id: int
    clientId: int
    iType: str
    iSubtype: Optional[str]

    name: Optional[str]
    cost: Decimal
    costUnit: str

    mondayAvail: str
    tuesdayAvail: str
    wednesdayAvail: str
    thursdayAvail: str
    fridayAvail: str
    saturdayAvail: str
    sundayAvail: str

    capacity: Optional[int]

    model_config = ConfigDict(from_attributes=True)
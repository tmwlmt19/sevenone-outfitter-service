from pydantic import BaseModel

class InventoryCreate(BaseModel):

    clientId: int
    type: str
    subtype: str
    cost: float
    name: str
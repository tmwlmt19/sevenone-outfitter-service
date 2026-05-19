from pydantic import BaseModel

class CustomerCreate(BaseModel):

    first_name: str
    last_name: str
    email: str
    phone: str
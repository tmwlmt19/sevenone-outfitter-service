from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schema.customerCreate import CustomerCreate
from app.services.outfitterService import create_customer

router = APIRouter()

@router.post("/customers")
def create(data: CustomerCreate, db: Session = Depends(get_db)):
    return create_customer(data, db)
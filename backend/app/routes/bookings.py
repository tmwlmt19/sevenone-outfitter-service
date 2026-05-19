from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schema.bookingCreate import BookingCreate
from app.services.outfitterService import create_booking

router = APIRouter()

@router.post("/bookings")
def create(data: BookingCreate, db: Session = Depends(get_db)):
    return create_booking(data, db)
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schema.clientCreate import ClientCreate
from app.services.outfitterService import create_client

router = APIRouter()

@router.post("/clients")
def create(data: ClientCreate, db: Session = Depends(get_db)):
    return create_client(data, db)
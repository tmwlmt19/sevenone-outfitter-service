from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schema.inventoryCreate import InventoryCreate
from app.services.outfitterService import create_inventory

router = APIRouter()

@router.post("/inventory")
def create(data: InventoryCreate, db: Session = Depends(get_db)):
    return create_inventory(data, db)
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schema.inventory import InventoryCreate, InventoryFilter, InventoryResponse
from app.services.outfitterService import create_inventory, read_inventory
from typing import List

router = APIRouter(prefix="/inventory")

@router.post("/new")
def create(data: InventoryCreate, db: Session = Depends(get_db)):
    return create_inventory(data, db)

@router.get("/",response_model=List[InventoryResponse])
def read(
    filters: InventoryFilter = Depends(),
    db: Session = Depends(get_db)
):
    return read_inventory(db, filters)
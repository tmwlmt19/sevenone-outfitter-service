from app.model.inventory import Inventory

def create(data, db):

        inventory = Inventory(**data.model_dump(exclude_unset=True))

        db.add(inventory)
        db.commit()

        return inventory

def get(
          db: Session,
          filters: InventoryFilter
          ):
    query = db.query(Inventory)

    if filters.id is not None:
        query = query.filter(
            Inventory.id == filters.id
        )

    if filters.clientId is not None:
        query = query.filter(
            Inventory.clientId == filters.clientId
        )

    if filters.iType is not None:
        query = query.filter(
            Inventory.iType == filters.iType
        )

    if filters.iSubtype is not None:
        query = query.filter(
            Inventory.iSubtype == filters.iSubtype
        )

    if filters.capacity is not None:
        query = query.filter(
            Inventory.capacity == filters.capacity
        )

    return query.all()
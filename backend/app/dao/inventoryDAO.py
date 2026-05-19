from app.model.inventory import Inventory

def create(data, db):

        inventory = Inventory(**data.model_dump())

        db.add(inventory)
        db.commit()

        return inventory
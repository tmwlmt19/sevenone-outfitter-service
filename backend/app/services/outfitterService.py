from app.dao import customerDAO, clientDAO, bookingDAO, inventoryDAO

def create_customer(data, db):

    customer = customerDAO.create(data, db)

    return customer

def create_client(data, db):

    client = clientDAO.create(data, db)

    return client

def create_booking(data, db):

    booking = bookingDAO.create(data, db)

    return booking

def create_inventory(data, db):

    inventory = inventoryDAO.create(data, db)

    return inventory

def read_inventory(db, filters):
    
    inventoryList = inventoryDAO.get(db, filters)

    return inventoryList

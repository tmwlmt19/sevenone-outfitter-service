from app.model.client import Client

def create(data, db):

        client = Client(**data.model_dump())

        db.add(client)
        db.commit()

        return client

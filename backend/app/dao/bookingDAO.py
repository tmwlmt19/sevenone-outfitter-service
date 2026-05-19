from app.model.booking import Booking

def create(data, db):

        booking = Booking(**data.model_dump())

        db.add(booking)
        db.commit()

        return booking
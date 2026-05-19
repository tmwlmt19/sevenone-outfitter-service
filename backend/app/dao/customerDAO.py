from app.model.customer import Customer

def create(data, db):

        customer = Customer(**data.model_dump())

        db.add(customer)
        db.commit()

        return customer

# class CustomerDAO:

#     @staticmethod
#     def create(data, db):
#         customer = Customer(
#             first_name=data.first_name,
#             last_name=data.last_name,
#             email=data.email
#         )

#         db.add(customer)
#         db.commit()
#         db.refresh(customer)

#         return customer
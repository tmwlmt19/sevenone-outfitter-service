from fastapi import FastAPI
from app.routes import clients, customers, bookings, inventory

app = FastAPI()

app.include_router(customers.router)
app.include_router(clients.router)
app.include_router(bookings.router)
app.include_router(inventory.router)


@app.get("/")
def root():
    return {"status": "ok"}
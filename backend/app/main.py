from fastapi import FastAPI
from app.routes import users, parking_reports, availability

app = FastAPI()

app.include_router(users.router)
app.include_router(parking_reports.router)
app.include_router(availability.router)
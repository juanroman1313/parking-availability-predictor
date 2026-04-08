from fastapi import FastAPI
from app.routes import users, parking_reports

app = FastAPI()

app.include_router(users.router)
app.include_router(parking_reports.router)
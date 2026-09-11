from fastapi import FastAPI
from routes.employees import router as employees_router

app = FastAPI()

@app.get('/')
def home():
    return "Welcome to Company Management System" # Will replace with status in future

app.include_router(             # Have to include every router like this
    employees_router, 
    prefix="/employees",
    tags=["Employees"]
)
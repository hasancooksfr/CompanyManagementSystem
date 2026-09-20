from fastapi import FastAPI

from routes.employees import router as employees_router
from routes.departments import router as departments_router
from routes.payrolls import router as payrolls_router
from routes.attendance import router as attendance_router

app = FastAPI()

@app.get('/')
def home():
    return "Welcome to Company Management System" # Will replace with status in future

app.include_router(             # Have to include every router like this
    employees_router, 
    prefix="/employees",
    tags=["Employees"]
)

app.include_router(
    departments_router,
    prefix="/departments",
    tags=["Departments"]
)

app.include_router(
    payrolls_router,
    prefix="/payroll",
    tags=["Payroll"]
)

app.include_router(
    attendance_router,
    prefix="/attendance",
    tags=["Attendance"]
)
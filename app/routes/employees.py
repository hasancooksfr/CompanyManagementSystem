from fastapi import APIRouter, HTTPException

# Services
from services.employees import create_employee

# Schemas
from schemas.employees import EmployeeCreate

router = APIRouter()

@router.get('/')
def employee_home():
    return "Employee Home" # Will replace with getting all employees

@router.post('/', status_code=201)
def employee_create(employee: EmployeeCreate):
    employee = create_employee(employee)

    return {
        "success": employee,
        "message": "Employee created successfully!"
    }
from fastapi import APIRouter, HTTPException

# Services
from services.employees import create_employee
from services.employees import get_all_employees

# Schemas
from schemas.employees import EmployeeCreate

router = APIRouter()

@router.get('/')
def get_employees():
    data = get_all_employees()

    return {
        "success": True,
        "message": "Fetched all employees",
        "data": data
    }


@router.post('/', status_code=201)
def employee_create(employee: EmployeeCreate):
    employee = create_employee(employee)

    return {
        "success": employee,
        "message": "Employee created successfully!"
    }
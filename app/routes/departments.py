from fastapi import APIRouter, HTTPException

# Services
from services.departments import create_department
from services.departments import get_all_departments
from services.departments import get_department_data

# Schemas
from schemas.departments import DepartmentCreate

router = APIRouter()

@router.get('/')
def home():
    data = get_all_departments()

    return {
        "success": True,
        "message": "Fetched all departments",
        "data": data
    }

@router.post('/')
def department_create(department: DepartmentCreate):
    create_department(department)

    return {
        "success": True,
        "message": "Department created successfully."
    }

@router.get('/{department_id}')
def departmentData(department_id):
    return get_department_data(department_id)
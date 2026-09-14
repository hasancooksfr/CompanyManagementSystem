from fastapi import APIRouter, HTTPException

# Services
from services.departments import create_department
from services.departments import get_all_departments
from services.departments import get_department_data
from services.departments import update_department_data

# Schemas
from schemas.departments import DepartmentCreate
from schemas.departments import DepartmentUpdate

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

@router.put('/{department_id}')
def departmentUpdate(department_id, department: DepartmentUpdate):
    update_department_data(department_id, department)

    return {
        "success": True,
        "message": "Department data updated successfully."
    }
from fastapi import APIRouter, HTTPException

# Services
from services.departments import create_department

# Schemas
from schemas.departments import DepartmentCreate

router = APIRouter()

@router.get('/')
def home():
    return "Welcome to Departments API"

@router.post('/')
def department_create(department: DepartmentCreate):
    create_department(department)

    return {
        "success": True,
        "message": "Department created successfully."
    }
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get('/')
def employee_home():
    return "Employee Home" # Will replace with getting all employees
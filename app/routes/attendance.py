from fastapi import APIRouter, HTTPException

# Services
from services.attendance import check_in
from services.attendance import check_out

# Schemas
from schemas.attendance import CheckIn
from schemas.attendance import CheckOut

router = APIRouter()

@router.get('/')
def home():
    return "Welcome to Attendance Management"

@router.post('/check-in/{employee_id}')
def checkin(employee_id, data: CheckIn):
    late = check_in(employee_id, data)
    return {
        "success": True,
        "message": "Employee checked in successfully.",
        "late_seconds": late
    }

@router.post('/check-out/{employee_id}')
def checkout(employee_id, data: CheckOut):
    early = check_out(employee_id, data)
    return {
        "success": True,
        "message": "Employee checked out successfully.",
        "early_seconds": early
    }
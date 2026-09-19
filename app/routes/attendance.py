from fastapi import APIRouter, HTTPException

from services.attendance import check_in

from schemas.attendance import CheckIn

router = APIRouter()

@router.get('/')
def home():
    return "Welcome to Attendance Management"

@router.post('/check-in/{employee_id}')
def checkin(employee_id, data: CheckIn):
    late = check_in(employee_id, data)
    return {
        "success": True,
        "message": "Attendance has been marked successfully.",
        "late_seconds": late
    }
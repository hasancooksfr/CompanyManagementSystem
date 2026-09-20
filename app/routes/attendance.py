from fastapi import APIRouter, HTTPException, Query

# Services
from services.attendance import check_in
from services.attendance import check_out
from services.attendance import mark_absent
from services.attendance import attendance_summary
from services.attendance import get_attendance_of_date
from services.attendance import attendance_summary_of_date

# Schemas
from schemas.attendance import CheckIn
from schemas.attendance import CheckOut

router = APIRouter()

@router.get('/')
def attendanceSummaryOfDate(
    date: str | None = Query( None,
        pattern = r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$"
    ) 
):
    data = attendance_summary_of_date(date)
    return {
        "success": True,
        "message": "Fetched attendance summary for date.",
        "data": data
    }

@router.get('/summary/{employee_id}')
def summary(employee_id):
    data = attendance_summary(employee_id)
    return {
        "success": True,
        "message": "Fetched attendance summary for employee.",
        "data": data
    }

@router.get('/{employee_id}')
def attendanceOnDate(
    employee_id,
    date: str = Query(
        pattern = r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$"
    )
):
    return get_attendance_of_date(employee_id, date)

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

@router.post('/mark-absent')
def markabsent():
    today = mark_absent()
    return {
        "status": True,
        "message": "Marked absent for employees without check-in.",
        "date": today
    }
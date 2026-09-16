from fastapi import APIRouter, HTTPException, Query

from services.profile import fetch_profile, payroll_history

router = APIRouter()

@router.get('/{employee_id}')
def profile(employee_id):
    return fetch_profile(employee_id)

@router.get('/{employee_id}/payroll')
def payroll(
    employee_id: str,
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100)
):
    return payroll_history(employee_id, page, limit)
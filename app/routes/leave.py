from fastapi import APIRouter, HTTPException

from services.leave import create_request

from schemas.leave import createRequest

router = APIRouter()

@router.get('/')
def home():
    return "Leave Management"

@router.post('/apply/{employee_id}', status_code=201)
def apply_leave(employee_id, data: createRequest):
    create_request(employee_id, data)

    return {
        "success": True,
        "message": "Leave applied with status pending."
    }
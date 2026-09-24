from fastapi import APIRouter, HTTPException

from services.leave import create_request
from services.leave import get_requests_by_employee
from services.leave import get_request_by_id

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

@router.get('/all/{employee_id}')
def getRequestsByEmployee(employee_id):
    data = get_requests_by_employee(employee_id)

    return {
        "success": True,
        "message": "Fetched all requests for employee_id",
        "employee_id": employee_id,
        "data": data
    }

@router.get('/{request_id}')
def getRequestById(request_id):
    return get_request_by_id(request_id)
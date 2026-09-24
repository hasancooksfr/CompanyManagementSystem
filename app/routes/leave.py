from fastapi import APIRouter, HTTPException

# Services
from services.leave import create_request
from services.leave import get_requests_by_employee
from services.leave import get_request_by_id
from services.leave import update_status_of_request

# Schemas
from schemas.leave import createRequest
from schemas.leave import addReview

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

@router.patch('/{request_id}/approve')
def approveRequest(request_id, review: addReview):
    update_status_of_request(request_id, "approved", review)

    return {
        "success": True,
        "message": "Request approved successfully."
    }

@router.patch('/{request_id}/reject')
def rejectRequest(request_id, review: addReview):
    update_status_of_request(request_id, "rejected", review)
    
    return {
        "success": True,
        "message": "Request rejected successfully."
    }
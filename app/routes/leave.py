from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get('/')
def home():
    return "Leave Management"
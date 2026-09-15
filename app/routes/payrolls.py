from fastapi import APIRouter, HTTPException

# Services
from services.payrolls import create_salary_structure
from services.payrolls import view_salary_structure
from services.payrolls import calculate_net_salary

# Schemas
from schemas.payrolls import SalaryStructure

router = APIRouter()

@router.get('/')
def payroll_home():
    return "Payroll API"

@router.get('/salary-structure/{employee_id}')
def get_salary_structure(employee_id):
    return view_salary_structure(employee_id)

@router.post('/salary-structure', status_code=201)
def salary_structure(salary: SalaryStructure):
    create_salary_structure(salary)

    return {
        "success": True,
        "message": "Salary structure successfully created."
    }

@router.get('/net-salary/{employee_id}')
def net_salary(employee_id):
    net_salary = calculate_net_salary(employee_id)

    return {
        "success": True,
        "message": "Calculated net salary for employee.",
        "net_salary": net_salary
    }
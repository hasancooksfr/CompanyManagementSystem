from fastapi import APIRouter, HTTPException

# Services
from services.payrolls import create_salary_structure
from services.payrolls import view_salary_structure
from services.payrolls import calculate_net_salary
from services.payrolls import all_salary_structures
from services.payrolls import salary_structure_update
from services.payrolls import salary_structure_delete

# Schemas
from schemas.payrolls import SalaryStructure
from schemas.payrolls import SalaryStructureUpdate

router = APIRouter()

@router.get('/')
def payroll_home():
    return "Payroll API"

@router.get('/salary-structure')
def get_all_salary_structures():
    data = all_salary_structures()

    return {
        "success": True,
        "message": "Fetched all salary structures",
        "data": data
    }

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

@router.put('/salary-structure/{employee_id}')
def update_salary_structure(employee_id, salary_structure: SalaryStructureUpdate):
    salary_structure_update(employee_id, salary_structure)
    return {
        "success": True,
        "message": "Updated Salary Structure successfully."
    }

@router.delete('/salary-structure/{employee_id}')
def delete_salary_structure(employee_id):
    salary_structure_delete(employee_id)
    return {
        "success": True,
        "message": "Deleted records for employee_id"
    }

@router.get('/net-salary/{employee_id}')
def net_salary(employee_id):
    net_salary = calculate_net_salary(employee_id)

    return {
        "success": True,
        "message": "Calculated net salary for employee.",
        "net_salary": net_salary
    }
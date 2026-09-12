from database import employees_collection
from fastapi import HTTPException

def create_employee(employee):
    employee_dict = employee.model_dump()

    employee_dict['_id'] = employee_dict['employee_id']
    employees_collection.insert_one(employee_dict)

    return True
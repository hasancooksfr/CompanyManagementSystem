from database import employees_collection
from fastapi import HTTPException

def create_employee(employee):
    employee_dict = employee.model_dump()

    employee_dict['_id'] = employee_dict['employee_id']
    employees_collection.insert_one(employee_dict)

    return True

def get_all_employees():
    employees = list(employees_collection.find(
        {},
        {
            "_id": 0,
            "employee_id": 1,
            "name": 1,
            "email_id": 1,
            "department": 1
        }
    ))

    return employees

def get_employee_data(
    employee_id
):
    query = {"employee_id": employee_id}

    employee = employees_collection.find_one(
        query,
        {"_id": 0}
    )
    
    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee
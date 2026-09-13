from database import employees_collection
from fastapi import HTTPException
from pymongo.errors import DuplicateKeyError

def create_employee(employee):
    employee_dict = employee.model_dump()

    try:
        employee_dict['_id'] = employee_dict['employee_id']
        employees_collection.insert_one(employee_dict)

        return True
        
    except DuplicateKeyError:
        raise HTTPException(
            status_code=409,
            detail="Employee ID already exists."
        )

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

def update_employee_data(
    employee_id,
    employee
):
    result = employees_collection.update_one(
        {"_id": employee_id},
        {"$set": employee.model_dump(exclude_unset=True)}
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Invalid Employee ID. Employee not found."
        )

    return result

def delete_employee_data(
    employee_id
):
    result = employees_collection.delete_one(
        {"_id": employee_id}
    )

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Invalid Employee ID. Employee not found."
        )
    
    return result
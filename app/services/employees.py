from database import employees_collection
from database import departments_collection
from fastapi import HTTPException
from pymongo.errors import DuplicateKeyError

def create_employee(employee):
    employee_dict = employee.model_dump()

    result = employees_collection.find_one({"employee_id": employee_dict['employee_id']})
    if result:
        raise HTTPException(
            status_code=409,
            detail="Employee ID already exists."
        )

    if employee_dict['department_id']:
        res = departments_collection.find_one({"department_id": employee_dict['department_id']})
        if not res:
            raise HTTPException(
                status_code=404,
                detail="Department with department_id does not exist."
            )
            
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
            "department_id": 1
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
    emp = employee.model_dump(exclude_unset=True)

    if "department_id" in emp:
        res = departments_collection.find_one(
            {"department_id": emp['department_id']}
        )
        if not res:
            raise HTTPException(
                status_code=404,
                detail="Department with department_id does not exist."
            )

    result = employees_collection.update_one(
        {"employee_id": employee_id},
        {"$set": emp}
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
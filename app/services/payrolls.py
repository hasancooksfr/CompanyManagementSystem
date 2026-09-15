from database import salary_structure_collection
from database import payrolls_collection
from database import employees_collection
from fastapi import HTTPException

def create_salary_structure(salary):
    structure = salary.model_dump()

    res = employees_collection.find_one({"employee_id": structure['employee_id']})
    if not res:
        raise HTTPException(
            status_code=404,
            detail="Employee with that ID does not exist."
        )

    res1 = salary_structure_collection.find_one({"employee_id": structure['employee_id']})
    if res1:
        raise HTTPException(
            status=409,
            detail="Salary structure for that employee already exists."
        )

    salary_structure_collection.insert_one(structure)

    return True

def all_salary_structures():
    res = list(salary_structure_collection.find(
        {},
        {
            "_id": 0,
            "employee_id": 1,
            "basic_salary": 1
        }
    ))
    return res

def view_salary_structure(employee_id):
    res = salary_structure_collection.find_one({"employee_id": employee_id}, {"_id": 0})
    if not res:
        raise HTTPException(
            status_code=404,
            detail="No records found for that employee ID"
        )

    return res

def calculate_net_salary(employee_id):
    res = salary_structure_collection.find_one({"employee_id": employee_id}, {"_id": 0})
    if not res:
        raise HTTPException(
            status_code=404,
            detail="No records found for that employee ID."
        )

    basic_salary = res["basic_salary"]
    total_allowances = sum(res['allowances'].values())
    total_deductions = sum(res['deductions'].values())

    net_salary = (basic_salary + total_allowances) - total_deductions
    return net_salary
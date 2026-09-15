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
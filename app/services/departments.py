from database import departments_collection
from fastapi import HTTPException
from pymongo.errors import DuplicateKeyError

def create_department(department):
    department_dict = department.model_dump()

    result = departments_collection.find_one({
        "department_id": department_dict['department_id']
    })

    if not result:
        departments_collection.insert_one(department_dict)

        return True

    else:
        raise HTTPException(
            status_code=409,
            detail="Department ID already exists."
        )


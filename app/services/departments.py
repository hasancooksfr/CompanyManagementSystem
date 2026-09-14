from database import departments_collection
from database import employees_collection
from fastapi import HTTPException
from pymongo.errors import DuplicateKeyError

def create_department(department):
    department_dict = department.model_dump()

    result = departments_collection.find_one({
        "department_id": department_dict['department_id']
    })

    if not result:
        res = employees_collection.find_one({
            "employee_id": department_dict['manager_id']
        })

        if res:
            departments_collection.insert_one(department_dict)

            return True
        
        else:
            raise HTTPException(
                status_code=404,
                detail="Manager with ID not found."
            )
        
    else:
        raise HTTPException(
            status_code=409,
            detail="Department ID already exists."
        )

def get_all_departments():
    data = list(departments_collection.find(
        {},
        {
            "_id": 0,
            "department_id": 1,
            "name": 1,
            "manager_id": 1
        }
    ))

    return data

def get_department_data(department_id):
    data = departments_collection.find_one({
        "department_id": department_id
    }, {
        "_id": 0
    })

    if not data:
        raise HTTPException(
            status_code=404,
            detail="Department with given ID not found."
        )

    else:
        return data

def update_department_data(department_id, department):

    dep = department.model_dump(exclude_unset=True)
    dep["department_id"] = department_id

    if "manager_id" in dep:
        result = employees_collection.find_one({"employee_id": dep['manager_id']})
        if not result:
            raise HTTPException(
                status_code=404,
                detail="Employee ID with manager_id not found."
            )

    res = departments_collection.update_one(
        {"department_id": department_id},
        {"$set": dep}
    )

    if res.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Department with given ID not found."
        )

    return True

def delete_department_data(department_id):
    dep = departments_collection.delete_one({"department_id": department_id})

    if dep.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Department with that ID does not exist."
        )
    
    return True
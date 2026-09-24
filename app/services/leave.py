from fastapi import HTTPException
from database import leave_collection, employees_collection
from datetime import datetime

def create_request(employee_id, data):
    leave = data.model_dump()
    employee = employees_collection.find_one({
        "employee_id": employee_id
    })

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee with employee_id not found."
        )

    from_date = datetime.strptime(leave['from_date'], "%d-%m-%Y")
    to_date = datetime.strptime(leave['to_date'], "%d-%m-%Y")

    duration = (to_date - from_date).days + 1

    if duration <= 0:
        raise HTTPException(
            status_code=409,
            detail="to_date can't be bigger than from_date"
        )

    last_request = leave_collection.find_one({},
        sort=[("request_id", -1)]
    )

    if last_request is None:
        req_id = "LR001"
    else:
        last_id = int(last_request['request_id'].replace("LR", ""))
        req_id = f"LR{last_id+1:03d}"

    leave_collection.insert_one({
        "request_id": req_id,
        "employee_id": employee_id,
        "type": leave['leave_type'],
        "from_date": leave['from_date'],
        "to_date": leave['to_date'],
        "reason": leave['reason'],
        "status": "pending"
    })

    return True

def get_requests_by_employee(employee_id):
    data = list(leave_collection.find({
        "employee_id": employee_id
    }, {
        "_id": 0,
        "employee_id": 0,
        "reason": 0
    }))

    return data
from fastapi import HTTPException
from database import leave_collection, employees_collection
from datetime import datetime
import math

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
            status_code=422,
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

def get_request_by_id(request_id):
    data = leave_collection.find_one({
        "request_id": request_id
    }, {"_id": 0})

    if not data:
        raise HTTPException(
            status_code=404,
            detail="No request found with request_id."
        )

    return data

def update_status_of_request(request_id, status, review):
    notes = review.model_dump()

    request = leave_collection.find_one({
        "request_id": request_id
    }, {
        "_id": 0
    })

    if not request:
        raise HTTPException(
            status_code=404,
            detail="No request found with request_id."
        )

    if status == "approved" and request['status'] == "rejected":
        raise HTTPException(
            status_code=409,
            detail="Request is already rejected and cannot be marked as approved."
        )
    
    if status == "rejected" and request['status'] == "approved":
        raise HTTPException(
            status_code=409,
            detail="Request is already approved and cannot be marked as rejected."
        )

    update = leave_collection.update_one(
        {
            "request_id": request_id
        },
        {
            "$set": {
                "status": status
            }
        }
    )

    if update.modified_count == 0:
        raise HTTPException(
            status_code=409,
            detail="Request is already marked with same status."
        )

    update = leave_collection.update_one(
        {
            "request_id": request_id
        },
        {
            "$set": {
                "notes": notes['notes']
            }
        }
    )

    return True

def get_all_pending_requests(page, limit):
    skip = (page - 1) * limit

    data = list(leave_collection.find(
        {
            "status": "pending"
        },
        {
            "_id": 0,
            "request_id": 1,
            "employee_id": 1,
            "from_date": 1,
            "to_date": 1,
            "type": 1
        })
        .sort("from_date", -1)
        .skip(skip)
        .limit(limit)
    )

    total = leave_collection.count_documents({
        "status": "pending"
    })

    total_pages = math.ceil(total / limit)

    return {
        "success": True,
        "message": "Fetched all pending requests",
        "data": data,
        "pagination": {
            "page": page,
            "limit": limit,
            "total_records": total,
            "total_pages": total_pages
        }
    }
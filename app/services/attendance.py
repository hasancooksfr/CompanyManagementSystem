from database import employees_collection, attendance_collection
from fastapi import HTTPException
import json
from datetime import datetime, time

with open("config.json", "r") as file:
    config = json.load(file)

def check_in(employee_id, data):
    d = data.model_dump()

    employee = employees_collection.find_one(
        {
            "employee_id": employee_id
        }
    )
    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found."
        )

    check = attendance_collection.find_one(
        {
            "employee_id": employee_id,
            "date": d['date']
        }
    )
    if check:
        raise HTTPException(
            status_code=409,
            detail="Employee already checked in for date."
        )

    allowed_time = datetime.strptime(config['attendance']['check_in'], "%H:%M:%S").time()
    check_in_timings = d['check_in']

    check_in_seconds = (
        check_in_timings.hour * 3600 +
        check_in_timings.minute * 60 +
        check_in_timings.second
    ) 

    allowed_seconds = (
        allowed_time.hour * 3600 + 
        allowed_time.minute * 60 +
        allowed_time.second
    )
    if check_in_seconds > allowed_seconds:
        late_seconds = check_in_seconds - allowed_seconds

    else:
        late_seconds = None


    resource = {
        "employee_id": employee_id,
        "date": d['date'],
        "check_in": d['check_in'].strftime("%H:%M:%S"),
        "check_out": None,
        "late_seconds": (f"{late_seconds}" if late_seconds else "not late"),
        "mark": "Present"
    }
    attendance_collection.insert_one(resource)
    
    return late_seconds
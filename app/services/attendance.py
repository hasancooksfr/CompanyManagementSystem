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
        "late_seconds": late_seconds,
        "early_seconds": None,
        "mark": "Present"
    }
    attendance_collection.insert_one(resource)
    
    return late_seconds

def check_out(employee_id, data):
    d = data.model_dump()

    attendance = attendance_collection.find_one({
        "employee_id": employee_id,
        "date": d['date']
    }, {"_id": 0})

    if not attendance:
        raise HTTPException(
            status_code=404,
            detail="Employee ID did not check in for date."
        )

    if attendance['check_out']:
        raise HTTPException(
            status_code=409,
            detail="Employee already checked out for date."
        )

    allowed_time = datetime.strptime(config['attendance']['check_out'], "%H:%M:%S").time()
    check_out_timing = d['check_out']

    check_out_seconds = (
        check_out_timing.hour * 3600 +
        check_out_timing.minute * 60 +
        check_out_timing.second
    )

    allowed_seconds = (
        allowed_time.hour * 3600 +
        allowed_time.minute * 60 +
        allowed_time.second
    )

    if allowed_seconds > check_out_seconds:
        early_seconds = allowed_seconds - check_out_seconds
    else:
        early_seconds = None

    attendance_collection.update_one(
        {
            "employee_id": employee_id,
            "date": d['date']
        },
        {
            "$set": {
                "check_out": d['check_out'].strftime("%H:%M:%S"),
                "early_seconds": early_seconds
            }
        }
    )
    return early_seconds

def mark_absent():
    today = datetime.now().strftime("%d-%m-%Y")
    employees = employees_collection.find(
        {
            "employment_status": "active"
        }
    )

    for employee in employees:
        employee_id = employee['employee_id']

        attendance = attendance_collection.find_one({
            "employee_id": employee_id,
            "date": today
        })

        if not attendance:
            attendance_collection.insert_one({
                "employee_id": employee_id,
                "date": today,
                "check_in": None,
                "check_out": None,
                "late_seconds": None,
                "early_seconds": None,
                "mark": "Absent"
            })

    return today
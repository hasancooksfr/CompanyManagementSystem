from database import employees_collection, payrolls_collection, departments_collection, salary_structure_collection
from fastapi import HTTPException
from services.attendance import attendance_summary
import math

def fetch_profile(employee_id):
    employee = employees_collection.find_one(
        {
            "employee_id": employee_id
        },
        {
            "_id": 0
        }
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee with employee_id does not exist."
        )

    department = departments_collection.find_one(
        {
            "department_id":  employee['department_id']
        },
        {
            "_id": 0
        }
    )

    if not department:
        if employee['department_id'] != "NOT ASSIGNED":
            employees_collection.update_one(
                {
                    "employee_id": employee_id
                },
                {
                    "$set": {
                        "department_id": "NOT ASSIGNED",
                        "employment_status": "changes_required"
                    }
                }
            )

        raise HTTPException(
            status_code=404,
            detail="Department with department_id does not exist"
        )

    manager = employees_collection.find_one({"employee_id": department['manager_id']}, {"_id": 0, "name": 1, "email_id": 1})

    attendance = attendance_summary(employee_id)

    return {
        "employee_id": employee_id,
        "name": employee['name'],
        "email_id": employee['email_id'],
        "phone_number": employee['phone_number'],
        "date_of_joining": employee['date_of_joining'],
        "job_title": employee['job_title'],
        "department": department['name'],
        "department_id": department['department_id'],
        "manager": {
            "manager_id": department['manager_id'],
            "manager_name": manager['name'],
            "manager_email_id": manager['email_id']
        },
        "salary": employee['salary'],
        "attendance": {
            "working_days": attendance['active_days'],
            "present_days": attendance['present_days'],
            "absent_days":  attendance['absent_days']
        },
        "employment_status": employee['employment_status']
    }

def payroll_history(employee_id, page, limit):
    employee = employees_collection.find_one({"employee_id": employee_id})
    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee with employee_id does not exist."
        )

    skip = (page - 1) * limit

    pay_his = list(
        payrolls_collection.find(
            {
                "employee_id": employee_id,
                "status": 'paid'
            },
            {
                "_id": 0
            }
        )
        .sort('month', -1)
        .skip(skip)
        .limit(limit)
    )

    total = payrolls_collection.count_documents(
        {
            "employee_id": employee_id,
            "status": "paid"
        }
    )
    total_pages = math.ceil(total / limit)

    return {
        "success": True,
        "message": "Fetched employee payroll history",
        "data": pay_his,
        "pagination": {
            "page": page,
            "limit": limit,
            "total_records": total,
            "total_pages": total_pages
        }
    }


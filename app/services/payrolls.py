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

def salary_structure_update(employee_id, salary_structure):
    ss = salary_structure.model_dump(exclude_unset=True)
    res = salary_structure_collection.update_one(
        {
            "employee_id": employee_id
        },
        {
            "$set": ss
        }
    )

    if res.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="No records found for employee_id."
        )

    return True

def salary_structure_delete(employee_id):
    res = salary_structure_collection.delete_one(
        {
            "employee_id": employee_id
        }
    )

    if res.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="No records found for employee_id"
        )

    return True

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

def generate_payroll(employee_id, payroll):
    data = payroll.model_dump()
    res = salary_structure_collection.find_one({"employee_id": employee_id}, {"_id": 0})
    if not res: 
        raise HTTPException(
            status_code=404,
            detail="No salary structure found for that employee ID."
        )

    res1 = payrolls_collection.find_one(
        {
            "employee_id": employee_id,
            "month": data['month']
        }
    )
    if res1:
        raise HTTPException(
            status_code=409,
            detail="Payroll already generated for employee_id in month."
        )

    basic_salary = res['basic_salary']
    total_allowances = sum(res['allowances'].values())
    total_deductions = sum(res['deductions'].values())

    net_salary = (basic_salary + total_allowances) - total_deductions

    last_payroll = payrolls_collection.find_one({},
        sort=[("payroll_id", -1)]
    )

    if last_payroll is None:
        payroll_id = "PAY001"
    else:
        last_id = int(last_payroll['payroll_id'].replace("PAY", ""))
        payroll_id = f"PAY{last_id+1:03d}"

    payroll1 = {
        "payroll_id": payroll_id,
        "employee_id": employee_id,
        "month": data['month'],
        "basic_salary": basic_salary,
        "allowances": res['allowances'],
        "deductions": res['deductions'],
        "net_salary": net_salary,
        "status": "generated"
    }

    payrolls_collection.insert_one(payroll1)

    return payroll_id

def get_all_payrolls(month, status, employee_id, payroll_id):
    query = {}

    if month:
        query['month'] = month

    if status:
        query['status'] = status

    if employee_id:
        query['employee_id'] = employee_id

    if payroll_id:
        query['payroll_id'] = payroll_id

    res = list(payrolls_collection.find(
        query,
        {
            "_id": 0,
            "payroll_id": 1,
            "employee_id": 1,
            "month": 1,
            "net_salary": 1,
            "status": 1
        }
    ))

    return res

def get_payroll(employee_id, month):
    res = payrolls_collection.find_one(
        {
            "employee_id": employee_id,
            "month": month,
            "status": {"$in": ["generated", "paid"]}
        },
        {
            "_id": 0
        }
    )

    if not res:
        raise HTTPException(
            status_code=404,
            detail="Payroll for employee_id and month does not exist with status 'generated' or 'paid'."
        )

    return res

def get_payroll_by_payroll_id(payroll_id):
    res = payrolls_collection.find_one({
        "payroll_id": payroll_id
    }, {
        "_id": 0
    })

    if not res:
        raise HTTPException(
            status_code=404,
            detail="Payroll with payroll_id does not exist."
        )

    return res

def update_status_of_payroll(payroll_id, status):
    payroll = payrolls_collection.find_one(
        {
            "payroll_id": payroll_id
        },
        {
            "_id": 0
        }
    )
    
    if not payroll:
        raise HTTPException(
            status_code=404,
            detail="Payroll does not exist with payroll_id"
        )

    if status == 'paid' and payroll['status'] == 'cancelled':
        raise HTTPException(
            status_code=409,
            detail="Cancelled payroll can not be marked as paid"
        )

    res = payrolls_collection.update_one(
        {
            "payroll_id": payroll_id
        },
        {
            "$set": {
                "status": status
            }
        }
    )

    if res.modified_count == 0:
        raise HTTPException(
            status_code=409,
            detail="Payroll is already marked with same status."
        )

    return True
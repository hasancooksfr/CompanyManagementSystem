# Payroll Management
This document gives a detailed information about **Payroll Management**. It is the third module of Company Management System.

It provides basic management for employee salary structures and payroll records.

# Features
- Create salary structure for an employee
- View all salary strucutures
- View detailed salary structure for an employee
- Update salary structure
- Delete salary structure
- Calculate Net Salary of an employee
- Generate monthly payroll for an employee
- View all payroll records
- View payroll details
- View employee payroll history
- Filter payroll details by Month and Status
- Mark payroll as paid
- Cancel generated payroll

# Salary Strucuture

A salary structure currently contains:
```text
Employee ID
Basic Salary
Allowances
Deductions
```

# Payroll Information

A payroll record currently includes:
```text
Payroll ID
Employee ID
Month (MM-YYYY)
Basic Salary
Allowances
Deductions
Net Salary
Status (generated/paid/cancelled)
```

The net salary is calculed using:
`Net Salary = (Basic Salary + Allowances) - Deductions`

# API Endpoints
## Get all Salary Structures
```http
GET /payroll/salary-structure
```
Returns a list of `employee_id` and `basic_salary`

Example:
```JSON
{
    "success": true,
    "message": "Fetched all salary structures",
    "data": [
        {
            "employee_id": "EMP001",
            "basic_salary": 10000
        },
        {
            "employee_id": "EMP002",
            "basic_salary": 350000
        }
    ]
}
```

## Get Salary Structure of a specific employee
```http
GET /payroll/salary-structure/{employee_id}
```
Returns full salary strucuture of that employee.

Example:
```JSON
{
    "employee_id": "EMP001",
    "basic_salary": 10000,
    "allowances": {
        "house rent": 5000,
        "transportation": 1000
    },
    "deductions": {
        "TDS": 1000
    }
}
```

## Create Salary Structure
```http
POST /payroll/salary-structure/
```

Example request:
```JSON
{
    "employee_id": "EMP001",
    "basic_salary": 10000,
    "allowances": {
        "house rent": 5000,
        "transportation": 1000
    },
    "deductions": {
        "TDS": 1000
    }
}
```

## Update Salary Strucuture of an employee
```http
PUT /payroll/salary-structure/{employee_id}
```

## Delete Salary Structure of an employee
```http
DELETE /payroll/salary-structure/{employee_id}
```

## Get all payroll records
```http
GET /payroll/
```
Returns a list of all payroll records.

Payroll records can be filtered using `month`, `status` and `employee_id` query parameters.
Same can be used to get employee payroll history.

Example:
```http
GET /payroll/?month=09-2026&status=generated?employee_id=EMP001
```

## Get payroll details of a specific employee (By employee ID & month)
```http
GET /payroll/{employee_id}?month={month}
```
Returns full payroll record, only if the status is `generated` or `paid`.

Example:
```http
GET /payroll/EMP001?month=09-2026
```

## Get payroll details (By payroll ID)
```http
GET /payroll/payroll-id/{payroll_id}
```

## Generate monthly payroll of an employee
```http
POST /payroll/generate/{employee_id}
```
Generates a payroll record for a specific employee and month

Example request:
```JSON
{
    "month": "09-2026"
}
```
The month must be provided in `MM-YYYY` format only.

The net salary is automatically calculated using the employee's salary strucuture.

### Checks:
If salary structure is not found, it returns an error.
It checks if employee is already having a payroll record for same month with status of `generated` or `paid` and only proceeds if not found.

##  Mark payroll as PAID
```http
PATCH /payroll/{payroll_id}/pay
```
Marks a payroll record as paid.

A payroll that is already paid or cancelled cannot be marked as paid.

## Mark payroll as CANCELLED
```http
PATCH /payroll/{payroll_id}/cancel
```
Marks a payroll record as cancelled.

A payroll that is already paid or cancelled cannot be marked as cancelled.

## Calculate only Net Salary of a specific employee
```http
GET /payroll/net-salary/{employee_id}
```
Calculates and returns Net Salary of an employee without generating a payroll

# Screenshots
## Salary Structure Creation
![Salary Salary Creation](/assets/payroll-management/create_salary_structure.png)

## Get all Salary Structures
![Get all Salary Structures](/assets/payroll-management/get_all_salary_strucutures.png)

## Get Salary Structure
![Get Salary Structure](/assets/payroll-management/get_salary_structure.png)

## Update Salary Structure
![Update Salary Structure](/assets/payroll-management/update_salary_structure.png)

## Delete Salary Structure
![Delete Salary Structure](/assets/payroll-management/delete_salary_structure.png)

## Generate Payroll
![Generate Payroll](/assets/payroll-management/create_payroll.png)

## Get all Payroll records
![Get all Payroll records](/assets/payroll-management/get_all_payrolls.png)

## Get Payroll record by Employee ID and Month
![Get Payroll record by Employee ID and Month](/assets/payroll-management/get_payroll_details.png)

## Get Payroll record by Payroll ID
![Get Payroll record by Payroll ID](/assets/payroll-management/get_payroll_details_by_payroll_id.png)

## Mark Payroll record as Paid
![Mark Payroll record as Paid](/assets/payroll-management/mark_payroll_as_paid.png)

## Mark Payroll record as Cancelled
![Mark Payroll record as Cancelled](/assets/payroll-management/mark_payroll_as_cancelled.png)

## Calculate Net Salary
![Calculate Net Salary](/assets/payroll-management/net_salary.png)

# Testing
The payroll management feature has been tested for:

- Creating salary structures
- Retrieving salary structures
- Updating salary structures
- Generating monthly payroll records
- Calculating net salary
- Retrieving payroll records
- Filtering payroll records by month and status
- Retrieving employee payroll history
- Marking payroll as paid
- Cancelling generated payroll
- Invalid employee_id or payroll_id errors
- Invalid month format
- Duplicate payroll records for the same employee and month
- Invalid payroll status transitions